import os
import shutil

# copy all files from input_dir to output_dir
def run(input_dir, output_dir, config, step):
    print(f"Copying files from {input_dir} to {output_dir}")
    for file in os.listdir(input_dir):
        shutil.copy(f"{input_dir}/{file}", output_dir)
        print(f"Copying {file}")