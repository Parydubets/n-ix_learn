from datetime import datetime, timedelta

def current_date_time(timezone):

    return (datetime.now()+timedelta(hours=timezone)).strftime("[%H:%M:%S] - %w, %B of %Y")

print(current_date_time(0))
print(current_date_time(2))
print(current_date_time(-2))