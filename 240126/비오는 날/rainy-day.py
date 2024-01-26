n = int(input())

class Weather:
    def __init__(self, day, week, weather):
        self.day = day
        self.week = week
        self.weather = weather
weathers = []
for _ in range(n):
    day, week, weather = tuple(input().split())
    if weather == "Rain":
        weathers.append(Weather(day, week, weather))

minidx = 0
for i in range(len(weathers)):
    if weathers[i].day < weathers[minidx].day:
        minidx = i
print(weathers[minidx].day, weathers[minidx].week, weathers[minidx].weather)