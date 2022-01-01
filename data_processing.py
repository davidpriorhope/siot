'''To do in this script:

- Multi-dimensional linear regression
    - R value for the correlation of layers to body temperature

'''
from sklearn import linear_model
import numpy as np

#extracting data sets from temporary files
avg_temp = list(map(float, open('temp_data/summary_avg_temp.txt', "r").read().splitlines()))        #dependent variable
avg_weather = list(map(float, open('temp_data/summary_avg_weather.txt', "r").read().splitlines()))  #independent variable
no_layers = list(map(float, open('temp_data/summary_no_layers.txt', "r").read().splitlines()))      #independent variable


X = np.column_stack((avg_weather,no_layers))    #independent variables
y = np.c_[avg_temp]                             #dependent variables


#fitting a linear regression
regr = linear_model.LinearRegression()
regr.fit(X, y)

coef_weather = regr.coef_.tolist()[0][0]
coef_layers = regr.coef_.tolist()[0][1]
intercept = float(regr.intercept_)

score = regr.score(X,y)

#writing out useful variables to temporary file

ML_data = [coef_weather,coef_layers,intercept,score]

textfile = open('temp_data/ML_data.txt', "w")
for i in ML_data:
    textfile.write(str(i) + "\n")
textfile.close()

#Testing predicting number of layers:
'''print('Score: ' +str(score))

current_weather = 11
desired_temp_per = 1
test_no_layers = 2
suggested_no_layers = int((desired_temp_per-coef_weather*current_weather-intercept)/coef_layers)

print('At ' + str(current_weather) + ' degrees, wearing ' + str(test_no_layers) + ' layers, it is estimated your body will reach: '+ str(float(current_weather*coef_weather+test_no_layers*coef_layers+intercept)) + ' % of its optimal temperature')

print('For outdoor temperature of '+str(current_weather)+ ' you should wear '+ str(suggested_no_layers)+' layers to be at your desired temperature.')'''