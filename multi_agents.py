from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TASK_PROMPTS = {
    "Summary (high-level overview)": "Summarize the overall purpose, scope, and motivation behind this research paper in simple and accessible language.",
    "Main conclusions/results": "List the key results or takeaways that the authors present in the paper. Make it clear and concise.",
    "New findings/contributions": "Explain what new knowledge, techniques, or theoretical contributions this paper introduces.",
    "Limitations/weaknesses": "Identify the main limitations, risks, or weaknesses acknowledged by the authors, or evident from the content.",
    "Future work/recommendations": "What future directions, improvements, or extensions do the authors suggest or imply for this research?",
    "Methods/techniques used": "Describe the main methods, experiments, models, or analysis techniques used in the study.",
    "Tools/skills/frameworks mentioned": "List notable software, frameworks, programming tools, or libraries mentioned, and explain how they were used.",
    "Applications/real-world impact": "Provide possible applications or real-world implications of the work. Where or how could this research be applied?",
    "Funding sources/conflicts of interest": "Extract any funding acknowledgments, sponsorships, or potential conflicts of interest stated by the authors."
}

def extract_with_agent(text: str, task: str) -> str:
    prompt = TASK_PROMPTS.get(
        task,
        f"Answer this question about the paper: {task}"
    ) + "\n\nPaper Content:\n" + text[:8000]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a research assistant that extracts specific insights from academic papers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=700
    )
    return response.choices[0].message.content.strip()
