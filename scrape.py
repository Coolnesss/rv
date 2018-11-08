import requests
import os
from lxml import html
session_requests = requests.session()
import numpy as np

login_url = "https://rv.tko-aly.fi/userauth.php"
result = session_requests.get(login_url)
tree = html.fromstring(result.text)

payload = {
	"username": "chra", 
	"passwd": os.environ["PASS"]
}

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)
tree = html.fromstring(result.content)
asd = tree.xpath("//code/text()")

all_bought = np.array(asd)
np.savetxt("all.csv", all_bought, delimiter=",", fmt="%s")