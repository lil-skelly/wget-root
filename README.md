# Wget-Root

**⚠️ Warning:** This script is completly for penetration testing purposes. I do not claim any responsibility if you use it for offensive activities.

If the wget  binary has the SUID bit set, It does not drop the elevated privileges and may be abused to access the file system. It may be used to do privileged writes or write files outside a restricted file system. This script automates the rewriting of the `passwd` file of the victims machine
# Usage
Firstly copy the `/etc/passwd` file of the victim to your host machine, using the following command:
`scp user@host /etc/passwd .` <br>
(Be carefull when typing the files destination and don't overwrite your own `/etc/passwd` file) <br>
After copying the `/etc/passwd` file of the victim, it is time to run the exploit. <br>
(You will need to run the exploit with `sudo` since root privileges are needed to modify the `/etc/passwd` file of the victim because of permission reasons)

### Options
```
--file FILE, -f FILE  passwd file to poison
--interface INTERFACE, -i INTERFACE
                      network interface or IP address to host the
                      HTTP server (default: eth0)
--port PORT, -p PORT  port to serve the HTTP server (default: 8000)
```
**Example Command**
```bash
sudo python3 wget_exploit.py --file <passwd copy> --port <webserver port> --interface <network interface/ip>
```
The script will poison the `<passwd copy>` file, by adding the new `root` password. 
Then it will host the `<passwd copy>` file to the web using a custom reuseable python HTTP server.<br>
**Dynamic** instructions will also be printed at the command line during the exploit execution as shown in the picture below.
The password for the `root` user, is simply `root`. 

![Proof Of Concept Video](https://user-images.githubusercontent.com/80885284/182122277-11c1718b-de9a-4bf6-b7aa-8e5f61d7acdb.webm)
![showcase](https://i.imgur.com/1bVzFk8.png)
