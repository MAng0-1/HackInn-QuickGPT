New-Item -Path 'C:\QuickGPT' -ItemType Directory -Force
New-Service -Name "ClipGPT" -BinaryPathName 'C:\QuickGPT\startup.exe' -StartupType "automatic"