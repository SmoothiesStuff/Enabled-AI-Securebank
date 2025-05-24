# SecureBank Fraud Detection API

This is a simple Flask API that lets you send in transaction info and it tells you if it's probably fraud. It's built in Python and runs in Docker, which just means it works the same no matter where you run it.


## What This Project Does

- Loads a little fake model that randomly says "fraud" or "not fraud" (Model implementation in future iterations)
- Takes in transaction data as JSON (you send it via curl)
- Tells you what the model thinks (random 0 not fraud or 1 fraud)
- Runs in a Docker container so you don't need to mess with local installs


## What You Need

- Python files and a `test.json` file (already included)
- Docker Desktop installed and running
- Terminal access (PowerShell or Command Prompt works)


## How to Run It (Quick Start)

1. **Open a terminal**  
   Navigate to the `securebank` folder. You can paste this in if you're in PowerShell:

   ```powershell
    1) cd "G:\Documents G\Hopkins\AI enabled systems\securebank"

    2) docker build -t securebank-app .

    3) docker run -p 5000:5000 securebank-app
	* if it works it will say "Running on http://#####:5000"

    4) cmd /c curl -X POST http://localhost:5000/predict/ -H "Content-Type: application/json" --data-binary "@data_sources/test.json"
	* output will be {'prediction': 1} or {'prediction': 0}