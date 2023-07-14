import PyPDF2
import docx
import csv

def split_pdf(input_file, output_prefix):
    pdf = PyPDF2.PdfFileReader(input_file)
    for page_num in range(pdf.numPages):
        output_file = f"{output_prefix}_{page_num + 1}.pdf"
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(pdf.getPage(page_num))
        with open(output_file, 'wb') as f:
            writer.write(f)
        print(f"Split PDF page {page_num + 1} saved as {output_file}")

def merge_pdfs(input_files, output_file):
    writer = PyPDF2.PdfFileWriter()
    for input_file in input_files:
        pdf = PyPDF2.PdfFileReader(input_file)
        for page_num in range(pdf.numPages):
            writer.addPage(pdf.getPage(page_num))
    with open(output_file, 'wb') as f:
        writer.write(f)
    print(f"Merged PDFs saved as {output_file}")

def convert_pdf_to_docx(input_file, output_file):
    pdf = PyPDF2.PdfFileReader(input_file)
    doc = docx.Document()
    for page_num in range(pdf.numPages):
        page = pdf.getPage(page_num)
        text = page.extract_text()
        doc.add_paragraph(text)
    doc.save(output_file)
    print(f"Converted PDF to DOCX. Saved as {output_file}")

def convert_pdf_to_csv(input_file, output_file):
    pdf = PyPDF2.PdfFileReader(input_file)
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            text = page.extract_text()
            writer.writerow([text])
    print(f"Converted PDF to CSV. Saved as {output_file}")

# Example usage
input_pdf = 'input.pdf'
split_pdf(input_pdf, 'output')  # Split PDF into individual pages

input_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
output_pdf = 'merged.pdf'
merge_pdfs(input_files, output_pdf)  # Merge multiple PDFs into one

input_pdf = 'input.pdf'
output_docx = 'output.docx'
convert_pdf_to_docx(input_pdf, output_docx)  # Convert PDF to DOCX

input_pdf = 'input.pdf'
output_csv = 'output.csv'
convert_pdf_to_csv(input_pdf, output_csv)  # Convert PDF to CSV

