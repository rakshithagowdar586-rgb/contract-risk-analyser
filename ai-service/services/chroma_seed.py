import chromadb
from chromadb.config import Settings
import os

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="contract_knowledge"
)

DATA_FOLDER = "data"

def seed_documents():

    docs = []

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".txt"):

            path = os.path.join(DATA_FOLDER, file)

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            docs.append({
                "id": file,
                "content": content
            })

    for doc in docs:
        collection.add(
            documents=[doc["content"]],
            ids=[doc["id"]]
        )

    print(f"{len(docs)} documents seeded into ChromaDB")


if __name__ == "__main__":
    seed_documents()