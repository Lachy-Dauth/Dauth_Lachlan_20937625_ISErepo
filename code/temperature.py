def temperature_difference(temp, mean_temp):
    """
    Calculates the temperature difference between a given temperature and the mean temperature.

    Args:
        temp (float): The given temperature.
        mean_temp (float): The mean temperature.

    Returns:
        str: A formatted string describing the temperature difference.

    """
    temp_word = ""
    diff = abs(temp - mean_temp)

    if temp > mean_temp:
        temp_word = "hotter"
    else:
        temp_word = "colder"

    if diff > 5:
        return f"It is {temp} degrees outside, {diff} degrees {temp_word} than the mean temperature, {mean_temp}."
    else:
        return f"It is {temp_word} than the mean temperature."

def temperature_finder(temperature_str, city_str, time_str):
    """
    Finds the temperature difference between a given temperature and the mean temperature of a specific city and time period.

    Args:
        temperature_str (str): The given temperature.
        city_str (str): The name of the city.
        time_str (str): The time period (e.g., "morning" or "afternoon").

    """
    temperature_dict = {
        "perth": {
            "morning": 18.2,
            "afternoon": 23
        },
        "adelaide": {
            "morning": 16.5,
            "afternoon": 21
        }
    }

    temp = float(temperature_str)
    time_code = time_str.lower()
    city_code = city_str.lower()

    mean_temp = temperature_dict[city_code][time_code]

    print(temperature_difference(temp, mean_temp))

def input_temperature():
    """
    Get user input for the month and country, and call the month_to_season function.
    """

    # Prompt the user for the temperature, city and time
    temperature = input("Enter the temperature: ")
    city = input("Enter a city: ")
    time = input("Is it the morning or afternoon: ")

    # Call the temperature_finder function with user-provided values
    temperature_finder(temperature, city, time)

def main():
    input_temperature()

if __name__ == "__main__":
    main()