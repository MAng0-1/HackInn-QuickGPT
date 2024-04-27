python3 -m venv venv
python -m venv venv
./venv/bin/Activate.ps1
./venv/Scripts/Activate.ps1

pip3 install pyinstaller pyperclip keyboard openai
pyinstaller `
  --noconfirm `
  --onefile `
  --clean `
  --name "startup.exe" `
  --paths "$PSScriptRoot/venv/lib:/usr/lib/python3.10/tkinters"`
  "$PSSCriptRoot/python_prototype/main.py"

deactivate
