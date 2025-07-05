import subprocess
import requests
import json
import time

# Load test prompts from file
def load_test_cases(filename="test_prompts.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Load tools from file
def load_tools(filename="tools_list.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Get list of models from `ollama list`
def get_ollama_models():
    result = subprocess.run(['ollama', 'list'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split('\n')[1:]  # skip header
    return [line.split()[0] for line in lines if line.strip()]

# Run individual test
def run_test(model, test_input, tools):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": test_input}],
        "tools": tools,
        "tool_choice": "auto",
        "temperature": 0
    }

    start = time.time()
    try:
        response = requests.post("http://localhost:11434/v1/chat/completions", json=payload)
        latency = time.time() - start
        response.raise_for_status()
        data = response.json()
        function_name = data["choices"][0]["message"]["tool_calls"][0]["function"]["name"]
    except Exception as e:
        function_name = "(none)"
        latency = time.time() - start
    return function_name, latency

# Main benchmark loop
def benchmark():
    test_cases = load_test_cases()
    tools = load_tools()
    models = get_ollama_models()

    for model in models:
        print(f"\n🧪 Testing model: {model}")
        for test in test_cases:
            function_name, latency = run_test(model, test["input"], tools)
            status = "✅ PASS" if function_name == test["expected_function"] else "❌ FAIL"
            print(f"Prompt: {test['input']}")
            print(f"Expected: {test['expected_function']}, Got: {function_name}, Latency: {latency:.2f}s [{status}]\n")

if __name__ == "__main__":
    benchmark()
