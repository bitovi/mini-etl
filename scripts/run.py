import os
import yaml
import importlib.util
import sys
from dotenv import load_dotenv

print("=====================================")
print("# Running ETL script")
print("=====================================")

# read dotenv file
load_dotenv()

# variables
pipeline_dir = os.environ.get('PIPELINE_DIR')
pipeline_input_dir = os.path.join(pipeline_dir, 'input')
pipeline_output_dir = os.path.join(pipeline_dir, 'output')
pipeline_config = os.path.join(pipeline_dir, 'pipeline.yaml')
openai_api_key = os.environ.get('OPENAI_API_KEY')

print("")
print("=========================== Environment variables")
print(f"PIPELINE_DIR={pipeline_dir}")
print("=========================== end Environment variables")

# Read the pipeline config file
print("")
print("=========================== Reading Pipeline Config")

with open(pipeline_config, 'r') as f:
    pipeline_config_contents = f.read()
    pipeline_config_obj = yaml.safe_load(pipeline_config_contents)

    print("")
    print("=====")
    print("Pipeline config object:")
    print(pipeline_config_obj)

    steps = pipeline_config_obj['pipeline']

    initial_input_dir = f"{pipeline_input_dir}"
    final_output_dir = f"{pipeline_output_dir}"

    previous_step_output_dir = initial_input_dir

    print(f"Initial input dir: {initial_input_dir}")
    print(f"Final output dir: {final_output_dir}")
    print("=====")

    for step in steps:
        step_name = step['name']
        transformer = step['transformer']
        copy_src_files = step.get('copy_src_files', False)

        print("")
        print("")
        print(f"=========================== Running step {step_name} ===========================")

        print("")
        print("Step details")
        print("===")
        print(f"Running step: {step}")
        print(f"Step name: {step_name}")
        print(f"Transformer: {transformer}")


        # Load the transformer module
        spec = importlib.util.spec_from_file_location("module.name", transformer)
        transformer_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(transformer_module)

        # make new directory for the output of this step
        step_output_dir = f"{pipeline_dir}/{step_name}"
        input_dir=previous_step_output_dir
        output_dir=step_output_dir


        print(f"Ensuring step output dir exists: {step_output_dir}")
        os.makedirs(step_output_dir, exist_ok=True)
        print("===")

        if copy_src_files:
            print(f"Copying source files from {input_dir} to {step_output_dir}")
            os.system(f"cp -r {input_dir}/. {step_output_dir}")
            print("===")

        # Run the transformer module
        print("")
        print(f"Running transformer module: {input_dir} {output_dir} {pipeline_config_obj} {step}")
        print("===")
        transformer_module.run(input_dir, output_dir, pipeline_config_obj, step)
        print("===")
        print("")
        



        # Update the previous step output dir
        previous_step_output_dir = step_output_dir
        print(f"=========================== Step {step_name} Complete ===========================")


    # Copy the final output to the pipeline output dir
    print(f"Copying final output to {final_output_dir}")
    os.system(f"cp -r {previous_step_output_dir}/. {final_output_dir}")







print("# ETL script completed")
print("=====================================")
print("=====================================")