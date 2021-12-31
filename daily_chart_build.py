# importing the required module
import matplotlib.pyplot as plt
import datetime
import numpy as np

time_list = open('temp_data/time.txt', "r").read().splitlines()
temp_list = list(map(float, open('temp_data/temp_raw.txt', "r").read().splitlines()))
weather_list = list(map(float, open('temp_data/weather.txt', "r").read().splitlines()))

no_ticks = 10

seperation = (len(time_list))/(no_ticks-1)

plt.figure()

plt.plot(time_list, temp_list, label = "Body Temperature")

plt.plot(time_list,weather_list, label = "Weather Temperature")

plt.xlabel('Time')

plt.ylabel('Temperature (C)')

plt.title(str(datetime.datetime.now().strftime('%d.%m.%y')))

plt.legend()

tick_array = np.floor(np.arange(0, len(time_list)+1, step=seperation))

tick_array[no_ticks-1]=len(time_list)-1

plt.xticks(tick_array, rotation = 30)

plt.savefig('docs/assets/latest_graph.png',bbox_inches='tight')