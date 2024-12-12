base = input("Enter the base amount and press enter: ")
height = input("Enter the height amount and press enter: ")

# Ensure the inputs are converted to integers safely.
try:
    base = int(base)
    height = int(height)
    print("Length of height: " + str(height))
    print("Length of base: " + str(base))
    print("The perimeter (circumference) is: " + str(2 * (base + height)))
except ValueError:
    print("Please enter valid numbers for base and height.")





def circumference(base, height):
    print("Length of height: " + str(height))
    print("Length of base: " + str(base))
    print("The perimeter (circumference) is: " + str(2 * (base + height)))

# Example call to the function
circumference(3, 4)
