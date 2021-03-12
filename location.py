import googlemaps
import sys
from datetime import datetime
import csv
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
GOOGLEAPIKEY=os.environ.get("APIKEY")

def main(csv_name,add_name):
    key = GOOGLEAPIKEY
    client = googlemaps.Client(key)
    full_list = []
    dl = download_lists(csv_name)
    for e, i in enumerate(dl):
        geocode_result = client.geocode(i[0])
        loc = geocode_result[0]['geometry']['location']
        name= add_name + i[1]
        list = [name, i[0], loc['lat'], loc['lng']]
        full_list.append(list)
        time.sleep(3)
        print(str(e+1) + "/" + str(len(dl)))
    print(full_list)
    wite(full_list, csv_name)



def wite(full_list, csv_name):  # 結果をCSVに書き込む
    with open("new_" + csv_name, 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in full_list:
            writer.writerow(i)


def download_lists(csv_name):
    result = []
    with open(csv_name, newline="", encoding="utf-8") as csvfile:
        spreader = csv.reader(csvfile)
        for row in spreader:
            result.append(row)
    return result


if __name__ == '__main__':
    main("sakai.csv", "(サカイ)")
    main("nippon.csv", "(日本大学)")
    main("nittaidai.csv", "(日体大)")
    main("art.csv", "(アート)")
