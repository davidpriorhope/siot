#Hello this is the main file which should be run for each cycle

#sense
exec(open("./sense.py").read())

#upload data
exec(open("./upload.py").read())

#Create website assets:
    #Read data 
    #Do processing (multi-dimensional linear regression)
        #this includes calculating the number of layers to cycle right now
    #build chart

exec(open("./chart_build.py").read())
exec(open("./daily_chart_build.py").read())
print('Generated charts')


#pushing updated files to github
exec(open("./push_to_github.py").read())