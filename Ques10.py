# Q10. Write a python script to print the current date and time. First Create a variable to store the date and time,
# then display the date and time in a proper foramat.?
from datetime import datetime
dt=datetime.now()
d1=dt.strftime("%d-%m-%Y and %I:%M:%S %p")
print(d1)