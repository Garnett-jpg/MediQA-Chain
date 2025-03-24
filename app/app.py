from transformers import pipeline
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import gradio as gr
import torch

# Load FAISS index and text embedding model
index = faiss.read_index("knowledge_base/medical_index.faiss")
model = SentenceTransformer('all-MiniLM-L6-v2')

with open("data/cleaned_abstracts.txt", "r", encoding="utf-8") as f:
    cleaned_abstracts = f.readlines()

def retrieve_documents(query, top_k=5):
    """Retrieve the most relevant medical documents"""
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(np.array(query_embedding), top_k)
    
    # Handle exceptions to prevent IndexError when indices are empty
    retrieved_docs = [cleaned_abstracts[i] for i in indices[0] if i < len(cleaned_abstracts)]
    return retrieved_docs if retrieved_docs else ["No relevant documents found."]

# Load the Qwen model, prioritize GPU usage if available
generator = pipeline("text-generation", model="Qwen/Qwen-1_8B", trust_remote_code=True)

def generate_answer(query, context):
    """Generate a medical answer based on retrieved documents"""
    input_text = f"\nQuestion: {query}\nContext:\n{context}\nAnswer:"
    answer = generator(input_text, max_new_tokens=1024, do_sample=True, temperature=0.7, num_return_sequences=1)
    return answer[0]['generated_text']

# Gradio interactive interface
def qa_pipeline(query):
    """Gradio answer pipeline"""
    retrieved_docs = retrieve_documents(query)
    context = " ".join(retrieved_docs)
    answer = generate_answer(query, context)
    return answer

# Create Gradio interface
iface = gr.Interface(
    fn=qa_pipeline,
    inputs=gr.Textbox(lines=2, placeholder="Type your medical question here..."),
    outputs="text",
    title="MediQA-Chain: Medical Question Answering System",
    description="Ask any medical question and get an AI-generated answer based on medical literature!"
)

# Launch Gradio service
iface.launch(share=True)

