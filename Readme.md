# RAG-based Healthcare Test Case Generator

## Overview
This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline
that automatically generates QA test cases from healthcare insurance benefit rules.

The system retrieves relevant benefit rules using TF-IDF and cosine similarity,
parses them into structured logic, and generates test cases that can be exported
to qTest (CSV) and Katalon (Groovy).

---

## Workflow
1. Convert healthcare benefit rules into RAG chunks  
2. Vectorize chunks using TF-IDF  
3. Retrieve relevant rules using cosine similarity  
4. Parse rule text into structured fields  
5. Generate synthetic member and claim scenarios  
6. Create test cases  
7. Export test cases to qTest CSV and Katalon Groovy format  

---

## Tech Stack
- Python  
- Pandas  
- scikit-learn (TF-IDF, cosine similarity)  
- pathlib  
- Jupyter Notebook  

---

## Sample Output
A sample qTest-compatible CSV is generated in the `output/` folder.

---

## Notes
- All data used is synthetic (no PII / PHI)
- This is a prototype demonstrating **RAG + QA automation**
- TF-IDF is used for retrieval; embeddings can be added as a future improvement

## Repository Structure
- `Rag-healthcare-testgen.ipynb` – Exploratory notebook and prototyping
- `Rag-healthcare-testgen.py` – Production-ready Python script

