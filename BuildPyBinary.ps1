python3 -m venv venv
./venv/bin/Activate.ps1

pip3 install pyperclip keyboard openai
pyinstaller `
  --noconfirm `
  --onefile `
  --clean `
  --name "startup.exe" `
  --paths "$PSScriptRoot/venv/lib:/usr/lib/python3.10/tkinters"`
  keyboard_listener.py

deactivate