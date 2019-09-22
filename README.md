## Buffer overflow Windows exploit development practice - 50 proof of concepts

I am following the `Windows Exploit Development Tutorial Series` as a guide for exploit development progression from https://www.fuzzysecurity.com/tutorials.html

First I learn how to exploit a certain type of protections or restriction, then read lot's of exploits and writeups about it, then search exploit-db for software that is vulnerable to that specific attack vector, then I test my new knowledge against said software. 

Eventually I will start hunting for 0day in software that relates to these topics.

----
I am writing 50 POC's for various exploits, some which include bypassing advanced memory protections for educational purposes.

```
Current status : 16/100
Metasploit modules: 0
Metasploit contributions : 0
0day discoveries : 4
Assigned CVE's : 
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
5. Millenium MP3 Studio 2.0 SEH overflow [local]
6. File sharing wizard SEH overflow
----
## Unicode Buffer Overflows

----
## ROP to bypass Data Exectuion Prevention (DEP)

1. Vulnserver TRUN + DEP enabled + ROP chain - VirtualProtect() method

----
## Bypassing ASLR

----
## 0day discoveries

1. DeviceViewer Sricam 3.12.0.1 SEH overflow
2. DeviceViewer Sricam 3.12x DOS buffer overflow 
3. DeviceViewer Sricam 3.12x DOS buffer ovlerflow 
4. Easy File Sharing Web Server 7.2 local SEH overflow
 
----
## Metasploit modules
