from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from config import CHROMA_DB_DIR
from prompts import SUMMARY_PROMPT


def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    vectordb.persist()
    return vectordb


def load_vector_store():
    embeddings = OpenAIEmbeddings()
    return Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings
    )


def create_rag_chain(vectordb):
    llm = ChatOpenAI(temperature=0)

    prompt = PromptTemplate(
        template=SUMMARY_PROMPT,
        input_variables=["context", "job_description"]
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain