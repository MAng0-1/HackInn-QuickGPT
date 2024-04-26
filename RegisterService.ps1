New-Item -Path 'C:\QuickGPT' -ItemType Directory -Force
New-Service -Name "ClipGPT" -BinaryPathName "$PSScriptRoot\dist\startup.exe" -StartupType "automatic"