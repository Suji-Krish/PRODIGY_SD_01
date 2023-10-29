def convert_temperature(temperature, original_unit):
  """Converts a temperature from one unit to another.

  Args:
    temperature: The temperature value to convert.
    original_unit: The original unit of measurement.

  Returns:
    A tuple of the converted temperature values in Celsius, Fahrenheit, and Kelvin.
  """

  if original_unit == "C":
    fahrenheit = (temperature * 9 / 5) + 32
    kelvin = temperature + 273.15
  elif original_unit == "F":
    celsius = (temperature - 32) * 5 / 9
    kelvin = (temperature + 459.67) * 5 / 9
  else:
    raise ValueError("Invalid original unit: {}".format(original_unit))

  return celsius, fahrenheit, kelvin


def main():
  """The main function."""

  temperature = input("Enter a temperature value: ")
  original_unit = input("Enter the original unit of measurement (C, F, or K): ")

  try:
    temperature = float(temperature)
  except ValueError:
    raise ValueError("Invalid temperature value: {}".format(temperature))

  celsius, fahrenheit, kelvin = convert_temperature(temperature, original_unit)

  print("Temperature in Celsius:", celsius)
  print("Temperature in Fahrenheit:", fahrenheit)
  print("Temperature in Kelvin:", kelvin)



