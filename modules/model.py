# just a dummy model, random output 0 or 1 (random guess)
import random

class Model:
    @staticmethod
    def predict(input_data):
        return random.randint(0, 1)   # return 0 or 1 randomly