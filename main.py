import googlemaps
import sys
from datetime import datetime
import csv


def main(uni_csv_name):
    university_locations = download_lists(uni_csv_name)
    hikkoshi_locations = download_lists("new_art.csv")
    for i in download_lists("new_sakai.csv"):
        hikkoshi_locations.append(i)
    for i in university_locations:
        areas =comparison_area(i[0], i[2], i[3])
        for a in hikkoshi_locations:
            n_lat = float(a[2])
            n_lon = float(a[3])
            if n_lat > areas[1] and n_lat < areas[2] and n_lon > areas[3] and n_lon < areas[4]:
                print(a[0],areas[0])
                continue





def download_lists(csv_name):
    result = []
    with open(csv_name, newline="", encoding="utf-8") as csvfile:
        spreader = csv.reader(csvfile)
        for row in spreader:
            result.append(row)
    return result

def comparison_area(location, target_latitude, target_longitude, size=5):
    # 日本における大体の緯度経度が１km= 0.0090133729745762(南北) １km=0.010966404715491394(東西)であるので、
    # 楕円を描くのはめんどくさいので東西南北５kmの箱を想定してその中に引越会社があるかを判定する。
    # 参考文献: https://easyramble.com/latitude-and-longitude-per-kilometer.html
    north_w = 0.0090133729745762
    east_w = 0.010966404715491394
    min_lat = float(target_latitude)-(east_w*size)
    max_lat = float(target_latitude)+(east_w*size)
    min_lon = float(target_longitude)-(north_w*size)
    max_lon = float(target_longitude)+(north_w*size)
    return [location, min_lat, max_lat, min_lon, max_lon]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main("new_nippon.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
