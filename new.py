
rpm=10000
wheelCir = 1.979 #meters
gearing= 55/14 #back over front
velocity = rpm/60 *wheelCir / gearing #in meters per second
speed = velocity*2.23694 #convert to mph
print (speed)