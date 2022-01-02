'''
- check google sheets to see tabs
- check local directory to see if charts already made
- for charts that are not built, build the chart'''

from googleapiclient import discovery
from os import listdir
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import gspread
import numpy as np

#setup & configuration
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Documents/siot_testing/credentials.json', scope) 
service = discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id = '1IcC5hPXw8ORDOmnVjd2q9RmzlfLSnAmwbr5Rk7N6taQ' # The spreadsheet to apply the updates to.
client = gspread.authorize(credentials)

#checking names of current google tabs
sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
sheets = sheet_metadata.get('sheets', '')


#creating a dictionary with elements as dates and keys as number of layers so that the data can quickly be accessed
no_layer_dict = {}

#here data of number of layers on each day is collected from the temporary files produced by read_gsheets.py
days_list = list(open('temp_data/summary_day.txt', "r").read().splitlines())
layer_list = list(open('temp_data/summary_no_layers.txt', "r").read().splitlines())

for i in range(len(days_list)):
    no_layer_dict[days_list[i]] = layer_list[i]


#creating function to generate charts
def chart_construct(time_list, temp_list, weather_list, cal_temp, no_layer, save_name, title):

    plt.figure()

    plt.plot([], [], ' ', label= str(no_layer)  + " layer(s) worn")

    plt.plot(time_list, temp_list,  color='b', label ="Body Temperature")

    plt.plot(time_list,weather_list,  color='g', label = "Weather Temperature")

    plt.axhline(cal_temp, color='r', label="Calibration Temperature")

    plt.xlabel('Time')

    plt.ylabel('Temperature (C)')

    plt.title(title)

    plt.legend()


    no_ticks = 10

    seperation = (len(time_list))/(no_ticks-1)

    tick_array = np.floor(np.arange(0, len(time_list)+1, step=seperation))

    tick_array[no_ticks-1]=len(time_list)-1

    plt.xticks(tick_array, rotation = 30)

    plt.savefig('docs/assets/'+save_name+'.png',bbox_inches='tight')

#creating function to read gsheets
def get_sheet_data(range_names):
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_names).execute()
    return result.get('values', [])


#this basically creates graphs for any which are missing in the cycle directory
for sheet in sheets:
    #getting name of sheet
    sheet_name = sheet.get("properties", {}).get("title")

    #checking if sheet has already been plotted, if not it will read the data from google sheets and plot the graph
    if sheet_name != 'Summary' and sheet_name+'.png' not in listdir('docs/assets/cycle'):

        master_list = [[],[],[],[]]

        #import sheet data
        for i in get_sheet_data(sheet_name+'!A:D'):
            for j in range(len(i)):
                master_list[j].append(str(i[j]))

        #get number of layers on that date using dictionary
        num_layer = no_layer_dict[sheet_name]

        #calculate calibration temperature
        cal_temp = float(master_list[1][0])/float(master_list[2][0])   

        #construct graph
        chart_construct(master_list[0],list(map(float, master_list[1])),list(map(float, master_list[3])),cal_temp,num_layer,'cycle/'+sheet_name,sheet_name)