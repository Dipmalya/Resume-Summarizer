from resume_loader import load_and_split_resume
from rag_pipeline import create_vector_store, load_vector_store, create_rag_chain

def build_index(pdf_path):
    print("Loading and splitting resume...")
    chunks = load_and_split_resume(pdf_path)

    print("Creating vector database...")
    create_vector_store(chunks)

    print("Indexing complete!")


def generate_summary(job_description):
    print("Loading vector store...")
    vectordb = load_vector_store()

    print("Creating RAG chain...")
    rag_chain = create_rag_chain(vectordb)

    print("Generating summary...\n")

    response = rag_chain.run(job_description)
    return response


if __name__ == "__main__":
    # Step 1: Build index (run once)
    # build_index("data/sample_resume.pdf")

    # Step 2: Provide Job Description
    job_description = """
    We are looking for a Full Stack Developer with experience in Java, Spring Boot,
    React, and cloud platforms like Azure. Experience in AI/ML and automation is a plus.
    """

    summary = generate_summary(job_description)

    print("===== GENERATED SUMMARY =====\n")
    print(summary)