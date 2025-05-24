# SecureBank fraud detection exercise

This is a simple Flask API that lets you send in transaction info and it tells you if it's probably fraud. It's built in Python and runs in Docker, which just means it works the same no matter where you run it.


## What this code does

- Loads a little fake model that randomly says "fraud" or "not fraud" (Model implementation in future iterations)
- Takes in transaction data as JSON (you send it via curl)
- Tells you what the model thinks (random 0 not fraud or 1 fraud)
- Runs in a Docker container so you don't need to mess with local installs


## What you need

- Python files 
- Docker Desktop installed and running
- Terminal access (PowerShell or Command Prompt works)
- this does not include the data_sources folder, that needs to be added in the directory


## How to run it

1. Download content

2. add data_sources to securebank folder

3. Open a Powershell terminal  
   Navigate to the `Enabled-AI-Securbank` folder. 

   #### powershell commands: 
    4) cd your_file_path\Enabled-AI-Securebank"

    5) docker build -t securebank-app .

    6) docker run -p 5000:5000 securebank-app
	* if it works it will say "Running on http://#####:5000"

7.  Open a second Powershell terminal

   #### powershell commands: 
    8) cd your_file_path\Enabled-AI-Securebank"

    9) cmd /c curl -X POST http://localhost:5000/predict/ -H "Content-Type: application/json" --data-binary "@data_sources/test.json"
	* output will be {'prediction': 1} or {'prediction': 0}

