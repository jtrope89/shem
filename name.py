from base import Base
import random
import logging
import re
import ipdb

class Name(Base):
    def __init__(self, file_name="full_names.txt"):
        super(Name, self).__init__()
        self.names = self.get_file_data(file_name)

    def name(self):
        """ return a random full name from data """
        return self.names[ self.generate_rand_num(self.names) ]

    def first_name(self):
        name_components = self.split_name()
        """ filter out nonsensical names such as Dr, Mrs, etc."""
        return [component for component in name_components if not component in self.prefixes][0]

    def suffix(self):
        return random.choice(self.suffixes)

    def prefix(self):
        return random.choice(self.prefixes)

    def last_name(self):
        potential_last_name = self.split_name()[-1]
        if potential_last_name in self.suffixes:
            return self.last_name()
        return potential_last_name

    def split_name(self):
        return self.name().split()

    def generate_rand_num(self, array):
        """Generates a random integer in the range of 0 and
        the length of the parameter - 1)"""
        return random.randint(0, len(array) - 1)
