""" Cornice services.
"""
from cornice import Service
import random

from sensors import get_distance

hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    #height will be between 50cm and 200cm
    #distance is distance from sensor (100cm to 50cm)
    height = random.randint(1, 100)
    distance = random.randint(1, 100)
    distance = get_distance()
    return {'data_height': height, 'data_distance': distance}
