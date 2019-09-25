## Buffer overflow Windows exploit development practice - 50 proof of concepts

I challenged myself to write 50 proof of concepts from scratch for pre-existing exploits, I see this as good practice.

After practicing writing existing exploits, I am also testing new software and hunting for 0days that I can publish and obtain CVEs for.

----
I am writing 50 POC's for various exploits, some which include bypassing advanced memory protections for educational purposes.

```
Current status : 17/50
Metasploit modules: 0
Metasploit contributions : 0
0day discoveries : 5
Assigned CVE's : 1
```

I would like to include but not be limited to : Vannila EIP overwrite, SEH + egghunters, ASLR/DEP/NX , SafeSeh, Stack cookies, unicode restrictions, and much more...

----
## Vanilla Stack Based Buffer Overflow

1. Vulnserver TRUN vanilla EIP overflow
2. FreeFloat FTP Server vanilla EIP overflow
3. PCMan FTP Server vanilla EIP overflow
4. Brainpan VulnHub box vanilla EIP overflow
5. DoStackBufferOverflowGood vanilla EIP overflow
6. MiniShare 1.4.1 vanilla EIP overflow

----
## Structured Exception Handler (SEH) Overwrite + egghunter

1. Easy File Sharing Web Server SEH overflow
2. Easy File Sharing Web Server SEH overflow + egghunter
3. Vulnserver GMON SEH overflow + egghunter
4. Xitami Web Server 2.5 SEH overflow + egghunter + partial SEH overwrite
5. Millenium MP3 Studio 2.0 SEH overflow

----
## Alphanumeric restrictions
   **Unicode restrictions:**
   
   **Hex restrictions:**

----
## ROP to bypass Data Exectuion Prevention (DEP)

1. Vulnserver TRUN + DEP enabled + ROP chain - VirtualProtect() method

----
## Vanilla Heap spraying

----
## 0day discoveries / disclosures

1. DeviceViewer Sricam 3.12.0.1 SEH overflow
2. [**exploit-db**](https://www.exploit-db.com/exploits/47410) DeviceViewer Sricam 3.12x local DOS buffer overflow
3. [**exploit-db**](https://www.exploit-db.com/exploits/47411) Easy File Sharing Web Server 7.2 SEH overflow 
4. [**CVE-2019-16724**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16724) File Sharing Wizard remote SEH overflow
 
----
## Metasploit modules
