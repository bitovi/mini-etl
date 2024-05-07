import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from helpers import hello_from_script, log_directories, extract_text_from_all_pdfs

from langchain_community.document_loaders import PyMuPDFLoader

def run(input_dir, output_dir, config, step):
    hello_from_script(__file__)
    log_directories(input_dir, output_dir, config, step)

    loader_class = PyMuPDFLoader
    output_file_extension = ".pymupdf.txt"

    # find all pdfs in input_dir
    # for each pdf, extract text and save to new directory in output_dir
    extract_text_from_all_pdfs(input_dir, output_dir, loader_class, output_file_extension)
