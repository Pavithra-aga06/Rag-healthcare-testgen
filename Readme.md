{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1284a0cf-36d4-4b13-a885-2209284e4753",
   "metadata": {},
   "source": [
    "# RAG-based Test Case Generator (Healthcare Domain)\n",
    "\n",
    "## Overview\n",
    "This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline\n",
    "that automatically generates QA test cases from healthcare insurance benefit rules.\n",
    "\n",
    "The system retrieves relevant benefit rules using TF-IDF and cosine similarity,\n",
    "parses them into structured logic, and generates test cases that can be exported\n",
    "to qTest (CSV) and Katalon (Groovy).\n",
    "\n",
    "## Workflow\n",
    "1. Convert healthcare benefit rules into RAG chunks\n",
    "2. Vectorize chunks using TF-IDF\n",
    "3. Retrieve relevant rule using cosine similarity\n",
    "4. Parse rule text into structured fields\n",
    "5. Generate synthetic member and claim scenarios\n",
    "6. Create test cases\n",
    "7. Export to qTest CSV and Katalon Groovy format\n",
    "\n",
    "## Tech Stack\n",
    "- Python\n",
    "- Pandas\n",
    "- scikit-learn (TF-IDF, cosine similarity)\n",
    "- pathlib\n",
    "- Katalon Studio (Groovy test case export)\n",
    "\n",
    "## Sample Output\n",
    "A sample qTest-compatible CSV is provided in the `output/` folder.\n",
    "\n",
    "## Notes\n",
    "- All data used is synthetic (no PII/PHI).\n",
    "- This is a prototype demonstrating RAG + QA automation integration.\n",
    "- TF-IDF is used for retrieval; embeddings can be added as a future improvement.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ba5abc7-ea1a-44f8-b44e-ca215dca97b2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (ml)",
   "language": "python",
   "name": "ml"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
