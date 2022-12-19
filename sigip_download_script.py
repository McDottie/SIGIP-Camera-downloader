import os
import requests
import string
from tqdm import tqdm
import time
import argparse

def main():

    parser = argparse.ArgumentParser(prog='SIGIP Download Scrip',
                                    description='This script downloads SIGIP Traffic cameras',
                                    epilog='If you have any questions open a Issue on Github at https://github.com/McDottie/SIGIP-Camera-downloader/issues')

    parser.add_argument('-r', '--roads', help='Download Speciffic roads. Ex: "IC8,A1"',
                        required=False)

    args = vars(parser.parse_args())
    roads = args["roads"]
    URL2 = "https://sigip.infraestruturasdeportugal.pt/pub/rest/services/SITE_EXTERNO_IP/viajar_na_estrada2021/MapServer/3/query?f=json&cacheHint=true&resultOffset=0&resultRecordCount=8000&where=1=1&orderByFields=objectid&outFields=data_ultimo_video,id_camera,estrada,descricao,url1,url2&outSR=4326&spatialRel=esriSpatialRelIntersects"

    while (True):
        response = requests.get(URL2)
        json = response.json()
        items = json['features']
        for obj in tqdm(items):
            attrs = obj['attributes']
            if (roads is not None and attrs['estrada'] in roads) or roads is None:
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


if __name__ == "__main__":
    main()
