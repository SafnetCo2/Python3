def main():
    fahrenheit_temps = [70, 71, 75, 80, 83, 85]
    
    # Print the Fahrenheit temperatures
    print(f"Fahrenheit: {fahrenheit_temps}")
    
    # Convert each Fahrenheit temperature to Celsius temperatures
    celsius_temp = []
    for f in fahrenheit_temps:
        c = celsius_temp(f)
        celsius_temp.append(c)
    
    # Print Celsius temperatures
    print(f"Celsius: {celsius_temp}")

def celsius_temp(f):
    """
    Convert fahrenheit to celsius
    """
    c = (f - 32) * 5 / 9
    return round(c, 1)

# Call the main function
main()
