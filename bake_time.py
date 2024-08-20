# Definición que calcula el tiempo de horneado

# Definir variable constante para tiempo de horneado
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    return PREPARATION_TIME_LAYER * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return PREPARATION_TIME_LAYER * number_of_layers + elapsed_bake_time 


    """Calculate the elapsed cooking time.
    
    :param number_of_layers: int - the number of layers in the lasagna.
    :param: elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    
    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spente cooking
    the lasagna.
    """




    