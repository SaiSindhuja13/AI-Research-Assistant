from read_pdf import extract_text_from_pdf
from extractinfo_agent import query_paper_with_focus
from rag_utils import chunk_document, create_vector_index, ask_with_rag

def extract_requested_info(pdf_path, user_request):
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_document(text)
    vectordb = create_vector_index(chunks)
    return ask_with_rag(user_request, vectordb)
def compare_two_papers_with_rag(text1, text2, user_question):
    chunks1 = chunk_document(text1)
    chunks2 = chunk_document(text2)
    all_chunks = chunks1 + chunks2
    db = create_vector_index(all_chunks)
    return ask_with_rag(user_question, db)

