# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__obvservations = []


    def add_observation(self, observation: str):
        if observation != "":
            self.__obvservations.append(observation)
        else:
            raise ValueError("Name of observation may not be empty")

    def latest_observation(self):
        if len(self.__obvservations) == 0:
            return ""
        else:
            return self.__obvservations[-1]

    def number_of_observations(self):
        return len(self.__obvservations)
    
    def __str__(self):
        return f"{self.__name}, {len(self.__obvservations)} observations"

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)