class Temperature:
    def __init__(self, temperature: float):
        self.set_temperature(temperature)

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5)+32
    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9
    def set_temperature(self, temperature: float):
        if (temperature <-273.15):
            pass
        self.temperature = temperature
temp = Temperature(-12)
print(temp.celsius_to_fahrenheit())
print(temp.fahrenheit_to_celsius())

temp2 = Temperature(-300)







        # print(f'Температура Фаренгейта {celsius_to_fahrenheit(self)}')
        # print(f'Температура Фаренгейта { fahrenheit_to_celsius(self)}')