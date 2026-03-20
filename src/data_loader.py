import os
import pandas as pd
import docx
import json
import PyPDF2

print("Current working directory:", os.getcwd())

def load_documents_from_directory(directory: str, file_types=("txt", "csv", "docx", "json", "pdf")) -> pd.DataFrame:
    """
    Load document from a specified directory and return a DataFrame with the content.
    Args:
        directory (str): The path to the directory containing the documents.
        file_types (tuple): A tuple of file extensions to consider.
    Returns:
        pd.DataFrame: A DataFrame with columns 'filename' and 'content'.
    """
    responses = []
    
    for filename in os.listdir(directory):
        ext = filename.split('.')[-1].lower()
        file_path = os.path.join(directory, filename)
        
        if ext in file_types:
            try:
                if ext == "txt":
                    with open(file_path, "r", encoding="utf-8") as file:
                        for line in file:
                            if line.strip():
                                responses.append(line.strip())
                                
                elif ext == "csv":
                    df = pd.read_csv(file_path)
                    if "response" in df.columns:
                        responses.extend(df["response"].dropna().tolist())
                        
                elif ext == "docx":
                    doc = docx.Document(file_path)
                    for para in doc.paragraphs:
                        if para.text.strip():
                            responses.append(para.text.strip())
                            print(responses)
                            
                elif ext == "json":
                    with open(file_path, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        if isinstance(data, list):
                            for item in data:
                                if isinstance(item, dict) and "response" in item:
                                    responses.append(item["response"])
                                    
                elif ext == "pdf":
                    with open (file_path, "rb") as file:
                        reader = PyPDF2.PdfReader(file)
                        for page in reader.pages:
                            text = page.extract_text()
                            if text:
                                for line in text.splitlines():
                                    if line.strip():
                                        responses.append(line.strip())
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
                
                
#a = load_documents_from_directory("data")
#a 


