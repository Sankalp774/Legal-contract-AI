# Simple Legal Contract Analyzer
# Analyzes contracts, extracts key clauses, and provides summaries

# Install required libraries
!pip install transformers python-docx PyMuPDF nltk

# Import libraries
from google.colab import files
import fitz  # PyMuPDF
import docx
import os
import re
import nltk
from transformers import pipeline

# Download NLTK data
nltk.download('punkt')

# Extract text from documents
def extract_text(filename):
    """Extract text from PDF or DOCX files"""
    if filename.endswith(".pdf"):
        with fitz.open(filename) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    elif filename.endswith(".docx"):
        doc = docx.Document(filename)
        return "\n".join([para.text for para in doc.paragraphs])
    return None

# Extract sections from contract
def extract_contract_sections(text):
    """Extract different sections from the contract"""
    section_patterns = [
        r'(?i)(?:ARTICLE|Section)\s+\d+[\.\:]?\s*([^\n]+)',
        r'(?i)^([A-Z][A-Z\s]+)(?:\.|:)'
    ]

    sections = {}
    current_section = "Preamble"
    sections[current_section] = []

    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue

        new_section_found = False
        for pattern in section_patterns:
            matches = re.findall(pattern, line)
            if matches:
                current_section = matches[0].strip()
                if current_section not in sections:
                    sections[current_section] = []
                new_section_found = True
                break

        if not new_section_found:
            sections[current_section].append(line)

    for section in sections:
        sections[section] = '\n'.join(sections[section])

    return sections

# Identify key legal terms
def identify_legal_terms(text):
    """Identify important legal terms"""
    legal_terms = [
        "indemnification", "liability", "termination", "confidentiality",
        "intellectual property", "warranty", "force majeure", "governing law"
    ]

    term_contexts = {}
    for term in legal_terms:
        pattern = re.compile(f"([^.]*?{term}[^.]*\.)", re.IGNORECASE)
        matches = pattern.findall(text)
        if matches:
            term_contexts[term] = matches[:2]  # Limit to 2 matches per term

    return term_contexts

# Main function to analyze contract
def analyze_contract(filename):
    """Analyze the uploaded contract"""
    print(f"⏳ Analyzing {filename}...")

    # Extract text
    contract_text = extract_text(filename)
    if not contract_text:
        print("❌ Failed to extract text from document.")
        return

    # Initialize summarizer (single model for simplicity)
    print("Loading summarization model...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Generate contract summary
    print("\n🔍 Generating summary...")
    chunks = [contract_text[i:i+1000] for i in range(0, len(contract_text), 1000)]
    summary = ""
    for chunk in chunks[:3]:  # Process only first 3 chunks for speed
        if len(chunk) > 100:
            res = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
            summary += res[0]['summary_text'] + " "

    # Extract sections
    print("\n🔍 Extracting sections...")
    sections = extract_contract_sections(contract_text)

    # Identify legal terms
    print("\n🔍 Identifying key terms...")
    legal_terms = identify_legal_terms(contract_text)

    # Print results
    print("\n📄 CONTRACT SUMMARY:")
    print(summary)

    print("\n📑 CONTRACT SECTIONS:")
    for section_name, content in list(sections.items())[:5]:  # Show only first 5 sections
        print(f"\n• {section_name}")
        if len(content) > 150:
            print(f"  {content[:150]}...")
        else:
            print(f"  {content}")

    print("\n⚖️ KEY LEGAL TERMS:")
    for term, contexts in legal_terms.items():
        print(f"\n• {term.upper()}:")
        for i, context in enumerate(contexts):
            print(f"  {i+1}. {context[:100]}...")

# Interactive contract analyzer
def analyze_legal_contract():
    """Main function for the contract analyzer"""
    print("📝 Simple Legal Contract Analyzer 📝")
    print("Upload your legal contract file (PDF or DOCX):")

    uploaded = files.upload()

    if not uploaded:
        print("No file uploaded. Please run the cell again and upload a file.")
        return

    filename = list(uploaded.keys())[0]
    analyze_contract(filename)

# Run the analyzer
analyze_legal_contract()
