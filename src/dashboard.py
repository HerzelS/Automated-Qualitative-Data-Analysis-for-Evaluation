import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from src.sentiment_mapping import map_response_semantic
from src.sentiment import analyze_sentiment

def build_dashboard(data_path="../data/sample_responses.csv"):
    df = pd.read_csv(data_path)

    app = Dash(__name__)
    app.title = "Evaluation Dashboard"

    app.layout = html.Div([
        html.H1("Evaluation Dashboard"),
        html.Label("Select Framework:"),
        dcc.Dropdown(
            id="framework-dropdown",
            options=[
                {"label": "DAC Criteria", "value": "DAC"},
                {"label": "ALNAP Criteria", "value": "ALNAP"}
            ],
            value="DAC",
            clearable=False
        ),
        dcc.Graph(id="criterion-bar"),
        html.H3("Sample Responses"),
        html.Div(id="response-list")
    ])

    @app.callback(
        [Output("criterion-bar", "figure"),
         Output("response-list", "children")],
        [Input("framework-dropdown", "value")]
    )
    def update_dashboard(framework):
        # Map responses to selected framework
        df["mapping"] = df["response"].apply(lambda x: map_response_semantic(x, framework=framework))
        df["criterion"] = df["mapping"].apply(lambda m: m[0]["criterion"] if m else None)
        df["question"] = df["mapping"].apply(lambda m: m[0]["matched_question"] if m else None)
        df["score"] = df["mapping"].apply(lambda m: m[0]["score"] if m else None)

        # Sentiment analysis
        df["sentiment"] = analyze_sentiment(df["response"].tolist())

        # Aggregate: count + average sentiment per criterion
        agg = df.groupby("criterion").agg(
            count=("criterion", "size"),
            avg_sentiment=("sentiment", "mean")
        ).reset_index()

        # Bar chart with sentiment coloring
        fig = px.bar(
            agg,
            x="criterion",
            y="count",
            color="avg_sentiment",
            color_continuous_scale=["red", "yellow", "green"],
            title=f"Responses Mapped to {framework} Criteria (Sentiment Overlay)"
        )

        # Response list
        response_items = [
            html.Li(f"{row['response']} → {row['criterion']} ({row['question']}) "
                    f"[score: {row['score']:.2f}, sentiment: {row['sentiment']:.2f}]")
            for _, row in df.iterrows()
        ]

        return fig, html.Ul(response_items)

    return app

if __name__ == "__main__":
    app = build_dashboard()
    app.run(debug=True)