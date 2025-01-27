#!/bin/bash

set -a
source .env
eval "$(micromamba shell hook --shell bash)"
micromamba activate vkr_tiler