import streamlit as st
from pipeline_multi import process_batch_papers, combine_outputs
from rag_utils import chunk_document, create_vector_index, ask_with_rag
from read_pdf import extract_text_from_pdf
st.image("ai_header.jpeg", width=120)
st.title("🧠 Aira - Your AI Research Assistant!")
st.caption("Saves your time by transforming any research papers into answers— summarize, compare, and explore without the reading overload! Powered by OpenAI, LangChain, FAISS, and Streamlit")
# (“ai_header.png” should be a clever AI or research graphic! Use any local or online image)

st.set_page_config(page_title="📚 Multi-Paper LLM Research Assistant", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
    rgba(255,255,255,0.82), 
    rgba(255,255,255,0.82)),
    url("https://images.template.net/wp-content/uploads/2017/06/Research-Papers.jpg");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader("Upload one or more research papers (PDF)", type="pdf", accept_multiple_files=True)

full_task_list = [
    "Summary (high-level overview)",
    "Main conclusions/results",
    "New findings/contributions",
    "Limitations/weaknesses",
    "Future work/recommendations",
    "Methods/techniques used",
    "Tools/skills/frameworks mentioned",
    "Applications/real-world impact",
    "Funding sources/conflicts of interest"
]

selected_tasks = st.multiselect("Select insights you'd like to extract:", full_task_list, default=["Summary (high-level overview)"])
user_question = st.text_input("❓ Or ask a custom question across all uploaded papers:")
show_combined = st.toggle("Show combined insights across all papers")

if uploaded_files and st.button("Run AI Agents"):
    st.info("📄 Extracting text and running agents...")
    paths = []
    all_texts = []

    for i, file in enumerate(uploaded_files):
        path = f"paper_{i+1}.pdf"
        with open(path, "wb") as f:
            f.write(file.read())
        paths.append(path)
        all_texts.append(extract_text_from_pdf(path))

    outputs = process_batch_papers(paths, selected_tasks)

    for title, result in outputs.items():
        st.markdown(f"## 📘 {title}")
        for task in selected_tasks:
            st.markdown(f"**🔹 {task}:**")
            st.write(result.get(task, "No output"))
        st.markdown("---")

    if show_combined:
        for task in selected_tasks:
            combined = combine_outputs(outputs, task)
            st.markdown(f"## 🧾 Combined View – {task}")
            st.write(combined)

    if user_question.strip():
        st.markdown("## 💬 Custom Question Answer")
        all_chunks = []
        for i, txt in enumerate(all_texts):
            title = f"Paper {i+1}"
            for doc in chunk_document(txt):
                doc.metadata["source"] = title
                all_chunks.append(doc)
        vectordb = create_vector_index(all_chunks)
        answer = ask_with_rag(user_question, vectordb)
        st.write(answer)
