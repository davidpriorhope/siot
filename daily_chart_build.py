# importing the required module
import matplotlib.pyplot as plt
import datetime

time_list = open('temp_data/time.txt', "r").read().splitlines()
temp_list = list(map(float, open('temp_data/temp_raw.txt', "r").read().splitlines()))
weather_list = list(map(float, open('temp_data/weather.txt', "r").read().splitlines()))

plt.figure()

plt.plot(time_list, temp_list, label = "Body Temperature")

plt.plot(time_list,weather_list, label = "Weather Temperature")

plt.xlabel('Time')

plt.ylabel('Temperature (C)')

plt.title(str(datetime.datetime.now().strftime('%d.%m.%y')))

plt.legend()

plt.savefig('docs/assets/latest_graph.png')