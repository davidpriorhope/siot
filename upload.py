from googleapiclient import discovery
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

#setup & configuration
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Documents/siot_testing/credentials.json', scope) 

client = gspread.authorize(credentials)

service = discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id = '1IcC5hPXw8ORDOmnVjd2q9RmzlfLSnAmwbr5Rk7N6taQ' # The spreadsheet to apply the updates to.


#setting up sampling frequency
#samp_freq = 0.5 #this is actually time between samples, not frequency

#creating an avergae function which we will call later!
def average(input_list):
    avg = sum(input_list)/len(input_list)
    return avg



#creating name for new sheet
new_sheet = datetime.datetime.now().strftime('%d.%m.%y')

def new_tab(): #creating a new tab
    batch_update_spreadsheet_request_body = {
        # A list of updates to apply to the spreadsheet.
        # Requests will be applied in the order they are specified.
        # If any request is not valid, no requests will be applied.
        'requests': [{
            "addSheet": {
                'properties': {
                    'title': new_sheet
                    }
            }
        }] 
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
    response = request.execute()



num_layer = input('How many layers are you wearing? ')  #asking number of layers + publishing to spreadsheet


time_list = open('temp_data/time.txt', "r").read().splitlines()
temp_list_raw = open('temp_data/temp_raw.txt', "r").read().splitlines()
temp_list_perc = list(map(float, open('temp_data/temp_per.txt', "r").read().splitlines()))
weather_list = list(map(float, open('temp_data/weather.txt', "r").read().splitlines()))
master_list = []

def compile():
    #compiling master_list
    for i in range(len(time_list)):
        master_list.append([time_list[i],temp_list_raw[i],temp_list_perc[i],weather_list[i]])



def upload():
    print('Uploading data')
    #appending the data to the new sheet
    resource = {
    "majorDimension": "ROWS",
    "values": master_list
    }
    sheet_range = new_sheet+"!A:D";
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range= sheet_range,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()
    

    #getting averages
    avg_temp_perc = average(temp_list_perc)
    avg_weather = average(weather_list)

    
    #updating summary sheet
    resource = {
    "majorDimension": "ROWS",
    "values": [[new_sheet,avg_temp_perc,avg_weather,num_layer]]
    }
    summary_range = 'Summary!A:D';
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=summary_range,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()

    print('All data successfully uploaded!')

try:
    new_tab()
except:
    print('Tab with '+ str(new_sheet) + 'already exists.')

compile()
upload()