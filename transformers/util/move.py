import os
import shutil

# copy all files from input_dir to output_dir
def run(input_dir, output_dir, config, step):
    print(f"Moving files from {input_dir} to {output_dir}")
    for file in os.listdir(input_dir):
        shutil.move(f"{input_dir}/{file}", output_dir)
        print(f"Moving {file}")