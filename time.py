#Forming Data
totalseconds = 7340
hours = 0
minutes = 0
seconds = 0
#Initializing while loop
while totalseconds >= 3600:
    hours += 1
    totalseconds -= 3600
while totalseconds >= 60:
    minutes += 1
    totalseconds -= 60
seconds = totalseconds
#printing the final output
print(f"Time: {hours} hours, {minutes} minutes, {seconds} seconds")
 # type: ignore