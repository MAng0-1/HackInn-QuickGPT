New-Item -Path 'C:\QuickGPT' -ItemType Directory -Force
New-Service -Name "ClipGPT" -BinaryPathName "$PSScriptRoot\bin\startup.exe" -StartupType "automatic"