from cowin_api import CoWinAPI
state_id = '21'
cowin = CoWinAPI()
districts = cowin.get_districts(state_id)
print(districts)



