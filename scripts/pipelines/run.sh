#!/bin/bash

directory="$1"

docker run \
-v $(pwd):/app \
-v $(pwd)/$1:/mini-etl/pipeline \
-e PIPELINE_DIR=/mini-etl/pipeline \
bitovi/mini-etl:local