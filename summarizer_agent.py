from transformers import pipeline
from read_pdf import extract_text_from_pdf

def make_prompt(user_topic):
    topic_prompts = {
        "Summary (high-level overview)": "Summarize this research paper in simple, plain language, in less than 500 words.",
        "Main conclusions/results": "List the key findings or conclusions reached by the authors,  in less than 500 words.",
        "New findings/contributions": "What new contributions does this work make compared to previous research?  in less than 500 words.",
        "Limitations/weaknesses": "List the study's limitations, flaws, or weaknesses clearly -  in less than 500 words.",
        "Future work/recommendations": "What future research or follow-up work is proposed by the authors?-  in less than 500 words.",
        "Methods/techniques used": "Briefly explain the methods, algorithms, or analysis techniques used -  in less than 500 words.",
        "Tools/skills/frameworks mentioned": "What software tools, frameworks, or programming skills were involved? Mention how they were used -  in less than 500 words.",
        "Applications/real-world impact": "How can this research be applied in real-world scenarios? Explain its impact - in less than 500 words.",
        "Funding sources/conflicts of interest": "Was the study funded? Are there mentions of sponsors or potential conflicts of interest? -  in less than 500 words."
    }

    return topic_prompts.get(user_topic, f"Answer this question about the paper: {user_topic}")

# Load the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    # Hugging Face models have input size limits (~1024 tokens)
    trimmed_text = text[:1024]  # Trim to avoid input overflow

    # Generate summary
    summary = summarizer(trimmed_text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    # Example usage with a real PDF
    pdf_path = "/Users/sindhujaupadrashta/Desktop/researchpaper1.pdf"
    full_text = extract_text_from_pdf(pdf_path)
    
    summary = summarize_text(full_text)
    print("\nSUMMARY:\n")
    print(summary)
