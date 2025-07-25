import json
from datetime import date

# Format as mm/dd/yy
#formatted_date = now.strftime("%m/%d/%y")

class Expense:
    _id_counter = 1

    def __init__(self, description, amount):
        self.id = Expense._id_counter
        Expense._id_counter += 1

        self.description = description
        self.amount = amount
        # Grab the date of the expense
        self.date = date.today()


    # Sets description for expense
    def set_description(self, description):
        self.description = description
    # Sets amount for expense
    def set_amount(self, amount):
        self.amount = amount

    # Prints expense details
    def print_details(self):
        print(f'# ID {self.id} {self.date} {self.description} {self.amount}')

    def to_dict(self):
        return {"ID": self.id, "Date": self.date.isoformat(), "description": self.description, "amount": self.amount}

    # Saves object to json
    def save(self, filepath):
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f)

    # Loads object from json
    @classmethod
    def from_dict(cls, data):
        obj = cls(data["description"], data["amount"])
        obj.id = data["ID"]
        obj.date = date.fromisoformat(data["Date"])
        return obj