{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "20394751-2229-4442-89b3-364c22aca164",
   "metadata": {},
   "source": [
    "                                    TestCase scenario using NLP and RAG (healthcare payer domain)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46064210-e309-487f-be82-7920beeba5d0",
   "metadata": {},
   "source": [
    "                                                            Explanation\n",
    "Rule Preparation-\n",
    "I start with predefined raw business rules stored in a file.\n",
    "These rules are chunked into 99 smaller, meaningful rule segments so that retrieval works at rule level instead of document level.\n",
    "\n",
    "Vectorization-\n",
    "Each rule chunk is converted into a TF-IDF vector.\n",
    "This allows textual rules to be represented numerically for similarity comparison.\n",
    "\n",
    "Query Processing-\n",
    "When a user or tester asks a question, the query is also converted into a TF-IDF vector using the same vectorizer.\n",
    "\n",
    "Rule Retrieval-\n",
    "Using cosine similarity, the query vector is compared against all rule chunk vectors.\n",
    "The system retrieves the top-matching rule chunk based on the highest similarity score.\n",
    "\n",
    "Rule Parsing-\n",
    "The retrieved rule text is parsed into a structured format, extracting:\n",
    "Conditions\n",
    "Coverage logic\n",
    "Constraints\n",
    "This converts unstructured rule text into machine-understandable JSON.\n",
    "\n",
    "Test Case Generation-\n",
    "Based on the structured rule JSON, the system automatically generates:\n",
    "Preconditions\n",
    "Test steps\n",
    "Expected results\n",
    "This removes manual test-case writing.\n",
    "\n",
    "Tool Integration-\n",
    "The generated test cases are exported and integrated with qTest and Katalon, enabling:\n",
    "Test management\n",
    "Automation execution"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "12f2a6a4-d602-4422-a352-bfe1c5892cd4",
   "metadata": {},
   "source": [
    "┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐\n",
    "│  Raw Benefits   │    │   99 TF-IDF      │    │  QTest/Katlon   │\n",
    "│  File (Excel)   │───▶│  Chunks (Vector  │───▶│  Test Execution │\n",
    "└─────────────────┘    │  Store)          │    └─────────────────┘\n",
    "                        └──────────────────┘\n",
    "                              │\n",
    "                       ┌──────────────┐\n",
    "                       │  USER QUERY  │\n",
    "                       │\"Platinum PCP\"│\n",
    "                       └──────────────┘\n",
    "                              │\n",
    "                        ┌──────────────┐\n",
    "                        │ COSINE MATCH │──┐\n",
    "                        │   0.69 score │  │\n",
    "                        └──────────────┘  │\n",
    "                              │          │\n",
    "                        ┌──────────────┐  │\n",
    "                        │  PARSE RULE  │  │\n",
    "                        │ → JSON       │  │\n",
    "                        └──────────────┘  │\n",
    "                              │          │\n",
    "                        ┌──────────────┐  │\n",
    "                        │ TEST CASE    │◄─┘\n",
    "                        │ JSON → QTest │\n",
    "                        └──────────────┘\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "47d4ba23-1edd-4433-9b4e-f54efd6401fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>plan_name</th>\n",
       "      <th>metal_level</th>\n",
       "      <th>deductible_individual</th>\n",
       "      <th>deductible_family</th>\n",
       "      <th>oop_max_individual</th>\n",
       "      <th>oop_max_family</th>\n",
       "      <th>hsa_compatible</th>\n",
       "      <th>primary_care_copay</th>\n",
       "      <th>specialist_copay</th>\n",
       "      <th>urgent_care_copay</th>\n",
       "      <th>er_copay</th>\n",
       "      <th>mental_health_copay</th>\n",
       "      <th>rx_tier1_copay</th>\n",
       "      <th>rx_tier2_copay</th>\n",
       "      <th>rx_tier3_copay</th>\n",
       "      <th>rx_tier4_copay</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Platinum Classic</td>\n",
       "      <td>Platinum</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2000</td>\n",
       "      <td>4000</td>\n",
       "      <td>No</td>\n",
       "      <td>15</td>\n",
       "      <td>35</td>\n",
       "      <td>55</td>\n",
       "      <td>100</td>\n",
       "      <td>15</td>\n",
       "      <td>10</td>\n",
       "      <td>30</td>\n",
       "      <td>60</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Gold Classic</td>\n",
       "      <td>Gold</td>\n",
       "      <td>775</td>\n",
       "      <td>1550</td>\n",
       "      <td>10150</td>\n",
       "      <td>20300</td>\n",
       "      <td>No</td>\n",
       "      <td>25</td>\n",
       "      <td>40</td>\n",
       "      <td>60</td>\n",
       "      <td>150</td>\n",
       "      <td>25</td>\n",
       "      <td>10</td>\n",
       "      <td>35</td>\n",
       "      <td>70</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Gold Simple</td>\n",
       "      <td>Gold</td>\n",
       "      <td>1500</td>\n",
       "      <td>3000</td>\n",
       "      <td>7200</td>\n",
       "      <td>14400</td>\n",
       "      <td>No</td>\n",
       "      <td>30</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Silver Classic</td>\n",
       "      <td>Silver</td>\n",
       "      <td>2450</td>\n",
       "      <td>4900</td>\n",
       "      <td>10150</td>\n",
       "      <td>20300</td>\n",
       "      <td>No</td>\n",
       "      <td>30</td>\n",
       "      <td>65</td>\n",
       "      <td>70</td>\n",
       "      <td>500</td>\n",
       "      <td>30</td>\n",
       "      <td>15</td>\n",
       "      <td>40</td>\n",
       "      <td>75</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Silver Simple PCP Saver</td>\n",
       "      <td>Silver</td>\n",
       "      <td>7300</td>\n",
       "      <td>14600</td>\n",
       "      <td>10100</td>\n",
       "      <td>20200</td>\n",
       "      <td>No</td>\n",
       "      <td>15</td>\n",
       "      <td>40</td>\n",
       "      <td>75</td>\n",
       "      <td>50</td>\n",
       "      <td>15</td>\n",
       "      <td>20</td>\n",
       "      <td>50</td>\n",
       "      <td>50</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 plan_name metal_level  deductible_individual  \\\n",
       "0         Platinum Classic    Platinum                      0   \n",
       "1             Gold Classic        Gold                    775   \n",
       "2              Gold Simple        Gold                   1500   \n",
       "3           Silver Classic      Silver                   2450   \n",
       "4  Silver Simple PCP Saver      Silver                   7300   \n",
       "\n",
       "   deductible_family  oop_max_individual  oop_max_family hsa_compatible  \\\n",
       "0                  0                2000            4000             No   \n",
       "1               1550               10150           20300             No   \n",
       "2               3000                7200           14400             No   \n",
       "3               4900               10150           20300             No   \n",
       "4              14600               10100           20200             No   \n",
       "\n",
       "   primary_care_copay  specialist_copay  urgent_care_copay  er_copay  \\\n",
       "0                  15                35                 55       100   \n",
       "1                  25                40                 60       150   \n",
       "2                  30                20                 20        20   \n",
       "3                  30                65                 70       500   \n",
       "4                  15                40                 75        50   \n",
       "\n",
       "   mental_health_copay  rx_tier1_copay  rx_tier2_copay  rx_tier3_copay  \\\n",
       "0                   15              10              30              60   \n",
       "1                   25              10              35              70   \n",
       "2                   20              20              20              20   \n",
       "3                   30              15              40              75   \n",
       "4                   15              20              50              50   \n",
       "\n",
       "   rx_tier4_copay  \n",
       "0              60  \n",
       "1              70  \n",
       "2              20  \n",
       "3              75  \n",
       "4              50  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from pathlib import Path\n",
    "import os\n",
    "import pandas as pd\n",
    "\n",
    "# Step 1: ensure correct working directory\n",
    "os.chdir(r\"C:\\Users\\shine\")\n",
    "\n",
    "# Step 2: build path safely\n",
    "DATA_DIR = Path(\"data\")\n",
    "BENEFITS_PATH = DATA_DIR / \"synthetic_company_plan_benefits.csv\"\n",
    "\n",
    "# Step 3: validate\n",
    "assert BENEFITS_PATH.exists(), \"Data file not found\"\n",
    "\n",
    "# Step 4: load\n",
    "df = pd.read_csv(BENEFITS_PATH)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "19a95593-22e6-42a8-8789-e309207dd129",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['plan_name', 'metal_level', 'deductible_individual', 'deductible_family', 'oop_max_individual', 'oop_max_family', 'hsa_compatible', 'primary_care_copay', 'specialist_copay', 'urgent_care_copay', 'er_copay', 'mental_health_copay', 'rx_tier1_copay', 'rx_tier2_copay', 'rx_tier3_copay', 'rx_tier4_copay']\n"
     ]
    }
   ],
   "source": [
    "print(df.columns.tolist())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "74eef869-c59b-4cf6-ace0-fc16f1b6fce8",
   "metadata": {},
   "outputs": [],
   "source": [
    "service_map = {\n",
    "    \"Primary Care Visit\": \"primary_care_copay\",\n",
    "    \"Specialist Visit\": \"specialist_copay\",\n",
    "    \"Urgent Care\": \"urgent_care_copay\",\n",
    "    \"Emergency Room\": \"er_copay\",\n",
    "    \"Mental Health Visit\": \"mental_health_copay\",\n",
    "    \"RX Tier 1\": \"rx_tier1_copay\",\n",
    "    \"RX Tier 2\": \"rx_tier2_copay\",\n",
    "    \"RX Tier 3\": \"rx_tier3_copay\",\n",
    "    \"RX Tier 4\": \"rx_tier4_copay\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "db0021cc-9e51-4e63-9801-a1e95a6aaeee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "99"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rag_chunks = []\n",
    "\n",
    "for _, row in df.iterrows():\n",
    "    for service_name, col_name in service_map.items():\n",
    "        cost_share = row[col_name]\n",
    "\n",
    "        chunk_text = (\n",
    "            f\"Plan: {row['plan_name']}\\n\"\n",
    "            f\"Metal Level: {row['metal_level']}\\n\"\n",
    "            f\"Service: {service_name}\\n\"\n",
    "            f\"Cost Share: {cost_share}\\n\"\n",
    "            f\"Individual Deductible: {row['deductible_individual']}\\n\"\n",
    "            f\"Family Deductible: {row['deductible_family']}\\n\"\n",
    "            f\"OOP Max (Individual): {row['oop_max_individual']}\\n\"\n",
    "            f\"OOP Max (Family): {row['oop_max_family']}\\n\"\n",
    "            f\"HSA Compatible: {row['hsa_compatible']}\"\n",
    "        )\n",
    "\n",
    "        metadata = {\n",
    "            \"plan\": row[\"plan_name\"],\n",
    "            \"metal\": row[\"metal_level\"],\n",
    "            \"service\": service_name,\n",
    "            \"year\": \"2026\",\n",
    "            \"source\": \"Synthetic Benefits CSV\"\n",
    "        }\n",
    "\n",
    "        rag_chunks.append({\n",
    "            \"text\": chunk_text,\n",
    "            \"metadata\": metadata\n",
    "        })\n",
    "\n",
    "len(rag_chunks)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1716b0ce-741b-40d3-b7c1-15be7b31fb0c",
   "metadata": {},
   "source": [
    "This code creates normalized RAG chunks with metadata from structured CSV data. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fe386626-4e13-4c79-85f3-ababd2473953",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'text': 'Plan: Platinum Classic\\nMetal Level: Platinum\\nService: Primary Care Visit\\nCost Share: 15\\nIndividual Deductible: 0\\nFamily Deductible: 0\\nOOP Max (Individual): 2000\\nOOP Max (Family): 4000\\nHSA Compatible: No',\n",
       " 'metadata': {'plan': 'Platinum Classic',\n",
       "  'metal': 'Platinum',\n",
       "  'service': 'Primary Care Visit',\n",
       "  'year': '2026',\n",
       "  'source': 'Synthetic Benefits CSV'}}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rag_chunks[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e040e769-979d-4407-9e4a-ec0a5069ee6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(99, 90)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "\n",
    "# Build corpus\n",
    "rag_texts = [c[\"text\"] for c in rag_chunks]\n",
    "\n",
    "vectorizer = TfidfVectorizer(stop_words=\"english\")\n",
    "X = vectorizer.fit_transform(rag_texts)\n",
    "\n",
    "X.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42341934-0958-4801-b90f-c6567a50b933",
   "metadata": {},
   "source": [
    "99 healthcare rule chunks were vectorized into a 90-dimensional feature space."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ca75dc4c-91b5-4713-8310-bd6f089b5e47",
   "metadata": {},
   "outputs": [],
   "source": [
    "def retrieve_benefit_rule(query, top_k=1):\n",
    "    query_vec = vectorizer.transform([query])\n",
    "    scores = cosine_similarity(query_vec, X)[0]\n",
    "\n",
    "    top_idx = scores.argsort()[-top_k:][::-1]\n",
    "\n",
    "    results = []\n",
    "    for idx in top_idx:\n",
    "        results.append({\n",
    "            \"score\": scores[idx],\n",
    "            \"text\": rag_chunks[idx][\"text\"],\n",
    "            \"metadata\": rag_chunks[idx][\"metadata\"]\n",
    "        })\n",
    "    return results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0b4524e2-b546-4404-81ed-23bfcf0d8de9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'score': np.float64(0.6884786293766466),\n",
       " 'text': 'Plan: Platinum Classic\\nMetal Level: Platinum\\nService: Primary Care Visit\\nCost Share: 15\\nIndividual Deductible: 0\\nFamily Deductible: 0\\nOOP Max (Individual): 2000\\nOOP Max (Family): 4000\\nHSA Compatible: No',\n",
       " 'metadata': {'plan': 'Platinum Classic',\n",
       "  'metal': 'Platinum',\n",
       "  'service': 'Primary Care Visit',\n",
       "  'year': '2026',\n",
       "  'source': 'Synthetic Benefits CSV'}}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "query = \"Platinum Classic primary care visit cost\"\n",
    "result = retrieve_benefit_rule(query)[0]\n",
    "\n",
    "result\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a5a9c0a-e713-4c0c-aa96-40f13b643541",
   "metadata": {},
   "source": [
    "This step retrieves the most relevant insurance rule chunk from the RAG corpus using TF-IDF and cosine similarity based on the user query."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5bdcf009-b64f-43e2-b3c9-35f252d538a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "synthetic_member = {\n",
    "    \"member_id\": \"SYN-001\",\n",
    "    \"age\": 35,\n",
    "    \"state\": \"NY\",\n",
    "    \"plan\": \"Platinum Classic\"\n",
    "}\n",
    "\n",
    "synthetic_claim = {\n",
    "    \"claim_id\": \"CLM-1001\",\n",
    "    \"service\": \"Primary Care Visit\",\n",
    "    \"billed_amount\": 150,\n",
    "    \"provider_network\": \"INN\"\n",
    "}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba34efd4-ebe7-483d-bf4a-d0cce6896262",
   "metadata": {},
   "source": [
    "I use synthetic member and claim objects to simulate real-world insurance scenarios and validate retrieved benefit rules before generating automated test cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "1216ef9f-331e-4978-a536-f7b794075992",
   "metadata": {},
   "outputs": [],
   "source": [
    "def parse_rag_rule(rag_text):\n",
    "    rule = {}\n",
    "    for line in rag_text.split(\"\\n\"):\n",
    "        if line.startswith(\"Cost Share:\"):\n",
    "            rule[\"cost_share\"] = int(\n",
    "                line.replace(\"Cost Share:\", \"\").strip()\n",
    "            )\n",
    "        if line.startswith(\"Individual Deductible:\"):\n",
    "            rule[\"deductible_individual\"] = int(\n",
    "                line.replace(\"Individual Deductible:\", \"\").strip()\n",
    "            )\n",
    "        if line.startswith(\"HSA Compatible:\"):\n",
    "            rule[\"hsa\"] = (\n",
    "                line.replace(\"HSA Compatible:\", \"\").strip().lower() == \"yes\"\n",
    "            )\n",
    "    return rule\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dba938be-bfec-439e-a556-0fc02c57ff7e",
   "metadata": {},
   "source": [
    "I parse the retrieved RAG rule text into a normalized, typed structure so downstream decision logic and automated test cases can be generated reliably."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f2027b38-8e44-4e65-8e18-642c601cfbeb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'cost_share': 15, 'deductible_individual': 0, 'hsa': False}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "retrieved = retrieve_benefit_rule(\n",
    "    \"Platinum Classic primary care visit cost\"\n",
    ")[0]\n",
    "\n",
    "parsed_rule = parse_rag_rule(retrieved[\"text\"])\n",
    "parsed_rule"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "47f4061d-61ae-4392-a199-9d1d58c4bdcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Test Case Name': 'NY_2026_Platinum_PCP_CostShare',\n",
       " 'Requirement': 'Benefit Cost Sharing Validation',\n",
       " 'Precondition': 'Synthetic member (SYN-001) enrolled in Platinum Classic plan',\n",
       " 'Step 1': 'Submit an in-network Primary Care Visit claim with billed amount $150',\n",
       " 'Expected Result': 'Apply cost share of 15 with individual deductible 0',\n",
       " 'Tags': 'NY,2026,Platinum,Synthetic,RAG'}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_case = {\n",
    "    \"Test Case Name\": \"NY_2026_Platinum_PCP_CostShare\",\n",
    "    \"Requirement\": \"Benefit Cost Sharing Validation\",\n",
    "    \"Precondition\": (\n",
    "        f\"Synthetic member ({synthetic_member['member_id']}) enrolled in \"\n",
    "        f\"{synthetic_member['plan']} plan\"\n",
    "    ),\n",
    "    \"Step 1\": (\n",
    "        f\"Submit an in-network {synthetic_claim['service']} claim \"\n",
    "        f\"with billed amount ${synthetic_claim['billed_amount']}\"\n",
    "    ),\n",
    "    \"Expected Result\": (\n",
    "        f\"Apply cost share of {parsed_rule['cost_share']} with \"\n",
    "        f\"individual deductible {parsed_rule['deductible_individual']}\"\n",
    "    ),\n",
    "    \"Tags\": \"NY,2026,Platinum,Synthetic,RAG\"\n",
    "}\n",
    "\n",
    "test_case\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3914397-97c7-4bd6-9b60-fe657c1c9e3f",
   "metadata": {},
   "source": [
    "After retrieving and parsing the benefit rule, I combine synthetic member and claim data to generate a structured, tool-ready test case that can be exported directly to qTest or Katalon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "05f243a9-a1b9-4972-a5a0-2e5728026976",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "WindowsPath('output/qtest_testcases.csv')"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "\n",
    "df_qtest = pd.DataFrame([test_case])\n",
    "\n",
    "OUT_DIR = Path(\"output\")\n",
    "OUT_DIR.mkdir(exist_ok=True)\n",
    "\n",
    "csv_path = OUT_DIR / \"qtest_testcases.csv\"\n",
    "df_qtest.to_csv(csv_path, index=False)\n",
    "\n",
    "csv_path\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "dd3345ad-2793-4c4d-bfb5-9bb6373343ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "WindowsPath('C:/Users/shine/output/qtest_testcases.csv')"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from pathlib import Path\n",
    "\n",
    "try:\n",
    "    PROJECT_ROOT = Path(__file__).resolve().parent\n",
    "except NameError:\n",
    "    PROJECT_ROOT = Path.cwd()\n",
    "\n",
    "OUTPUT_DIR = PROJECT_ROOT / \"output\"\n",
    "OUTPUT_DIR.mkdir(exist_ok=True)\n",
    "\n",
    "csv_path = OUTPUT_DIR / \"qtest_testcases.csv\"\n",
    "csv_path\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "45e2c5b9-f862-42ff-97df-8e89418f3adb",
   "metadata": {},
   "outputs": [],
   "source": [
    "KATALON_TEMPLATE = \"\"\"\n",
    "import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI\n",
    "\n",
    "WebUI.comment(\"{test_id}\")\n",
    "WebUI.comment(\"{description}\")\n",
    "WebUI.comment(\"Expected: {expected}\")\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "75a62246-4f65-42c9-aa66-61fae455cb54",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pathlib import Path\n",
    "\n",
    "def generate_katalon_test(test_case, katalon_testcase_path):\n",
    "    content = KATALON_TEMPLATE.format(\n",
    "        test_id=test_case[\"test_id\"],\n",
    "        description=test_case[\"description\"],\n",
    "        expected=test_case[\"expected\"].replace(\"$\", \"\\\\$\")\n",
    "    )\n",
    "\n",
    "    file_path = Path(katalon_testcase_path) / f\"{test_case['test_id']}.groovy\"\n",
    "    file_path.write_text(content, encoding=\"utf-8\")\n",
    "\n",
    "    return file_path\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ed4d9e8-547c-4c7e-a495-a93fb47a8ec0",
   "metadata": {},
   "source": [
    "A Groovy test case template is a reusable script skeleton with placeholders, and test automation scaffolding refers to the supporting structure that allows these templates to be programmatically filled and generated as executable test cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "48c33e7e-75c7-4f17-ad93-1384b03effcd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "WindowsPath('katalon/Test Cases/TC_Platinum_PCP.groovy')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_case = {\n",
    "    \"test_id\": \"TC_Platinum_PCP\",\n",
    "    \"description\": \"Validate Platinum Classic – Primary Care Visit cost sharing\",\n",
    "    \"expected\": \"$15 copay, no deductible applies\"\n",
    "}\n",
    "\n",
    "KATALON_OUT = Path(\"katalon/Test Cases\")\n",
    "KATALON_OUT.mkdir(parents=True, exist_ok=True)\n",
    "\n",
    "generate_katalon_test(test_case, KATALON_OUT)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ff5ecb9a-f0a2-4ea6-bf9e-23107547c8d7",
   "metadata": {},
   "source": [
    "Currently the system generates one test case because it processes a single query with top-1 retrieval. Expanding the query set or increasing top-k allows automatic generation of multiple test cases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "059038fe-f196-4547-8347-7c519e133469",
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
