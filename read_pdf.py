from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

if __name__ == "__main__":
    pdf_path = "/Users/sindhujaupadrashta/Desktop/researchpaper1.pdf"  # Replace with your paper
    text = extract_text_from_pdf(pdf_path)
    print(text[:1000])  # Show only first 1000 characters
