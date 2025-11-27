

#or

temp = 25 
is_raining = False


if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")




#and


temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY also")
elif temp <= 0 and is_sunny:
    print("Its COLD")
    print("its SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("Its WARM")
    print("Its SUNNY")
    
    
#not



temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY also")
elif temp <= 0 and is_sunny:
    print("Its COLD")
    print("its SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("Its WARM")
    print("Its SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is SUNNY also")
elif temp <= 0 and is_sunny:
    print("Its COLD")
    print("its SUNNY")
elif temp < 28 and temp > 0 and not is_sunny:
    print("Its WARM")
    print("Its SUNNY")