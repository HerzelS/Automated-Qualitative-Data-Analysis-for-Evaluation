import pandas as pd
from src.data_loader import load_documents_from_directory as load_documents_from_folder
from src.preprocessing import preprocess_texts
from src.sentiment import analyze_sentiment
from src.sentiment_mapping import map_response_semantic
#from src.dashboard import build_dashboard

def run_pipeline(data_folder="./data", framework="DAC"):
    """
    End-to-end pipeline:
    1. Load documents from folder (txt, csv, docx, json, pdf)
    2. Preprocess text
    3. Sentiment analysis
    4. Semantic mapping (DAC or ALNAP)
    5. Launch dashboard
    """
    print(f"Loading documents from {data_folder}...")
    df = load_documents_from_folder(data_folder)

    print("Preprocessing texts...")
    texts_clean = preprocess_texts(df["response"].dropna().tolist())

    print("Analyzing sentiment...")
    df["sentiment"] = analyze_sentiment(df["response"].tolist())

    print(f"Mapping responses to {framework} criteria...")
    df["mapping"] = df["response"].apply(lambda x: map_response_semantic(x, framework=framework))

    print("Launching dashboard...")
    # Dashboard expects a CSV path, so we save the processed responses temporarily
    temp_path = data_folder + "/_processed_responses.csv"
    df.to_csv(temp_path, index=False)
  #  app = build_dashboard(data_path=temp_path)
  #  app.run_server(debug=True)

if __name__ == "__main__":
    # Example usage: run pipeline on sample data with DAC framework
    run_pipeline(data_folder="./data", framework="DAC")
