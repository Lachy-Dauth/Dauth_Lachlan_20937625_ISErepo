def tempurature_difference(temp, mean_temp):

    temp_word = ""
    diff = abs(temp - mean_temp)

    if temp > mean_temp:
        temp_word = "hotter"
    else:
        temp_word = "colder"

    if diff > 5:
        return f"It is {temp} degrees outside, {diff} degrees {temp_word} than the mean tempurature, {mean_temp}."
    else:
        return f"It is {temp_word} than the mean tempurature."
        

def tempurature_finder(tempurature_str, city_str, time_str):
    
    tempurature_dict = {
        "perth" : {
            "morning" : 18.2,
            "afternoon" : 23
        },
        "adelaide" : {
            "morning" : 16.5,
            "afternoon" : 21
        }
    }

    temp = float(tempurature_str)
    time_code = time_str.lower()
    city_code = city_str.lower()

    mean_temp = tempurature_dict[city_code][time_code]

    print(tempurature_difference(temp, mean_temp))

