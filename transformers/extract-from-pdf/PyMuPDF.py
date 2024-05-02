import sys
import os
import shutil
from langchain_community.document_loaders import PyMuPDFLoader

def run(input_dir, output_dir, config, step):
    print("hello world from PyMuPDF.py")

    print(f"Input dir: {input_dir}")
    print(f"Output dir: {output_dir}")
    print(f"Config: {config}")
    print(f"Step: {step}")

    # find all pdfs in input_dir
    # for each pdf, extract text and save to new directory in output_dir
    print(f"Extracting text from PDFs in {input_dir} to {output_dir}")
    for file in os.listdir(input_dir):

        # check if file is a pdf
        if file.endswith(".pdf"):
            # call file_extractor_func to extract text from pdf
            extract_text_from_pdf(input_dir, output_dir, file)


def extract_text_from_pdf(input_dir, output_dir, file, output_file_extension=".pymupdf.txt"):
    pdf_path = f"{input_dir}/{file}"

    print(f"Extracting text from {pdf_path}")
    pdf_loader = PyMuPDFLoader(pdf_path)
    lines = pdf_loader.load()
    
    with open(f"{output_dir}/{file}{output_file_extension}", "w") as f:
        for line in lines:
            f.write(line.page_content + "\n")
        print(f"Text extracted from {file}")
