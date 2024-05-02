import sys
import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
import glob
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

def run(input_dir, output_dir, config, step):
    print(f"Input dir: {input_dir}")
    print(f"Output dir: {output_dir}")
    print(f"Config: {config}")
    print(f"Step: {step}")

    # example: step.filter_files = ["*.unstructured.txt"]
    # if   step.filter_files is set
    # then only process files that match the filter
    # else process all .txt files
    if "filter_files" in step:
        filter_files = step["filter_files"]
    else:
        filter_files = ["*.txt"]

    output_file_extension = ".simple-chunker.txt"
    if "output_file_extension" in step:
        output_file_extension = step["output_file_extension"]

    # find all files in input_dir, filter by filter_files
    # each entry in filter_files is a glob pattern which could yield many files
    # for each file, chunk text and save to new directory in output_dir
    print(f"Chunking text from files in {input_dir} to {output_dir}")
    for filter_file in filter_files:
        for file in glob.glob(f"{input_dir}/{filter_file}"):
            relative_file = os.path.relpath(file, input_dir)
            # call file_chunker_func to chunk text from file
            chunk_text_from_file(input_dir, output_dir, relative_file, step, output_file_extension)
    

def chunk_text_from_file(input_dir, output_dir, file, step, output_file_extension=".simple-chunker.txt"):
    print(f"Chunking text from {file}")
    with open(f"{input_dir}/{file}", "r") as f:
        text = f.read()
        breakpoint_threshold_type = "percentile"
        if "breakpoint_threshold_type" in step:
            breakpoint_threshold_type = step["breakpoint_threshold_type"]

        text_splitter = SemanticChunker(
            OpenAIEmbeddings(), breakpoint_threshold_type=breakpoint_threshold_type
        )

        docs = text_splitter.create_documents([text])
        print("==== doc 0 ====")
        print(docs[0])
        print("==== doc 0 page content ====")
        print(docs[0].page_content)

        # output a chunk per line
        with open(f"{output_dir}/{file}{output_file_extension}", "w") as f:
            for chunk in docs:
                print(f"\n\n==== chunk ====\n")
                print(chunk)
                print(f"\n==== end chunk ====\n\n")

                f.write("\n\n==== chunk ====\n")
                f.write(chunk.page_content + "\n")
                f.write("\n==== end chunk ====\n\n")
