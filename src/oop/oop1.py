# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base vehicle class:
class Vehicle:
    pass


# Vehicle subtype classes:
class GroundVehicle(Vehicle):
    pass


class FlightVehicle(Vehicle):
    pass


# Ground type vehicle classes:
class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


# Flight type vehicle classes:
class Starship(FlightVehicle):
    pass


class Airplane(FlightVehicle):
    pass
