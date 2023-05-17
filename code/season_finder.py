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