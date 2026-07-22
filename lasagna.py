"""Functions used in preparing Guido's gorgeous lasagna.
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATAION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# Multiply the number of layers with preparation time that has been set on the top
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes based on the number of layers."""
    return number_of_layers * PREPARATAION_TIME

#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
