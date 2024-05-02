#!/bin/bash

directory="$1"

# clean
# Remove all files and folders except 'input', 'output', and 'pipeline.yaml'
echo "Cleaning up the directory: $directory"
find "$directory" -mindepth 1 -maxdepth 1 ! -name 'input' ! -name 'output' ! -name 'pipeline.yaml' -exec rm -rf {} +

# Clear the 'output' directory
echo "Clearing the 'output' directory"
rm -rf "$directory/output"/*

echo "Cleanup completed successfully."