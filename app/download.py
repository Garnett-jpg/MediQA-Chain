from Bio import Entrez
import time

def download_abstracts(query, max_results=100, email="your-email@example.com"):
    # Set email (required by PubMed)
    Entrez.email = email

    # Search PubMed
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()

    # Retrieve list of article IDs
    id_list = record["IdList"]
    print(f"Found {len(id_list)} articles.")

    # Download abstracts
    abstracts = []
    for pubmed_id in id_list:
        try:
            # Fetch article details
            handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="abstract", retmode="text")
            abstract = handle.read().strip()
            handle.close()

            if abstract:
                abstracts.append(abstract)
                print(f"Downloaded abstract for PMID: {pubmed_id}")
            else:
                print(f"No abstract found for PMID: {pubmed_id}")

            # Avoid frequent requests (PubMed limits to a maximum of 3 requests per second)
            time.sleep(0.34)
        except Exception as e:
            print(f"Error downloading PMID: {pubmed_id} - {e}")

    return abstracts

def save_abstracts_to_file(abstracts, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for abstract in abstracts:
            f.write(abstract + "\n")
    print(f"Saved {len(abstracts)} abstracts to {file_path}")

if __name__ == "__main__":
    # Search keyword (e.g., "diabetes")
    query = "diabetes"
    # Download abstracts
    abstracts = download_abstracts(query, max_results=100, email="your-email@example.com")
    # Save abstracts to file
    save_abstracts_to_file(abstracts, "data/medical_abstracts.txt")
