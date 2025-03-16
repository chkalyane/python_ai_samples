import spacy
from transformers import pipeline
from PyPDF2 import PdfReader
from fpdf import FPDF

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() or "" #Handle cases where no text is extracted.
            return text
    except FileNotFoundError:
        return "Error: PDF file not found."
    except Exception as e:
        return f"An error occurred: {e}"

def generate_answer(question, context):
    """Generates an answer using a question-answering model."""
    qa_pipeline = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad",revision="564e9b5")
    result = qa_pipeline(question=question, context=context)
    return result['answer'] if result else "Answer not found."

def create_pdf_report(question, answer, output_path="answer_report.pdf"):
    """Creates a PDF report with the question and answer."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Question:", ln=True)
    pdf.multi_cell(190, 10, txt=question)
    pdf.cell(200, 10, txt="Answer:", ln=True)
    pdf.multi_cell(190, 10, txt=answer)
    output_path = r"C:\Users\chkal\Downloads\answer_report.pdf"
    pdf.output(output_path)
    print(f"Report saved to {output_path}")

def process_pdf_question(pdf_path, question, output_report=True):
    """Processes a PDF and answers a question."""
    pdf_text = extract_text_from_pdf(pdf_path)
    if pdf_text.startswith("Error:"):
        return pdf_text #Return the error message if there was an error.

    answer = generate_answer(question, pdf_text)

    if output_report:
        create_pdf_report(question, answer)
    return answer

# Example usage:
path = r"C:\Users\chkal\Downloads\PDF1.pdf"
pdf_file = path
user_question = "What is the main topic of the document?"

result = process_pdf_question(pdf_file, user_question)
print("question:", "What is the main topic of the document?")
print("Answer:", result)

#Example with no pdf report.
result2 = process_pdf_question(pdf_file, "Briefly describe Becky's Adventure Day.", output_report=False)
print("question:", "Briefly describe Becky's Adventure Day.")
print("Answer:", result2)