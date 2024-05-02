#!/bin/bash

directory="$1"

script_directory=$(dirname "$0")

# run sibling file `clean.sh` to clean up the directory
bash ${script_directory}/clean.sh "$directory"

# run sibling file `run.sh` to run the pipeline
bash ${script_directory}/run.sh "$directory"