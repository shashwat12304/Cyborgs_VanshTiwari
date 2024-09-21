import chromadb
from langchain_ollama import ChatOllama
class RAG:
    def __init__(self):
        self.client = chromadb.HttpClient(host='localhost', port=8000)
        self.collection = ''

    def getcollection(self, collection_name):
        self.collection = self.client.get_or_create_collection(name=collection_name)
        return self

    def add(self, data):
        self.collection.add(
            documents=data,
            metadatas=[{"source": "info"}],
            ids=["id1"]
        )

    def get_contexts(self, query):
        results = self.collection.query(
            query_texts=[query],
            n_results=5
        )
        return results['documents']
    
    def llm(self,query,contexts):
        llm = ChatOllama(
            model="llava:13b",
            temperature=0
        )
        messages = [
            (
                "system",
                f'''
                You are a helpful Generator in Retrieval Augmented Generation that answers the question on the basis of given contexts{contexts}
                ''',
            ),
            ("human", f"Please answer the query {query}"),
        ]
        ai_msg = llm.invoke(messages)
        return ai_msg.content

if __name__ == "__main__":
    rag = RAG().getcollection("Students")
    query = input("Please enter the query")
    contexts = rag.get_contexts(query)
    answer = rag.llm(query,contexts)
    print(answer)
