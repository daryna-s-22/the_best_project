from pandas import read_csv


def read_input_from_console():
    """
    Reads text from the console.

    Returns:
        str: The text entered by the user.

    """
    return input("Enter text: ")


def read_input_from_file_with_using_built_in_features(filepath):
    """
    Reads text from a file using built-in Python capabilities.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        str: The contents of the file.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def read_input_from_file_with_using_pandas(filepath):
    """
    Reads text from a file using the pandas library.

    Args:
        filepath (str): The path to the CSV file to be read.

    Returns:
        str: The contents of the file formatted as a string.
    """
    return read_csv(filepath, header=None).to_string(index=False)




