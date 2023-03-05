x = int(input("Enter the day of the week: "))

import datetime

x = datetime.datetime.weekday()

print(x.strftime("%w"))
