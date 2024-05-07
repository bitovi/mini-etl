import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from helpers import hello_from_script, log_directories

from langchain_community.document_loaders import PyPDFLoader

def run(input_dir, output_dir, config, step):
    hello_from_script(__file__)
    log_directories(input_dir, output_dir, config, step)

    # find all pdfs in input_dir
    # for each pdf, extract text and save to new directory in output_dir
    print(f"Extracting text from PDFs in {input_dir} to {output_dir}")
    for file in os.listdir(input_dir):

        # check if file is a pdf
        if file.endswith(".pdf"):
            # call file_extractor_func to extract text from pdf
            extract_text_from_pdf(input_dir, output_dir, file)


def extract_text_from_pdf(input_dir, output_dir, file, output_file_extension=".pypdf.txt"):
    pdf_path = f"{input_dir}/{file}"

    print(f"Extracting text from {pdf_path}")
    pdf_loader = PyPDFLoader(pdf_path)
    pages = pdf_loader.load_and_split()
    
    with open(f"{output_dir}/{file}{output_file_extension}", "w") as f:
        page_index = 1
        for page in pages:
            f.write(f"==== page {page_index} ====\n")
            # f.write(page.dict())
            f.write(page.page_content)
            f.write(f"==== end page {page_index} ====\n")
            page_index += 1
        print(f"Text extracted from {file}")
