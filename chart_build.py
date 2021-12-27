# importing the required module
import matplotlib.pyplot as plt
import read_gsheets

#getting the data from google sheets
summary_sheet_data = read_gsheets.get_chart_data('Summary!A:D')

day = []
avg_temp = []
avg_weather = []
no_layers = []
master_list = [avg_weather, no_layers]
x_ax_names = ['Weather (C)', 'Number of Layers']
graph_save_names = ['weather_graph', 'layer_graph']

#parsing data from spreadsheet into correct local lists
for i in summary_sheet_data:
    day.append(i[0])
    avg_temp.append(round(float(i[1]),3))
    avg_weather.append(float(i[2]))
    no_layers.append(float(i[3]))

def create_plots(x_axis, x_axis_name, save_name):

    sorted_x_axis, sorted_avg_temp, sorted_day = zip(*sorted(zip(x_axis, avg_temp, day)))

    plt.figure()
    plt.plot(sorted_x_axis, sorted_avg_temp, 'bo-')
    plt.xlabel(x_axis_name)
    plt.ylabel('Body Temperature (%)')
    plt.title('Body temperature v ' + x_axis_name)

    count = 0

    for x,y in zip(sorted_x_axis, sorted_avg_temp):
        label = sorted_day[count]
        count +=1
        plt.annotate(label, # this is the text
                    (x,y), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.savefig('docs/assets/' + save_name +'.png')

for i in range(len(x_ax_names)):
    create_plots(master_list[i], x_ax_names[i], graph_save_names[i])