import os
import requests
import string
from tqdm import tqdm
import time

URL2 = "https://sigip.infraestruturasdeportugal.pt/pub/rest/services/SITE_EXTERNO_IP/viajar_na_estrada2021/MapServer/3/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount=8000&where=1=1&orderByFields=objectid&outFields=data_ultimo_video,id_camera,estrada,descricao,url1,url2&outSR=4326&spatialRel=esriSpatialRelIntersects"

while (True):
    response = requests.get(URL2)
    json = response.json()
    items = json['features']
    for obj in tqdm(items):
        attrs = obj['attributes']
        response2 = requests.get(attrs["url1"])
        name = attrs['descricao'] + str(attrs['data_ultimo_video']) + ".mp4"
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        name = ''.join(c for c in name if c in valid_chars).replace(' ', '_')
        # print(name)
        path = str(attrs['estrada']) + '/' + str(attrs['id_camera']) + '/' + str(attrs['data_ultimo_video']) + '/'
        if not os.path.exists(path):
            os.makedirs(path)
            open(path + name, "wb").write(response2.content)

    time.sleep(300)
