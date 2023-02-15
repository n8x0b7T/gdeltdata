import pandas as pd
from urllib.parse import urlparse
import requests

df = pd.read_csv("merged_snorkel.csv")

domains = []

for i in df['SOURCEURL']:
    domains.append(urlparse(i).netloc)

enpoints = ['/rss', '/feed']

for i in set(domains):
    for j in enpoints:
        try:
            r = requests.get(f"http://{i+j}")
        except:
            break
            pass
        if r.status_code == 200:
            print(i+j)
            break