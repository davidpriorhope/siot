# importing the required module
import matplotlib.pyplot as plt
import numpy as np


day = open('temp_data/summary_day.txt', "r").read().splitlines()
avg_weather = list(map(float, open('temp_data/summary_avg_weather.txt', "r").read().splitlines()))
no_layers = list(map(float, open('temp_data/summary_no_layers.txt', "r").read().splitlines()))
avg_temp = []

for i in open('temp_data/summary_avg_temp.txt', "r").read().splitlines():
    avg_temp.append(round(float(i),3))


master_list = [avg_weather, no_layers]
x_ax_names = ['Weather (C)', 'Number of Layers']
graph_save_names = ['weather_graph', 'layer_graph']
temp_data_names = ['weather_correlation', 'layer_correlation']

def write_data(my_list, save_name):
    textfile = open('temp_data/' +save_name+".txt", "w")
    for i in my_list:
        textfile.write(str(i) + "\n")
    textfile.close()


def create_plots(x_axis, x_axis_name, graph_save_name,temp_save_name):

    sorted_x_axis, sorted_avg_temp, sorted_day = zip(*sorted(zip(x_axis, avg_temp, day)))

    plt.figure()

    #Calculating trendline
    z = np.polyfit(sorted_x_axis,sorted_avg_temp,1)
    p = np.poly1d(z)
    equat = "y=%.2fx+%.2f"%(z[0],z[1])

    #getting R2
    yhat = p(sorted_x_axis)
    ybar = np.sum(sorted_avg_temp)/len(sorted_avg_temp)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((sorted_avg_temp - ybar)**2)
    R2 = round(ssreg / sstot,2)
    plt.plot([], [], ' ', label= "R2 of: " +str(R2))

    #plotting trendline
    plt.plot(sorted_x_axis,p(sorted_x_axis),"r--", label = "Trendline: "+equat)


    #plotting sorted x axis v average body temperature
    plt.plot(sorted_x_axis, sorted_avg_temp, 'bo-', label = "Body Temperature (%)")
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
                    rotation = 45,
                    ha='center') # horizontal alignment can be left, right or center

    plt.legend()

    plt.savefig('docs/assets/' + graph_save_name +'.png',bbox_inches='tight')

    save_list = [R2,equat]

    write_data(save_list,temp_save_name)



for i in range(len(x_ax_names)):
    create_plots(master_list[i], x_ax_names[i], graph_save_names[i],temp_data_names[i])


#constructing 3D plot of quadratic regression

Ci, Cw, Cl, Cw2, Clw, Cl2, quad_int, r2_quad = list(map(float, open('temp_data/ML_data_quad.txt', 'r').read().splitlines()))

fig = plt.figure()
ax = plt.axes(projection='3d')

L = np.linspace(min(no_layers), max(no_layers), len(no_layers))
wea = np.linspace(min(avg_weather), max(avg_weather), len(avg_weather))

lay, WEA = np.meshgrid(L, wea)


bt = Ci + WEA*Cw +lay*Cl + (lay**2)*Cl2 + Clw*WEA*lay + Cw2*(WEA**2) + quad_int

ax.plot_wireframe(lay, WEA, bt, color='black')
ax.set_title('Wireframe Plot of Quadratic Regression');

ax.set_ylabel('Weather (C)')
ax.set_xlabel('Number of Layers')
ax.set_zlabel('Body Temperature (%)');

ax.scatter3D(no_layers, avg_weather, avg_temp)

plt.savefig('docs/assets/quad_regr.png')


#Constructing graphs of linear regression and quadratic regression

coef_weather, coef_layers, intercept, score = list(map(float, open('temp_data/ML_data.txt', "r").readlines()))

fig = plt.figure()

desired_temp = 1.2

wea_range = np.linspace(-15,35,40)

a = Cl2

b = Clw*wea_range + Cl

c = Ci + Cw*wea_range + Cw2*wea_range**2+quad_int-desired_temp

L1 = (-b+((b**2)-4*a*c)**0.5)/(2*a)

L2 = (-b-((b**2)-4*a*c)**0.5)/(2*a)

lin = (desired_temp-coef_weather*wea_range-intercept)/coef_layers

plt.plot(wea_range, L1, label='Quad Reg 1')

plt.plot(wea_range,L2, label='Quad Reg 2')

plt.plot(wea_range,lin, label='Linear Reg')

plt.scatter(avg_weather,no_layers)

plt.legend()

plt.xlabel('Weather')

plt.ylabel('Number of Layers')

plt.title('Regression for body temperature of '+ str(desired_temp)+'x optimal')

plt.savefig('docs/assets/reg_charts.png')