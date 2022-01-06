'''To do in this script:

- Multi-dimensional linear regression
    - R value for the correlation of layers to body temperature

'''
from sklearn import linear_model
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

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

#writing out useful linear variables to temporary file

ML_data = [coef_weather,coef_layers,intercept,score]

textfile = open('temp_data/ML_data.txt', "w")
for i in ML_data:
    textfile.write(str(i) + "\n")
textfile.close()


#Now we will fit a quadratic regression

poly = PolynomialFeatures(degree=2)
poly_variables = poly.fit_transform(X)

quad_regr = linear_model.LinearRegression()
quad_model = quad_regr.fit(poly_variables, y)

quad_score = quad_model.score(poly_variables, y)

quad_coef = quad_model.coef_.tolist()[0]

quad_data = quad_coef + [float(quad_regr.intercept_),float(quad_score)]

quad_file = open('temp_data/ML_data_quad.txt', "w")

for i in quad_data:
    quad_file.write(str(i) + "\n")
quad_file.close()