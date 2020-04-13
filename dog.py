class Dog:
    species="mammal"

    def __init__(self, dog_name, dog_age):
        self.name = dog_name
        self.age = dog_age

        # __ is private member
        # public member
        # _ is protected member

    def description(self):
        return "{} is {} yrs old.".format(self.name, self.age)