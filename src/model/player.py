import pickle


class Player:

    def __init__(self, name, color):
        self.name = name
        self.color = color
        # All ants the player owns.
        self.ants = set()

    def store_data(self):
        """stores the data of a player in a pickle file"""
        pickle.dump(self, open(str(self.name) + ".p", "wb"))

    def read_data(self, filename):
        """reads the data of a player from a pickle file"""
        loaded = pickle.load(open(filename, "rb"))
        self.__dict__ = loaded.__dict__
