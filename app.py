import streamlit as st
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sklearn.metrics.pairwise import cosine_similarity

# ================= Configuration =================
# Ensure this matches your folder name
DATA_DIR = "news_documents" 
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_NAME = "google/flan-t5-base"
# =============================================

# Page Setup
st.set_page_config(page_title="Financial News Search", page_icon="📈")
st.title("📈 Financial News Semantic Search")
st.markdown("Semantic Search Engine powered by **SBERT** (Retrieval) and **Flan-T5** (Generation).")

@st.cache_resource
def load_models():
    # 1. Load Documents
    documents = []
    if os.path.exists(DATA_DIR):
        files = [f for f in os.listdir(DATA_DIR) if f.endswith(".txt")]
        for filename in files:
            path = os.path.join(DATA_DIR, filename)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                    if len(text) > 50:
                        documents.append({"source": filename, "text": text})
            except:
                continue
    
    # 2. Load Embedding Model
    embed_model = SentenceTransformer(MODEL_NAME)
    texts = [d["text"][:500] for d in documents]
    embeddings = embed_model.encode(texts, normalize_embeddings=True)
    
    # 3. Load LLM
    tokenizer = AutoTokenizer.from_pretrained(LLM_NAME)
    llm_model = AutoModelForSeq2SeqLM.from_pretrained(LLM_NAME)
    
    return documents, embed_model, embeddings, tokenizer, llm_model

# Loading Spinner
with st.spinner('Loading engine and models, please wait...'):
    docs, embed_model, embeddings, tokenizer, llm_model = load_models()

st.success(f"System Ready! Loaded {len(docs)} documents.")

# Interface
query = st.text_input("Enter your question:", placeholder="e.g., Who announced cash dividends?")
run_search = st.button("🔍 Search & Answer")

if run_search and query:
    # --- 1. Semantic Search Logic ---
    # Encode the query
    q_emb = embed_model.encode([query], normalize_embeddings=True)
    
    # Calculate Cosine Similarity Scores
    scores = cosine_similarity(q_emb, embeddings)[0]
    
    # Get Top 3 Indices
    top_k_indices = np.argsort(-scores)[:3]
    
    # Retrieve Results and Attach Scores
    results = []
    for i in top_k_indices:
        doc = docs[i]
        doc['score'] = scores[i] # Add score to the document object
        results.append(doc)
    
    # --- 2. LLM Generation Logic ---
    context = " ".join([r["text"][:300] for r in results])
    prompt = f"Question: {query}\nContext: {context}\nAnswer:"
    
    input_ids = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True).input_ids
    outputs = llm_model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # --- 3. Display Results ---
    st.markdown("### 💡 AI Answer")
    st.info(answer)
    
    st.markdown("### 📄 Reference Documents (Ranked by Similarity)")
    for r in results:
        # Display filename AND the similarity score
        with st.expander(f"Source: {r['source']} (Score: {r['score']:.4f})"):
            st.write(r['text'][:1000] + "...")
            st.caption(f"Full Similarity Score: {r['score']}")