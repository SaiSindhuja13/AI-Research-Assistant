import os
from openai import OpenAI

# ✅ Load OpenAI API key safely (assumes you've set OPENAI_API_KEY in your environment)
openai_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize the OpenAI client
client = OpenAI(api_key=openai_key)

def make_prompt(user_topic):
    topic_prompts = {
        "Summary (high-level overview)": "Summarize this research paper in simple, plain language.",
        "Main conclusions/results": "List the key findings or conclusions reached by the authors.",
        "New findings/contributions": "What new contributions does this work make compared to previous research?",
        "Limitations/weaknesses": "List the study's limitations, flaws, or weaknesses clearly.",
        "Future work/recommendations": "What future research or follow-up work is proposed by the authors?",
        "Methods/techniques used": "Briefly explain the methods, algorithms, or analysis techniques used.",
        "Tools/skills/frameworks mentioned": "What software tools, frameworks, or programming skills were involved? How were they used?",
        "Applications/real-world impact": "How can this research be applied in real-world scenarios? Explain its impact.",
        "Funding sources/conflicts of interest": "Was the study funded? Are there mentions of sponsors or potential conflicts of interest?"
    }

    prompt_text = topic_prompts.get(
        user_topic,
        f"Answer this question about the research paper: {user_topic}"
    )

    return prompt_text + " Please answer in less than 500 words using clear, accessible language."

def query_paper_with_focus(text, user_request):
    prompt = make_prompt(user_request)
    paper_excerpt = text[:8000]  # Truncate to fit within model context

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant skilled at analyzing research papers."},
            {"role": "user", "content": f"{prompt}\n\nPaper Content:\n{paper_excerpt}"}
        ],
        temperature=0.3,
        max_tokens=700
    )

    return response.choices[0].message.content.strip()
