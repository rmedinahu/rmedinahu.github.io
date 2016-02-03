seconds = raw_input("Enter a large number of seconds: ")
seconds = int(seconds)

days = seconds / 86400
seconds = seconds % 86400
hours = seconds / 3600
seconds = seconds % 3600
mins = seconds / 60
seconds = seconds % 60

print days, 'days', hours, 'hours', mins, 'minutes', seconds, 'seconds'