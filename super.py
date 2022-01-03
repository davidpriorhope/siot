#Hello this is the main file which should be run for each cycle


#sense
exec(open("./sense.py").read())

#upload data
exec(open("./upload.py").read())

#reading summary data from google sheets
exec(open("./read_gsheets.py").read())

#doing ML to process + correlate data
exec(open("./data_processing.py").read())

#building charts + getting equation + R2
exec(open("./chart_build.py").read())

#building new charts
exec(open("./append_new_chart.py").read())
print('Generated charts')

#updating HTML file
#exec(open("./update_html.py").read())

#pushing updated files to github
exec(open("./push_to_github.py").read())

print('The website changes are being deployed and the website should update in the next few minutes.')