 #if both x and y == 0 it means that it is on the origin 

#Intialization
x, y = 1, 1

#loop until user enters 0, 0 for origin
# ask the user to input x and y coordinates

while x != 0 or y != 0:
  coordinates =(input("Enter x and y(press space in between the numbers): "))

#split and convert to float

  x, y = coordinates.split()
  x = float(x)
  y = float(y)
  print(f"Enter x and y: {x:.2f}   {y:.2f}")

#if x == 0, it means that the coordinate lies on y axis
  if (x == 0 and y != 0):
    print(f"==> ({x:.2f}, {y:.2f}) is at Y-axis")

#if y == 0 it means that the coordinate lies on the x axis
  elif (x != 0 and y == 0):
    print(f"==> ({x:.2f}, {y:.2f}) is at X-axis")

#if both numbers for x and y are >0, it belongs to the first quadrant
  elif (x > 0 and y > 0):
    print(f"==> ({x:.2f}, {y:.2f}) is above X-axis")
    print("==> It is at first quadrant")

#if both numbers for x and y are <0, it belongs to the third quadrant
  elif (x < 0 and y < 0):
    print(f"==> ({x:.2f}, {y:.2f}) is below X-axis")
    print("==> It is at third quadrant")

#if x is >0 (positive), y is <0 (negative), it belongs to the second quadrant
  elif (x > 0 and y < 0):
    print(f"==> ({x:.2f}, {y:.2f}) is below X-axis")
    print("==> It is at forth quadrant")

#if x is <0 (negative), y is >0 (positive), it belongs to the forth quadrant
  elif (x < 0 and y > 0):
    print(f"==> ({x:.2f}, {y:.2f}) is above X-axis")
    print("==> It is at second quadrant")

#loop ends when user entered 0, 0 
if (x == 0 and y == 0):
   print(f"==> ({x:.2f}, {y:.2f}) is at orgin")

input("Press enter to terminate")