# Step into your project directory (if needed)
cd ~/THIS_PROJECT

# Create a virtual environment
python3 -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate

# For Windows (PowerShell)
venv\Scripts\Activate.ps1

# Install libraries from requirements.txt
pip install -r requirements.txt

# Test benchmark for function calls
python3 tools.py