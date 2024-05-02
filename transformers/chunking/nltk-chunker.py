import sys
import os
import shutil
import glob
from langchain_text_splitters import NLTKTextSplitter

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

    output_file_extension = ".nltk-chunker.txt"
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
            chunk_text_from_file(input_dir, output_dir, relative_file, output_file_extension)
    

def chunk_text_from_file(input_dir, output_dir, file, output_file_extension=".nltk-chunker.txt"):
    print(f"Chunking text from {file}")
    with open(f"{input_dir}/{file}", "r") as f:
        text = f.read()
        text_splitter = NLTKTextSplitter(chunk_size=1000)
        docs = text_splitter.split_text(text)
        print("==== doc 0 ====")
        print(docs[0])

        # output a chunk per line
        with open(f"{output_dir}/{file}{output_file_extension}", "w") as f:
            for chunk in docs:
                # print(f"\n\n==== chunk ====\n")
                # print(chunk)
                # print(f"\n==== end chunk ====\n\n")

                f.write("\n\n==== chunk ====\n")
                f.write(chunk + "\n")
                f.write("\n==== end chunk ====\n\n")
