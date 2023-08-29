class Currency:
    currencies = {
        'CHF': 0.930023, # Swiss franc 
        'CAD': 1.264553, # Canadian dollar
        'GBP': 0.737414, # British pound
        'JPY': 111.019919, # Japanese yen
        'EUR': 0.862361, # Euro
        'USD': 1.0 # US dollar
    }
      
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        self.value = (self.value / Currency.currencies[self.unit]) * Currency.currencies[new_unit]
        self.unit = new_unit

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __iadd__(self, other):
        result = self + other
        self.value, self.unit = result.value, result.unit
        return self

    def __radd__(self, other):
        result = self + other
        if self.unit != "USD":
            result.changeTo("USD")
        return result

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            converted_value = other / Currency.currencies["USD"] * Currency.currencies[self.unit]
            return Currency(self.value - converted_value, self.unit)
        
        temp_value = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return Currency(self.value - temp_value, self.unit)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            converted_value = other / Currency.currencies["USD"] * Currency.currencies[self.unit]
            return Currency(self.value + converted_value, self.unit)
        
        temp_value = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return Currency(self.value + temp_value, self.unit)

    def __isub__(self, other):
        result = self - other
        self.value, self.unit = result.value, result.unit
        return self

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            converted_value = other / Currency.currencies["USD"] * Currency.currencies[self.unit]
            return Currency(converted_value - self.value, self.unit)

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)  # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3)  # an int or a float is considered to be a USD value
print(30 - v2)