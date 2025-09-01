from read_pdf import extract_text_from_pdf
from transformers import pipeline

# Load Hugging Face model (first time takes a minute)
critique_generator = pipeline("text-generation", model="gpt2")

def critique_paper(text):
    prompt = (
        "Critique the following research paper. "
        "List its potential limitations, assumptions, and any gaps in the methodology:\n\n"
        + text[:1500]  # Truncate to avoid overload
    )
    output = critique_generator(prompt, max_length=300, do_sample=True)[0]['generated_text']
    return output

if __name__ == "__main__":
    pdf_path = "/Users/sindhujaupadrashta/Desktop/researchpaper1.pdf"
    text = extract_text_from_pdf(pdf_path)

    critique = critique_paper(text)
    print("\n📉 CRITIQUE:\n")
    print(critique)
