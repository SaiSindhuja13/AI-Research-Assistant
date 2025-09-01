from read_pdf import extract_text_from_pdf
from multi_agents import extract_with_agent

def process_paper_agents(pdf_path: str, tasks: list[str]):
    text = extract_text_from_pdf(pdf_path)
    results = {}
    for task in tasks:
        results[task] = extract_with_agent(text, task)
    return results

def process_batch_papers(pdf_paths: list[str], tasks: list[str]):
    all_outputs = {}
    for i, path in enumerate(pdf_paths):
        paper_name = f"Paper {i+1}"
        all_outputs[paper_name] = process_paper_agents(path, tasks)
    return all_outputs

def combine_outputs(all_outputs: dict, task: str) -> str:
    response = f"🔎 Combined {task} Summaries\n\n"
    for paper, res in all_outputs.items():
        response += f"📘 {paper}:\n{res.get(task, '— No Data —')}\n\n"
    return response.strip()
