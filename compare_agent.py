from read_pdf import extract_text_from_pdf

def compare_papers(text1, text2):
    # MOCK comparison (for now)
    return (
        "Comparison Summary:\n"
        "- **Topic**: Both papers deal with topological methods in machine learning.\n"
        "- **Methodology**: Paper 1 focuses on unreduced persistence diagrams; Paper 2 emphasizes stability analysis.\n"
        "- **Results**: Paper 1 shows competitive accuracy with lower computation; Paper 2 focuses on robustness.\n"
        "- **Novelty**: Paper 1 introduces a new vectorization approach; Paper 2 adapts existing theories in a novel context."
    )

if __name__ == "__main__":
    # Replace these with your actual file paths
    paper1_path = "/Users/sindhujaupadrashta/Desktop/researchpaper1.pdf"
    paper2_path = "/Users/sindhujaupadrashta/Desktop/researchpaper2.pdf"

    text1 = extract_text_from_pdf(paper1_path)
    text2 = extract_text_from_pdf(paper2_path)

    comparison = compare_papers(text1, text2)
    print("\nCOMPARISON:\n")
    print(comparison)
