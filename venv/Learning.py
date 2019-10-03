# Octothorp
print("A FEW THINGS")
# tells me true or false
print(5 < 3)
# whole number
print(float(9 / 8))
# floating point whole number
print(float(9 / 9))

print(6 + 9 + 4 + 20 / 6 - 9)
# intiger
print(9 / 8)



# variable
cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers/cars_driven

print("There are", cars,"cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can trasnport", carpool_capacity,"people today.")
print("We have", passengers,"passengers to carpool today")
print("We need to put about", average_passengers_per_car,"people in each car")

myName = "Mr. Black"
myAge = 257
myHeight = 70
myEyes = "brown"
myTeeth = "white"
myHair = "yes, some"

print("Lat's talk about %s." % myName)
print("He's %d inches tall." % myHeight)
print("He's got %s eyes and %s hair." % (myEyes, myHair))
print("His teeth \tare usually %s depending \n on the coffee." % myTeeth)
print("If I add %d and %d, I get %d." % (myAge, myHeight, myAge + myHeight))