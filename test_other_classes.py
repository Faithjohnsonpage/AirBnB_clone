#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Reload all objects from storage
storage.reload()

# Test State class
print("-- Create a new State --")
my_state = State()
my_state.name = "California"
my_state.save()
print(my_state)

# Test City class
print("-- Create a new City --")
my_city = City()
my_city.state_id = my_state.id
my_city.name = "San Francisco"
my_city.save()
print(my_city)

# Test Amenity class
print("-- Create a new Amenity --")
my_amenity = Amenity()
my_amenity.name = "Wifi"
my_amenity.save()
print(my_amenity)

# Test Place class
print("-- Create a new Place --")
my_place = Place()
my_place.city_id = my_city.id
my_place.user_id = "user_id"
my_place.name = "Cozy Apartment"
my_place.description = "A cozy apartment in the heart of the city."
my_place.number_rooms = 2
my_place.number_bathrooms = 1
my_place.max_guest = 4
my_place.price_by_night = 100
my_place.latitude = 37.7749
my_place.longitude = -122.4194
my_place.amenity_ids = [my_amenity.id]
my_place.save()
print(my_place)

# Test Review class
print("-- Create a new Review --")
my_review = Review()
my_review.place_id = my_place.id
my_review.user_id = "user_id"
my_review.text = "Great place to stay!"
my_review.save()
print(my_review)
