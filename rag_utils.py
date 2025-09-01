import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema.document import Document
from langchain_community.vectorstores import FAISS

# ✅ Global LLM + Embedding clients
embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3, api_key=os.getenv("OPENAI_API_KEY"))

# 🚀 1. Create chunks from raw string
def chunk_document(text, chunk_size=1000, overlap=150):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    docs = splitter.create_documents([text])  # Returns list of Document objects
    return docs

# 📦 2. Embed and store chunks in a vector index (FAISS in memory for now)
def create_vector_index(chunks):
    db = FAISS.from_documents(chunks, embeddings)
    return db

# 📄 3. Query with retrieval + generation
def ask_with_rag(query, vector_index, top_k=4):
    relevant_docs = vector_index.similarity_search(query, k=top_k)
    context = "\n\n".join(doc.page_content for doc in relevant_docs)

    prompt = f"""
You are a helpful AI assistant. Use ONLY the following research paper passages to answer the user question.
If the answer is not in the context, say so directly.

Context:
{context}

Question: {query}
Answer:
    """.strip()

    answer = llm.invoke(prompt)
    return answer.content.strip()
