# importing the required module
import matplotlib.pyplot as plt
import read_gsheets

#getting the data from google sheets
summary_sheet_data = read_gsheets.get_chart_data('Summary!A:D')

day = []
avg_temp = []
avg_weather = []
no_layers = []
master_list = [avg_temp, avg_weather, no_layers]
y_ax_names = ['Temperature (%)', 'Weather (C)', 'Number of Layers']
graph_save_names = ['temp_graph', 'weather_graph', 'layer_graph']

#parsing data from spreadsheet into correct local lists
for i in summary_sheet_data:
    day.append(i[0])
    avg_temp.append(i[1])
    avg_weather.append(i[2])
    no_layers.append(i[3])

def create_plots(y_axis, y_axis_name, save_name):
    plt.figure()
    plt.plot(day, y_axis)
    plt.xlabel('Day')
    plt.ylabel(y_axis_name)
    plt.title(y_axis_name + ' v Day')
    plt.savefig('docs/assets/' + save_name +'.png')

for i in range(len(y_ax_names)):
    create_plots(master_list[i], y_ax_names[i], graph_save_names[i])