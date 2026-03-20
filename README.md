# Automated-Qualitative-Data-Analysis-for-Evaluation

## Overview
As an evaluation professional who is also an AI enthusiast, this project focuses on making analysis of qualitative data much easier with the help of AI using python.

The project provides an end-to-end pipeline for analyzing qualitative data in evaluation contexts. It ingests documents (TXT, CSV, DOCX, JSON, PDF), preprocesses text, performs sentiment analysis, maps responses to DAC and ALNAP evaluation criteria using semantic similarity, and visualizes results in an interactive dashboard.


## Folder Structure
```text
automated-qual-analysis/
├── data/
│   └── sample_responses.csv        # Example dataset
├── notebooks/
│   └── 01_text_analysis.ipynb      # Optional exploratory notebook
├── src/
│   ├── preprocessing.py            # Text cleaning + stopwords
│   ├── topic_modeling.py           # BERTopic modeling
│   ├── sentiment.py                # VADER sentiment analysis
│   ├── visualization.py            # Wordcloud + sentiment plots
│   ├── evaluation_criteria.py      # DAC and ALNAP definitions
│   ├── evaluation_questions.py     # DAC evaluation questions
│   ├── alnap_criteria.py           # ALNAP definitions
│   ├── semantic_mapping.py         # Transformer-based semantic mapping
│   ├── data_loader.py              # Load TXT, CSV, DOCX, JSON, PDF
│   └── dashboard.py                # Interactive Plotly/Dash dashboard
├── main.py                         # Orchestration script (run pipeline)
├── requirements.txt                # All dependencies
└── README.md                       # Documentation & usage instructions

```
## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-org/automated-qual-analysis.git
cd automated-qual-analysis
pip install -r requirements.txt
````
## Usage

1. Place your qualitative data files (TXT, CSV, DOCX, JSON, PDF) inside the `data/` folder.
Example: `data/sample_responses.csv`
2. Run the pipeline:
````bash
python main.py
````
3. The pipeline will:

  - Load and preprocess all documents.

  - Perform sentiment analysis.

  - Map responses to DAC (default) or ALNAP criteria.

  - Save a processed CSV.

  - Launch the interactive dashboard at `http://127.0.0.1:8050`.

## Switching Frameworks
By default, the pipeline uses DAC criteria. To switch to ALNAP, edit `main.py`:

````python
run_pipeline(data_folder="./data", framework="ALNAP")
````

## Features

- Flexible ingestion: TXT, CSV, DOCX, JSON, PDF.
- Preprocessing: Stopword removal, text cleaning.
- Sentiment analysis: VADER compound scores.
- Semantic mapping: Transformer embeddings match responses to DAC/ALNAP criteria & evaluation questions.
- Visualization: Interactive dashboard with sentiment overlay [under development].

## Example Output  

A word cloud showing the most occuring words:

![Word Cloud Screenshot](docs/word.png)

A sentiment distribution:

![Sentiment Distribution Plot Screenshot](docs/sentiment.png)

## Next Steps

- Add argparse to main.py for command-line options (--framework DAC/ALNAP, --data ./data).
- Extend dashboard with filters (e.g., show only negative responses).
- Add time-series sentiment trends if responses are timestamped.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

## License
MIT License
