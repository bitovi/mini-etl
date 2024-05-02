# mini-etl

A simple ETL (Extract, Transform, Load) tool for processing files.

## Quick Start

1. Create a new pipeline folder
2. Create a subfolder called `input` and place the files to process in this folder
3. Create a `pipeline.yaml` file in the root of the pipeline folder
4. Run the pipeline

🎉 The processed files will be saved in the `output` folder!


To run the pipeline, use the following commands:
```bash
 ./scripts/pipelines/build.sh
 ./scripts/pipelines/rerun.sh relative/path/to/pipeline
```

## Pipeline Anatomy
Each pipeline is a directory. The directory name is the pipeline name. The directory contains the following:
- `input/`: The input directory containing the files to process.
- `output/`: The output directory where the processed files are saved.
- `pipeline.yaml`: The pipeline configuration file.

### Input Directory
The `input/` directory contains the files to process. The files can be of any type. The pipeline processes all files in the `input/` directory.

### Output Directory
The `output/` directory contains the processed files. The pipeline saves the processed files in the `output/` directory.

### Pipeline Configuration (`pipeline.yaml`)
The root of the pipeline directory contains a `pipeline.yaml` file that defines the pipeline configuration. The configuration file is a YAML file with the following structure:

example `pipeline.yaml`
```yaml
pipeline:
- name: PyPDF
  transformer: transformers/extract-from-pdf/pypdf.py
```

The `pipeline` key is a list of steps. Each step is a dictionary with the following keys:
- `name`: The name of the step.
- `transformer`: The path to the transformer script.
- `copy_src_files`: (optional) A boolean value indicating whether to copy the source files to the output directory. Default is `false`.

## Pipeline Execution
The pipeline processes the files in the `input/` directory using the transformers defined in the `pipeline.yaml` file. The pipeline executes the transformers in the order they are defined in the configuration file.

Each transformer is given the path to an input directory and a path to an output directory. The transformer is responsible for reading the files in the input directory, processing them, and writing the processed files to the output directory.

The script will create intermediate input/output directories for each step in the pipeline. The intermediate directories are named after the step name.

## Transformers
Transformers are Python modules that process the input files. Each transformer is a Python script that reads the input files and writes the processed files to the output directory.

The script will be given the following environment variables:
- `PIPELINE_DIR`: The path to the pipeline directory.
- `INPUT_DIR`: The path to the input directory.
- `OUTPUT_DIR`: The path to the output directory.


### Writing a Transformer
[todo]