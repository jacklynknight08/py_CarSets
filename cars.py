print("Car Sets Exercise")

# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("Jeep Cherokee")
showroom.add("Mitsubishi Lancer")
showroom.add("Ford Explorer")
showroom.add("Subaru Outback")

# Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add("Jeep Cherokee")

# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

# Using update(), add two more car models to your showroom with another set.
showroom.update({"Ford Mustang", "Chevrolet Impala"})

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Subaru Outback")
print(showroom)

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = set()
junkyard.add("Nissan Sentra")
junkyard.add("Chevrolet Impala")
junkyard.add("Volkswagen Beetle")
junkyard.add("Toyota Rav4")

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
cars = junkyard.intersection(showroom)
print(cars)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
new_cars = showroom.union(junkyard)
print(new_cars)

# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
new_cars.discard("Toyota Rav4")
print(new_cars)