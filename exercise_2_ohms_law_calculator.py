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
    current = float(input('\nEnter the value for Current(I): '))
    resistance = float(input('\nEnter the value for Resistance(R): '))
    voltage = current * resistance

    if voltage == '1':
        print(f'\nThe value of voltage: {voltage} Volt')
    else:
        print(f'\nThe value of voltage: {voltage} Volts')

# If the user chooses to calculate Current (I)
# If the user chooses to calculate Resistance (R)
# Handling invalid user input
