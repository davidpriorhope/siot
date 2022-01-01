# importing the required module
import matplotlib.pyplot as plt
import datetime
import numpy as np

time_list = open('temp_data/time.txt', "r").readlines()
temp_list = list(map(float, open('temp_data/temp_raw.txt', "r").readlines()))
weather_list = list(map(float, open('temp_data/weather.txt', "r").readlines()))

cal_temp= temp_list[0]/(float(open('temp_data/temp_per.txt', "r").readline()))
no_layer = float(open('temp_data/summary_no_layers.txt', "r").readlines()[-1]) #note for this to work you need to run read_gsheets before

plt.figure()

plt.plot([], [], ' ', label= str(no_layer)  + " layer(s) worn")

plt.plot(time_list, temp_list,  color='b', label ="Body Temperature")

plt.plot(time_list,weather_list,  color='g', label = "Weather Temperature")

plt.axhline(cal_temp, color='r', label="Calibration Temperature")

plt.xlabel('Time')

plt.ylabel('Temperature (C)')

plt.title(str(datetime.datetime.now().strftime('%d.%m.%y')))

plt.legend()


no_ticks = 10

seperation = (len(time_list))/(no_ticks-1)

tick_array = np.floor(np.arange(0, len(time_list)+1, step=seperation))

tick_array[no_ticks-1]=len(time_list)-1

plt.xticks(tick_array, rotation = 30)

plt.savefig('docs/assets/latest_graph.png',bbox_inches='tight')