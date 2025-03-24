# MediQA-Chain

**MediQA-Chain** is a question-answering system based on medical literature. It retrieves relevant information from PubMed abstracts and generates accurate answers based on user queries. This project integrates Retrieval-Augmented Generation (RAG) technology and large language models (LLMs) to provide an efficient QA tool for the medical field.

## Features

- **Literature Download**: Retrieves medical abstracts from PubMed.
- **Data Preprocessing**: Cleans and tokenizes text, removing stop words.
- **Vectorized Storage**: Uses Sentence Transformers to convert text into vectors and stores them using FAISS indexing.
- **Retrieval-Augmented Generation**: Combines retrieved documents with a large language model to generate answers.
- **User Interaction**: Provides a Gradio-based web interface for user queries and responses.

## Project Structure

```
MEDIQA-CHAIN/
├── .gradio/               # Gradio cache files
├── app/                   # Main application directory
│   ├── app.py             # Gradio interactive interface
│   ├── data/              # Data files
│   │   ├── cleaned_abstracts.txt  # Cleaned abstracts
│   │   └── medical_abstracts.txt  # Original abstracts
│   ├── knowledge_base/    # Knowledge base files
│   │   └── medical_index.faiss  # FAISS index
│   ├── data_preprocess.py # Data preprocessing script
│   ├── download.py        # PubMed abstract download script
│   └── embed_faiss.py     # Text vectorization & FAISS index creation script
├── README.md              # Project documentation
└── requirements.txt       # Dependency list
```

## Quick Start

### 1. Install Dependencies
```bash
conda create -n <your_env_name> python=3.10
pip install -r requirements.txt
```

### 2. Download Medical Abstracts
Run the following script to download medical abstracts from PubMed:
```bash
python app/download.py
```
The abstracts will be saved to `app/data/medical_abstracts.txt`.

### 3. Data Preprocessing
Clean and tokenize the abstracts by running:
```bash
python app/data_preprocess.py
```
The processed abstracts will be saved to `app/data/cleaned_abstracts.txt`.

### 4. Build FAISS Index
Convert the cleaned abstracts into vectors and build the FAISS index:
```bash
python app/embed_faiss.py
```
The index will be saved to `app/knowledge_base/medical_index.faiss`.

### 5. Launch the QA System
Run the following script to start the Gradio interface:
```bash
python app/app.py
```
Open your browser and visit the displayed URL to enter medical queries and receive answers.

## Dependencies
See `requirements.txt` for the full list of required packages.

## License
This project is open-source under the MIT License.

## Acknowledgements
This project utilizes the following open-source tools:
- [FAISS](https://github.com/facebookresearch/faiss): A library for efficient similarity search and clustering of dense vectors.
- [Sentence-Transformers](https://github.com/UKPLab/sentence-transformers): A framework for sentence embeddings using BERT & other transformer-based models.
- [Gradio](https://github.com/gradio-app/gradio): A user-friendly framework for building ML model interfaces.
- [Hugging Face Transformers](https://github.com/huggingface/transformers): A library for NLP models, including LLMs such as Qwen.

## Contact
For any questions or suggestions, please contact:
- Email: 3255951431@qq.com
- GitHub: [Garnett-jpg](https://github.com/Garnett-jpg)