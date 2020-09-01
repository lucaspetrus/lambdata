import pandas as pd


# pd.DataFrame is the DataFrame class
# You can make children of classes you didn't write!
# As an exercise, try to use and/or build on this
class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class BareMinimumClass:
    pass


class Complex:
    def __init__(self, realpart, imagpart):
        """
        This is called the Constructor for complex numbers.
        Complex numbers are part real, and part imaginary.
        Imaginary numbers are roots of negative numbers
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)


num1 = Complex(3, -5)
num2 = Complex(-1, 6)
num1.add(num2)  # what should num1 be after?
print(num1.r, num1.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvote(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """Parent Class"""
    """General representation of animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + ' is delicious, yum!'


class Tiger(Animal):
    """Child Class"""
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = int(num_stripes)

    def say_great(self):
        return "It's GREEEEEEAATTT"

    def run(self):
        # Overriding run to be different for Tigers
        return 'Scamperwoose'


if __name__ == '__main__':
    # Demo code if you run python oop_examples.py
    # Example 0
    b = BareMinimumClass
    # Example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2) # What should num1 be after?
    # Example 2
    user1 = SocialMediaUser('Erle', 'Jax')
    user2 = SocialMediaUser('John', 'New York')
    user3 = SocialMediaUser('John Doe', 'Anytown, USA')
    print(user2.is_popular())  # False
    for _ in range(75):
        user2.receive_upvote()
    print(user2.is_popular())  # True (but it printed out false...)
