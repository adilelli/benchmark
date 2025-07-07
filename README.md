# Ollama Benchmark
This is for benchmark testing LLM installed from Ollama for function calls and latency

## Step into your project directory (if needed)
cd ~/THIS_PROJECT

## Create a virtual environment
python3 -m venv benchmark

## Activate it (macOS/Linux)
source benchmark/bin/activate

## For Windows (PowerShell)
venv\Scripts\Activate.ps1

## Install libraries from requirements.txt
pip install -r requirements.txt

## Test benchmark for function calls
python3 tools.py