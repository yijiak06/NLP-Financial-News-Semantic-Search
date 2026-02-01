import os
import sys
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sklearn.metrics.pairwise import cosine_similarity

# ================= Configuration =================
DATA_DIR = "news_documents" 
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_NAME = "google/flan-t5-base"
# =============================================

def load_documents(data_dir):
    """Loads all .txt files from the data directory."""
    if not os.path.exists(data_dir):
        print(f" Error: Directory '{data_dir}' not found.")
        return []
    
    files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]
    documents = []
    
    print(f" Loading {len(files)} documents...")
    for filename in tqdm(files, desc="Reading files"):
        path = os.path.join(data_dir, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if len(text) > 50: # Skip very short files
                    documents.append({"source": filename, "text": text})
        except Exception:
            continue
    return documents

def build_index(documents):
    """Generates embeddings for the document collection."""
    print("\n Generating embeddings... This may take a moment.")
    model = SentenceTransformer(MODEL_NAME)
    # Truncate text to 500 chars for indexing speed
    texts = [d["text"][:500] for d in documents] 
    embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=True)
    return model, embeddings

def setup_llm():
    """Loads the Flan-T5 model for Question Answering."""
    print("\n Loading LLM model...")
    tokenizer = AutoTokenizer.from_pretrained(LLM_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(LLM_NAME)
    return tokenizer, model

def search_and_answer(query, docs, embed_model, embeddings, llm_tokenizer, llm_model):
    """Core logic: Semantic Search + LLM Generation (RAG)."""
    
    # --- 1. Semantic Search ---
    q_emb = embed_model.encode([query], normalize_embeddings=True)
    scores = cosine_similarity(q_emb, embeddings)[0]
    
    # Retrieve top 3 results
    top_k_indices = np.argsort(-scores)[:3]
    
    # Collect results with their scores
    results = []
    for i in top_k_indices:
        doc = docs[i]
        doc['score'] = scores[i] # Store the score
        results.append(doc)
    
    # --- 2. LLM Answer Generation ---
    context = " ".join([r["text"][:300] for r in results])
    prompt = f"Question: {query}\nContext: {context}\nAnswer:"
    
    inputs = llm_tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids
    outputs = llm_model.generate(inputs, max_length=128, num_beams=4, early_stopping=True)
    answer = llm_tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return answer, results

def main():
    print("=== 📈 Financial News Semantic Search Engine (CLI) ===")
    
    # Initialization
    docs = load_documents(DATA_DIR)
    if not docs:
        print("Please ensure data_prep.py has been run and 'news_documents' exists.")
        return
    
    embed_model, embeddings = build_index(docs)
    llm_tokenizer, llm_model = setup_llm()
    
    print("\n System Ready!")
    
    # Interaction Loop
    while True:
        try:
            query = input("\n Enter your question (or type 'exit' to quit): ")
            
            if query.lower() in ['exit', 'quit', 'q']:
                print(" Goodbye!")
                break
                
            if not query.strip():
                continue
                
            print(" AI is thinking...")
            answer, sources = search_and_answer(query, docs, embed_model, embeddings, llm_tokenizer, llm_model)
            
            print(f"\n AI Answer: {answer}")
            print("\n References (Top 3):")
            for i, src in enumerate(sources, 1):
                # Display source name and its similarity score
                print(f"   {i}. {src['source']} (Score: {src['score']:.4f})")
                
        except KeyboardInterrupt:
            print("\n Exiting...")
            break
        except Exception as e:
            print(f" An error occurred: {e}")

if __name__ == "__main__":
    main()