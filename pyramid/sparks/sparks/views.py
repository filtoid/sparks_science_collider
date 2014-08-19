""" Cornice services.
"""
from cornice import Service
from pyramid.view import view_config
import random

from sensors import get_distance, get_distance_2

hello = Service(name='hello', path='/data', description="Simplest app", cors_origins=('*',))

@hello.get(cors_headers=('X-My-Header', 'Content-Type'))
def get_info(request):
    """Returns Hello in JSON."""
    #height will be between 50cm and 200cm
    #distance is distance from sensor (100cm to 50cm)
    height = 200 - get_distance_2()
    #height = random.randint(2, 20)
    distance = get_distance()
    #distance = random.randint(50, 195)
    return {'data_height': height, 'data_distance': distance}
