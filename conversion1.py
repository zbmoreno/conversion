speed = input("Please enter a speed in miles/hour: ")
floatSpeed = float(speed)
print("Original speed in miles/hour: {}".format(floatSpeed))
conversion1 = (floatSpeed * 190080) * 24
print("Converted to barleycorn/day is: {}".format(conversion1))#7.99998
conversion2 = (floatSpeed * 7.99998 ) * 336
print("Converted to furlongs/fornight is: {}".format(conversion2))#7.99998
conversion3 = (floatSpeed * 1.46667) / 1130
print("Converted to Mach number is: {}".format(conversion3))#0.44704
conversion4 = (floatSpeed * 0.44704) / 299792458
print("Converted to the percentage of speed of light is: {}".format(conversion4))