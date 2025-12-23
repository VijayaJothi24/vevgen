# VEVGEN

A minimal Python project that uses the OpenAI Python client. Contains setup instructions, environment variable usage, and Azure-specific notes.

## Prerequisites

- Python 3.8+ installed (Windows: use the `py` launcher).
- Git (optional).

## Setup (Windows)

PowerShell:

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv
```

Command Prompt (cmd.exe):

```bat
py -3 -m venv venv
.\venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install openai python-dotenv
```

Git Bash / WSL (Linux/macOS):

```bash
python3 -m venv venv
source venv/bin/activate   # or source venv/Scripts/activate on some Git Bash setups
python -m pip install --upgrade pip
pip install openai python-dotenv
```

Or install without activating (Windows):

```bash
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install openai python-dotenv
```

## Environment variables

Create a `.env` file in the project root with at least your API key:

```
OPENAI_API_KEY=sk-...
```

For Azure OpenAI, set these as well:

```
OPENAI_API_TYPE=azure
OPENAI_API_VERSION=2023-05-15
OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
```

Add `.env` to your `.gitignore` to avoid committing secrets.

## Example usage

Load environment variables and configure the client:

```python
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]
# For Azure, also set:
# openai.api_type = os.environ.get("OPENAI_API_TYPE")
# openai.api_base = os.environ.get("OPENAI_API_BASE")
# openai.api_version = os.environ.get("OPENAI_API_VERSION")

# Example API call (adjust for the client methods you use):
# resp = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role":"user","content":"Hello"}])
# print(resp)
```

## Requirements file

Optionally create `requirements.txt`:

```
openai
python-dotenv
```

Then install with:

```bash
pip install -r requirements.txt
```

## Security

Do not commit `OPENAI_API_KEY` or `.env` to source control. Use environment management or secrets stores for production.