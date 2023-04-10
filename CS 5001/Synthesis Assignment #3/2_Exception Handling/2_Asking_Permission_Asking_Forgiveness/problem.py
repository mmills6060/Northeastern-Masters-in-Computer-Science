# Michael Arthur Mills
# April 7. 2023
# CS 5001

# The solution to the code that implements the "asking permission" approach to exception handling.



import math

def calculate_brightness(distance, luminosity, apparent_magnitude):
    # Validate input
    if not isinstance(distance, (int, float)) or distance <= 0:
        raise ValueError("Distance must be a positive number.")
    if not isinstance(luminosity, (int, float)) or luminosity <= 0:
        raise ValueError("Luminosity must be a positive number.")
    if not isinstance(apparent_magnitude, (int, float)):
        raise ValueError("Apparent magnitude must be a number.")

    # Calculate the star's absolute magnitude using the distance modulus equation
    absolute_magnitude = -2.5 * math.log10(luminosity) + 5 * math.log10(distance) + 5

    # Calculate the brightness of the star using the magnitude equation
    brightness = luminosity / (4 * math.pi * (distance * 3.086e+16) ** 2) * 10 ** (-0.4 * apparent_magnitude)

    return brightness

try:
    # Set the star's distance in parsecs
    distance = 10

    # Set the star's intrinsic luminosity in solar units
    luminosity = 5

    # Set the apparent magnitude of the star (as observed from Earth)
    apparent_magnitude = 4

    # Calculate the brightness of the star
    brightness = calculate_brightness(distance, luminosity, apparent_magnitude)

    print("The brightness of the star is", brightness, "watts per square meter.")

except ValueError as e:
    print("Error:", str(e))
except Exception as e:
    print("An unexpected error occurred:", str(e))



