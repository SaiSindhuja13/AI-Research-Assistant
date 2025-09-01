from read_pdf import extract_text_from_pdf
from summarizer_agent import summarize_text
from critic_agent import critique_paper
from compare_agent import compare_papers

def ask_to_save_output(content, filename="output.txt"):
    save = input("\nWould you like to save the output to a file? (y/n): ")
    if save.lower() == "y":
        with open(filename, "w") as f:
            f.write(content)
        print(f"✅ Output saved to {filename}")


def controller():
    print("\n==== Multi-Agent Research Assistant ====\n")
    print("Options:")
    print("1. Summarize a paper")
    print("2. Critique a paper")
    print("3. Compare two papers")
    
    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        path = input("Enter full path to PDF file: ")
        text = extract_text_from_pdf(path)
        summary = summarize_text(text)
        print("\n📝 SUMMARY:\n")
        print(summary)
        summary = summarize_text(text)
       
        ask_to_save_output(summary, "summary.txt")

    elif choice == "2":
        path = input("Enter full path to PDF file: ")
        text = extract_text_from_pdf(path)
        critique = critique_paper(text)
        print("\n🔍 CRITIQUE:\n")
        print(critique)
        ask_to_save_output(critique, "critique.txt")

    elif choice == "3":
        path1 = input("Enter full path to first PDF: ")
        path2 = input("Enter full path to second PDF: ")
        text1 = extract_text_from_pdf(path1)
        text2 = extract_text_from_pdf(path2)
        comparison = compare_papers(text1, text2)
        print("\n⚖️ COMPARISON:\n")
        print(comparison)
        ask_to_save_output(comparison, "comparison.txt")


    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    controller()
 