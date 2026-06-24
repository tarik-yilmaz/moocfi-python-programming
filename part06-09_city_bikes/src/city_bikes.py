# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str) -> dict:
    stations = {}

    with open(f"src/{filename}") as new_file:
        for line in new_file:
            line = line.replace("\n", "")

            parts = line.split(";")

            if parts[0] == "Longitude":
                continue

            station = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])

            stations[station] = (longitude, latitude)
    
    return stations


def distance(stations: dict, station1: str, station2: str) -> float:
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict) -> tuple:

    station_names = list(stations.keys())

    greatest = 0
    station1 = ""
    station2 = ""

    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            name1 = station_names[i]
            name2 = station_names[j]

            calculated_distance = distance(stations, name1, name2)

            if calculated_distance > greatest:
                greatest = calculated_distance
                station1 = name1
                station2 = name2

    return station1, station2, greatest