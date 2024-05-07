import os

def hello_from_script(script_path):
    script_name = os.path.basename(script_path)
    print(f"hello world from {script_name}")

def log_directories(input_dir, output_dir, config, step):
    print("in helpers!")
    print(f"Input dir: {input_dir}")
    print(f"Output dir: {output_dir}")
    print(f"Config: {config}")
    print(f"Step: {step}")

def extract_text_from_all_pdfs(input_dir, output_dir, loader_class, output_file_extension):
    print("in helpers!")
    print(f"Extracting text from PDFs in {input_dir} to {output_dir}. Using: {loader_class.__name__}")
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            extract_text_from_pdf(input_dir, output_dir, file, loader_class, output_file_extension)

def extract_text_from_pdf(input_dir, output_dir, file, loader_class, output_file_extension):
    print("in helpers!")
    pdf_path = os.path.join(input_dir, file)
    pdf_loader = loader_class(pdf_path)
    lines = pdf_loader.load()

    output_file_path = os.path.join(output_dir, file + output_file_extension)
    with open(output_file_path, "w") as f:
        for line in lines:
            f.write(line + "\n")
        print(f"Text extracted from {file}")

# def run_transformer(script_name, config, step, input_dir, output_dir, loader_class, output_file_extension):
#     print("in helpers!")
#     hello_from_script(script_name)
#     log_directories(input_dir, output_dir, config, step)
