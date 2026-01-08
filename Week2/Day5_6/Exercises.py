# Instructions:
# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
# Use the Cat class to create three cat objects with different names and ages.
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Kory", 0.5)
cat2 = Cat("Leia", 18)
cat3 = Cat("Randomxd", 6.7)

def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return print(f"“The oldest cat is {cat1.name}, and is {cat1.age} years old.”")
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return print(f"“The oldest cat is {cat2.name}, and is {cat2.age} years old.”")
    else:
        return print(f"“The oldest cat is {cat3.name}, and is {cat3.age} years old.”")


# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.
# Create davids_dog and sarahs_dog objects with their respective names and heights.
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("Lassy", 40)
sarahs_dog = Dog("Princesa", 45)

print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()


# Instructions:
# Create a Song class with a method to print song lyrics line by line.
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)
    
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# Create a Zoo class to manage animals. 
# The class should allow adding animals, 
# displaying them, selling them, and organizing them into alphabetical groups.

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        animal_sorted = {}
        for animal in sorted(self.animals):
            first_letter = animal[0].upper()
            if first_letter not in animal_sorted:
                animal_sorted[first_letter] = []
            animal_sorted[first_letter].append(animal)
        return animal_sorted
    def get__groups(self):
        animal_groups = self.sort_animals()
        for letter, animals in animal_groups.items():
            print(f"{letter}: {', '(animals)}")

myzoo = Zoo("Parque de las leyendas")
myzoo.add_animal("Puma")
myzoo.add_animal("Zorro")
myzoo.add_animal("Lobo")
myzoo.get_animals()
myzoo.sell_animal("Zorro")
myzoo.sort_animals()
myzoo.get__groups()
