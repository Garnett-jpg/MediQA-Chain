from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load the pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert text into vectors
cleaned_abstracts = open("data/cleaned_abstracts.txt", "r", encoding="utf-8").readlines()
embeddings = model.encode(cleaned_abstracts)

# Create a FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save the index
faiss.write_index(index, "knowledge_base/medical_index.faiss")

# Load the FAISS index
index = faiss.read_index("knowledge_base/medical_index.faiss")

# Check how many vectors are stored in the index
print("Number of vectors in FAISS index:", index.ntotal)
