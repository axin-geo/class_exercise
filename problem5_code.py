
# Example function calls:
#convert_units(4, 'pound','kilogram') should return 1.81
#convert_units(2, 'mile', 'kilometer') should return 3.22


#3. The only permissible conversions are listed below. Any other attempted conversion should throw an
#exception of type Exception.
#pound → kilogram, with 1 pound = 0.45kg
#mile → kilometer, with 1 mile = 1.61km
#fahrenheit → celsius, with C = 5/9(F-32)
#gallon → liter, with 1 gallon = 3.79 liters

def convert_units(amount, us_unit, metric_unit):
    #1. amount is a nonnegative number of types float or integer. If not, the function should throw an
    #exception of type Exception
    if not isinstance(amount, (int, float)) or amount < 0:
        raise Exception("Amount must be a nonnegative number.")
    
    #2. us unit and metric unit are strings. If not, the function should throw an exception of type Exception
    if not isinstance(us_unit, str) or not isinstance(metric_unit, str):
        raise Exception("Unit descriptions must be strings.")
    
    # Define conversion factors as required, key pair dic
    conversions = {
        ('pound', 'kilogram'): 0.45,
        ('mile', 'kilometer'): 1.61,
        ('fahrenheit', 'celsius'): lambda x: (x - 32) * 5 / 9,
        ('gallon', 'liter'): 3.79
    }
    
    # Check if the input conversion is suupoorted
    conversion_factor = (us_unit, metric_unit)
    if conversion_factor not in conversions:
        raise Exception("The requested conversion is not supported.")
    
    # Make the conversion
    converter = conversions[conversion_factor]
    if callable(converter):  # Check if the converter is a function (for temperature)
        return round(converter(amount), 2)
    else:
        return round(amount * converter, 2)

print(convert_units(1, 'mile', 'kilometer'))