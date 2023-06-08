
# The leap year calculator

year =  int(input("Which year do want to check? "))

if year % 4 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not leap Year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Error!")
    