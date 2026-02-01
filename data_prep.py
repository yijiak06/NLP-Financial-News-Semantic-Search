import os
import pandas as pd
from tqdm import tqdm

# ================= Configuration =================
# Use relative paths for better portability on GitHub
CSV_PATH = 'dataset.csv'
OUTPUT_DIR = 'news_documents'
# =============================================

def prepare_data():
    print(f" Reading data from {CSV_PATH}...")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    try:
        # 1. Load Data
        df = pd.read_csv(CSV_PATH)
        print(f"Original rows: {len(df)}")

        # 2. Data Cleaning
        # Remove rows where 'Content' is an exact duplicate
        df_clean = df.drop_duplicates(subset=['Content']).copy()
        
        # Filter out empty strings, pure whitespace, and artifact '[]' values
        # We ensure 'Content' is treated as a string first
        df_clean = df_clean[df_clean['Content'].astype(str).str.strip().str.len() > 0]
        df_clean = df_clean[df_clean['Content'].astype(str).str.strip() != '[]']
        df_clean = df_clean[df_clean['Content'].astype(str) != 'nan']
        
        print(f" Rows after cleaning: {len(df_clean)}")
        print(f" Starting file generation...")

        # 3. Generate Document Files
        # Using tqdm to show a progress bar
        for index, row in tqdm(df_clean.iterrows(), total=len(df_clean), desc="Saving files"):
            
            # Create a safe filename using the Subject (first 50 chars)
            # Replace illegal characters for file systems
            safe_subject = str(row['Subject'])[:50].replace("/", "_").replace("\\", "_").replace(":", "-").strip()
            filename = f"{index}_{safe_subject}.txt"
            file_path = os.path.join(OUTPUT_DIR, filename)
            
            # Combine Subject and Content for better semantic search context
            full_text = f"{str(row['Subject'])}\n\n{str(row['Content'])}"
            
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(full_text)
            except Exception as e:
                print(f"Could not save file {filename}: {e}")

        print(f"\n Success! {len(df_clean)} valid documents saved to '{OUTPUT_DIR}'.")

    except FileNotFoundError:
        print(f" Error: Could not find {CSV_PATH}. Please ensure the file exists.")
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    prepare_data()