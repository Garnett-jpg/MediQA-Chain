import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Read data with UTF-8 encoding
with open("data/medical_abstracts.txt", "r", encoding="utf-8") as f:
    abstracts = f.readlines()

# Clean and tokenize the text
cleaned_abstracts = []
for abstract in abstracts:
    doc = nlp(abstract.strip())
    cleaned_abstracts.append(" ".join([token.text for token in doc if not token.is_stop]))

# Save the cleaned data
with open("data/cleaned_abstracts.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(cleaned_abstracts))

# Print the number of cleaned abstracts
print(f"Number of cleaned abstracts: {len(cleaned_abstracts)}")
