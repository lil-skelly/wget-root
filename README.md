# Wget-Root

**⚠️ Warning:** This script is completly for white hat activities. I do not claim any responsibility for the damage it may cause if used for offensive purposes.

If the wget binary has the SUID bit set, It does not drop the elevated privileges and may be abused to access the file system. It may be used to do privileged writes or write files outside a restricted file system. This script automates the rewriting of the `passwd` file of the victims machine
# Usage
Firstly copy the `/etc/passwd` file of the victim to your host machine, using the following command:
`scp user@host /etc/passwd .` <br>
( ⚠️ Be carefull when typing the files destination and don't overwrite your own `/etc/passwd` file) <br>
After copying the `/etc/passwd` file of the victim, it is time to run the exploit. <br>
( ⚠️ You will need to run the exploit with `sudo` since root privileges are needed to modify the `/etc/passwd` file of the victim because of permission reasons)

```
usage: sudo wget_exploit.py [-h] [--file FILE] [--interface INTERFACE] [--port PORT] [--password PASSWORD]

Poison the victims /etc/passwd file and host it over HTTP. Overwrite the /etc/passwd file of the victim by abusing the SUID bit of the wget binary.

options:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  passwd file to poison
  --interface INTERFACE, -i INTERFACE
                        network interface or IP address to host the HTTP server (default: eth0)
  --port PORT, -p PORT  port to serve the HTTP server (default: 8000)
  --password PASSWORD, -P PASSWORD
                        password to set for the root user (default: root)

```
   
The script will poison the `<passwd copy>` file, by adding the new `root` password. 
Then it will host the `<passwd copy>` file to the web using a custom reuseable python HTTP server.<br>
**Dynamic** instructions will also be printed at the command line during the exploit execution as shown in the picture below.
The password for the `root` user, is simply `root`. 

![Proof Of Concept Video](https://user-images.githubusercontent.com/80885284/182122277-11c1718b-de9a-4bf6-b7aa-8e5f61d7acdb.webm) <br>
![Screenshot 2022-08-01 11:01:30](https://user-images.githubusercontent.com/80885284/182182543-b10b2e50-64c3-4f57-ab8e-ea0ddde7561a.png)

[TryHackMe](https://tryhackme.com) has an [awesome machine](https://tryhackme.com/room/wgelctf) that lets you play with this exploit. <br>
⚠️ Solving CTF's with others exploit just kills the fun. Using this exploit to solve the ctf above is not recommended for begginers in the world of IT. More advanced users are welcome to use this exploit to automatically solve the CTF listed above for fun or for testing purposes.
