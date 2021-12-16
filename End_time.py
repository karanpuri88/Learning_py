hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Issue duration (minutes): "))
new_hour = (hour + int((mins+dura)/60))
new_mins = (mins + dura)%60
if new_hour > 24 :
    new_hour1 = new_hour - 24
    print ("Next day End time :",new_hour1,":",new_mins)
if new_hour < 24:
    print ("Same day End time :",new_hour,":",new_mins)


