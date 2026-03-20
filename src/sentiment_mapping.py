from sentence_transformers import SentenceTransformer, util
from src.evaluation_criteria import DAC_CRITERIA, ALNAP_CRITERIA
from src.evaluation_questions import EVAL_QUESTIONS as EQs

model = SentenceTransformer('all-MiniLM-L6-v2')

def map_response_semantic(text: str, framework="DAC", top_k=1):
    
    if framework == "DAC":
        criteria = DAC_CRITERIA
        questions = EQs
        
    elif framework == "ALNAP":
        criteria = ALNAP_CRITERIA
        questions = EQs
        
    else:
        raise ValueError("Unsupported framework. Choose 'DAC' or 'ALNAP'.")

    corpus = []
    mapping_index = []

    for criterion, question_list in questions.items():
        for q in question_list:
            corpus.append(q)
            mapping_index.append((criterion, q))

    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embedding = model.encode(text, convert_to_tensor=True)

    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=top_k)[0]

    results = []
    for hit in hits:
        criterion, question = mapping_index[hit["corpus_id"]]

        results.append({
            "criterion": criterion,
            "definition": criteria.get(criterion, "Definition not found"),
            "matched_question": question,
            "score": float(hit["score"])
        })

    return results