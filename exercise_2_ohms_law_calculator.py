# Add introduction header centered with dashes
print(" Ohm's Law Calculator ".center(50, "-"))

# Display calculation options for user.
print("\nV for Voltage")
print("I for Current")
print("R for Resistance")

# Taking user's selection for what they want to calculate
selection = str(input("\n Please select what you want to calculate (V, I, or R): ").capitalize())

# If the user chooses to calculate Voltage (V)
if selection == 'V':
    current = float(input("\nEnter the value for Current(I): "))
    resistance = float(input("\nEnter the value for Resistance(R): "))
    voltage = current * resistance

    if voltage == '1':
        print(f"\nThe value of Voltage(V): {voltage} volt")
    else:
        print(f"\nThe value of Voltage(V): {voltage} volts")

# If the user chooses to calculate Current (I)
elif selection == 'I':
    voltage = float(input("\nEnter the value for Voltage(V): "))
    resistance = float(input("Enter the value for Resistance(R): "))

    if resistance == 0:
        print("Invalid input. Resistance cannot be zero. Please try again.")
    else:
        current = voltage / resistance
        print(f"The value for Current(I): {current} amperes")

# If the user chooses to calculate Resistance (R)
elif selection == 'R':
    voltage = float(input("\nEnter the value for Voltage(V): "))
    current = float(input("Enter the value for Current(I): "))

    if current == 0:
        print("Invalid input. Current cannot be zero. Please try again.")
    else:
        resistance = voltage / current
        print(f"The value for Resistance(R): {resistance} ohms")

# Handling invalid user input
else:
    print("Invalid input. Please enter either (V, I, or R).")