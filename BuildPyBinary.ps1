sudo apt install python3-tk
pip3 install pyperclip keyboard openai

pyinstaller `
  --distpath "$PSScriptRoot/bin" `
  --workpath "$PSScriptRoot/build" `
  --noconfirm `
  --onefile `
  --name "startup.exe" `
  --paths "~/.local/lib/python3.10/site-packages:/usr/lib/python3.10/tkinters"`
  keyboard_listener.py
