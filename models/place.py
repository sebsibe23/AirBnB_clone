#!/usr/bin/python3
"""
Defines the Place class.

This module defines the Place class, which represents a place.

Attributes:
    city_id (str): The ID of the city where the place is located.
    user_id (str): The ID of the user who owns the place.
    name (str): The name of the place.
    description (str): The description of the place.
    number_rooms (int): The number of rooms in the place.
    number_bathrooms (int): The number of bathrooms in the place.
    max_guest (int): The maximum number of guests allowed in the place.
    price_by_night (int): The price per night for the place.
    latitude (float): The latitude coordinate of the place.
    longitude (float): The longitude coordinate of the place.
    amenity_ids (list): A list of IDs of amenities available in the place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of IDs of amenities available in the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
