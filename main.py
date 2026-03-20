import pandas as pd
from src.data_loader import load_documents_from_directory as load_documents_from_folder
from src.preprocessing import preprocess_texts
from src.sentiment import analyze_sentiment
from src.sentiment_mapping import map_response_semantic
from src.visualization import plot_wordcloud, plot_sentiment_distribution
from src.dashboard import build_dashboard

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
    
    print(df[["response", "sentiment"]].head())

    print(f"Mapping responses to {framework} criteria...")
    df["mapping"] = df["response"].apply(lambda x: map_response_semantic(x, framework=framework))
    
    # Plot word cloud and sentiment distribution
    print("Generating visualizations...")
    plot_wordcloud(texts_clean)
    plot_sentiment_distribution(df["sentiment"])
    
    # Save processed data for dashboard
    processed_path = f"{data_folder}/processed_responses.csv"
    df.to_csv(processed_path, index=False)
    print(f"Processed data saved to {processed_path}")

    print("Launching dashboard...")
    app = build_dashboard(data_path=processed_path)
    app.run(debug=True)

if __name__ == "__main__":
    # Example usage: run pipeline on sample data with DAC framework
    run_pipeline(data_folder="./data", framework="DAC")