# Legal Contract Analyzer by AI
A smart legal document analysis tool that simplifies and streamlines the process of understanding legal contracts. This project uses NLP techniques to summarize, extract key clauses, generate questions, and evaluate answers, making it ideal for law students, professionals, and anyone dealing with complex legal texts.



##Features


✅ Contract Summarization – Automatically generate concise summaries of long legal documents.

🧠 Clause Extraction – Identify important clauses like termination, confidentiality, indemnity, etc.

❓ Question Generation – Generate MCQs, one-word answers, and long-form questions from legal documents.

📝 Answer Evaluation – Score user-provided answers using semantic similarity (BERTScore).

✍️ Auto-Correction – Provide improved versions of user answers using a text generation model.

🖼️ User Interface – Clean and minimal interface built using Gradio.

💡 Use Case


This tool is built to assist:

Law students for exam preparation.

Legal professionals in quick contract review.

Developers building legaltech solutions.

Educators creating assessment content from legal texts.

🧰 Tech Stack


Python

Gradio – For the UI

Transformers (Hugging Face) – Summarization & text generation

BERTScore – Answer evaluation

PyMuPDF / PDFplumber – PDF parsing

Scikit-learn / SpaCy / NLTK – NLP utilities

PyMuPDF (fitz) – For parsing and extracting text from PDFs

NLTK – For text preprocessing (tokenization, stopwords)

Scikit-learn – For keyword extraction (TF-IDF based)

Sentence Transformers – (If you used it) for semantic similarity 

Torch – Backend for BERTScore and Transformer models

TQDM – For progress bars 


🤝 Contribution

Pull requests are welcome! If you'd like to add features or fix bugs, feel free to fork the repo and submit a PR.

📜 License

This project is open source under the MIT License.
