#update Java script variables
coef_weather, coef_layers, intercept, score = open('temp_data/ML_data.txt', "r").readlines()

lines = open('docs/app.js', "r").readlines()

with open('docs/app.js', "w") as f:
    for line in lines:
        if "const coef_weather" in line:
            line = "const coef_weather = " + str(float(coef_weather))+ ';\n'

        elif "const coef_layer = " in line:
            line = "const coef_layer = " + str(float(coef_layers))+ ';\n'
        
        elif "const int" in line:
            line = 'const int = '+ str(float(intercept))+';\n'

        elif "const score = " in line:
            line = "const score = "+str(float(score))+ ';\n'

        f.write(line)


#update carosel

