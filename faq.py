import pandas as pd 
from pathlib import Path
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

faq_path = Path(__file__).parent / "resources/faq_data.csv"
chroma_client = chromadb.Client()
collection_name_faq = "faqs"
groq_client = Groq()

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name='sentence-transformers/all-MiniLM-L6-V2'
)

def ingest_fag_data(): 
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        print("Ingesting FAQ data into chromadb...")
        collection = chroma_client.get_or_create_collection(
            name=collection_name_faq,
            embedding_function=ef,
        )
        print("Collection created ", collection)
        print("Reading CSV")
        df = pd.read_csv(faq_path)

        docs = df['Question'].to_list()
        metadata = [{'answer': ans } for ans in df['Answer'].to_list()]
        print("Generating ids for ", len(docs))
        ids = [f"id_{i}" for i in range(len(docs))]
        print("Adding faqs into collection")
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
        print(f"FAQ Data successfully ingested into chroma collection : {collection_name_faq}")
    else:
        print(f"Collection {collection_name_faq} already exists!")


def get_relevant_qa(query):
    print("Getting relevant answer")
    collection = chroma_client.get_collection(name=collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results=2,
    )
    return result

def faq_chain(query):
    result = get_relevant_qa(query)
    context = "".join([r.get('answer') for r in result['metadatas'][0]])
    answer = generate_answer(query, context)
    return answer

def generate_answer(query, context):
    prompt = f'''
    Given the following question and answer pairs, provide a concise answer based on the context only.
    If the answer is not found, respond with "I don't know".
    Do not make up any information.

    Question: {query} 

    context: {context}
    '''

    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    ingest_fag_data()
    query = "How to register mobile number?"
    answer = faq_chain(query)
    print(answer)