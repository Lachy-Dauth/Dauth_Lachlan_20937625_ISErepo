import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def month_to_code(month_str):
    """
    Converts a month string to its corresponding numerical code.

    Parameters:
    month_str (str): A string representing a month, e.g. "January", "feb".

    Returns:
    int: The numerical code for the month, e.g. 1 for "January", 2 for "February", etc.

    Raises:
    ValueError: If month_str is not a valid month format.
    """

    # A dictionary of month formats and their corresponding numerical codes.
    month_formats = {
        "jan": 1,
        "january": 1,
        "feb": 2,
        "february": 2,
        "mar": 3,
        "march": 3,
        "apr": 4,
        "april": 4,
        "may": 5,
        "jun": 6,
        "june": 6,
        "jul": 7,
        "july": 7,
        "aug": 8,
        "august": 8,
        "sep": 9,
        "sept": 9,
        "september": 9,
        "oct": 10,
        "october": 10,
        "nov": 11,
        "november": 11,
        "dec": 12,
        "december": 12
    }

    # Convert month_str to lowercase for case-insensitive matching.
    month_str = month_str.lower()

    # Check if month_str is a valid month format.
    if month_str in month_formats:
        return month_formats[month_str]
    else:
        raise ValueError(f"Invalid month format: {month_str}")
    
def display_img(image_path):
    """
    Display an image using Matplotlib.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        None
    """

    # Load the image using matplotlib's imread function
    image = mpimg.imread(image_path)

    # Display the image using matplotlib's imshow function
    plt.imshow(image)

    # Hide the axis labels and ticks
    plt.axis('off')

    # Show the image
    plt.show()

def month_to_season(month_str, country_str):
    country_season = {
        "australia" : {
            1: "Summer",
            2: "Summer",
            3: "Autumn",
            4: "Autumn",
            5: "Autumn",
            6: "Winter",
            7: "Winter",
            8: "Winter",
            9: "Spring",
            10: "Spring",
            11: "Spring",
            12: "Summer"
        },
        "noongar" : {
            1: "Birak",
            2: "Bunuru",
            3: "Bunuru",
            4: "Djeran",
            5: "Djeran",
            6: "Makuru",
            7: "Makuru",
            8: "Djilba",
            9: "Djilba",
            10: "Kambarang",
            11: "Kambarang",
            12: "Birak"
        },
        "spain" : {
            1: "Winter",
            2: "Winter",
            3: "Spring",
            4: "Spring",
            5: "Spring",
            6: "Summer",
            7: "Summer",
            8: "Summer",
            9: "Autumn",
            10: "Autumn",
            11: "Autumn",
            12: "Winter"
        },
        "japan" : {
            1: "Winter",
            2: "Winter",
            3: "Spring",
            4: "Spring",
            5: "Spring",
            6: "Summer",
            7: "Summer",
            8: "Summer",
            9: "Autumn",
            10: "Autumn",
            11: "Autumn",
            12: "Winter"
        },
        "mauritius" : {
            1: "Summer",
            2: "Summer",
            3: "Summer",
            4: "Summer",
            5: "Autumn",
            6: "Winter",
            7: "Winter",
            8: "Winter",
            9: "Winter",
            10: "Spring",
            11: "Summer",
            12: "Summer"
        },
        "sri lanka" : {
            1: "Northeast Monsoon",
            2: "Northeast Monsoon",
            3: "Inter-Monsoon",
            4: "Inter-Monsoon",
            5: "Southeast Monsoon",
            6: "Southeast Monsoon",
            7: "Southeast Monsoon",
            8: "Southeast Monsoon",
            9: "Southeast Monsoon",
            10: "Inter-Monsoon",
            11: "Inter-Monsoon",
            12: "Northeast Monsoon"
        },
        "malaysia" : {
            1: "Northeast Monsoon",
            2: "Northeast Monsoon",
            3: "Inter-Monsoon",
            4: "Inter-Monsoon",
            5: "Southeast Monsoon",
            6: "Southeast Monsoon",
            7: "Southeast Monsoon",
            8: "Southeast Monsoon",
            9: "Southeast Monsoon",
            10: "Inter-Monsoon",
            11: "Inter-Monsoon",
            12: "Northeast Monsoon"
        },
    }