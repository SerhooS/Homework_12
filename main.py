##########   Завдання 1
# Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни,
# кількість жителів міста, поштовий індекс міста, телефонний код міста. Реалізуйте доступ до окремих полів (Інкапсуляція).

# class City:
#     __country = "Ukraine"
#     __phone_code = "+380"
#
#     def __init__(self, name, region, population, postal_code):
#         self.name = name
#         self.region = region
#         self.population = population
#         self.postal_code = postal_code
#         self.country = self.__country
#         self.phone_code = self.__phone_code
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if 2 < len(name) < 30:
#             self.__name = name
#         else:
#             raise ValueError("Provide correct name!")
#
#     @property
#     def region(self):
#         return self.__region
#
#     @region.setter
#     def region(self, region):
#         if 2 < len(region) < 50:
#             self.__region = region
#         else:
#             raise ValueError("Provide correct region!")
#
#     @property
#     def population(self):
#         return self.__population
#
#     @population.setter
#     def population(self, population):
#         if 100 < population < 3000000:
#             self.__population = population
#         else:
#             raise ValueError("Provide correct population!")
#
#     @property
#     def postal_code(self):
#         return self.__postal_code
#
#     @postal_code.setter
#     def postal_code(self, postal_code):
#         if 2 < len(postal_code) < 20:
#             self.__postal_code = postal_code
#         else:
#             raise ValueError("Provide correct postal_code!")
#
#     def show_info(self):
#         print(f"City: {self.__name}\nRegion: {self.__region}\nCountry: {self.__country}\nPopulation: {self.__population}\n"
#               f"Postal code: {self.__postal_code}\nPhone code: {self.__phone_code}")
#
# try:
#     City1 = City("Dnipro", "Dnipropetrovsk region", 980000, "49000")
#     City2 = City("Kyiv", "Kyiv City", 2800000, "02000")
#     City3 = City("Lviv", "Lviv Region", 720000, "79000")
#     City1.show_info()
#     City2.show_info()
# except ValueError as error:
#     print(error)


###########   Завдання 2
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів країни,
# телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція).

# class Country:
#     def __init__(self, name, continent, population, phone_code, capital, cities):
#         self.name = name
#         self.continent = continent
#         self.population = population
#         self.phone_code = phone_code
#         self.capital = capital
#         self.cities = cities
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if 2 < len(name) < 20:
#             self.__name = name
#         else:
#             raise ValueError("Provide correct country name!")
#
#     @property
#     def continent(self):
#         return self.__continent
#
#     @continent.setter
#     def continent(self, continent):
#         if 2 < len(continent) < 20:
#             self.__continent = continent
#         else:
#             raise ValueError("Provide correct continent!")
#
#     @property
#     def population(self):
#         return self.__population
#
#     @population.setter
#     def population(self, population):
#         if 100 < population < 3000000000:
#             self.__population = population
#         else:
#             raise ValueError("Provide correct population!")
#
#     @property
#     def phone_code(self):
#         return self.__phone_code
#
#     @phone_code.setter
#     def phone_code(self, phone_code):
#         if 2 < len(phone_code) < 20:
#             self.__phone_code = phone_code
#         else:
#             raise ValueError("Provide correct phone_code!")
#
#     @property
#     def capital(self):
#         return self.__capital
#
#     @capital.setter
#     def capital(self, capital):
#         if 2 < len(capital) < 30:
#             self.__capital = capital
#         else:
#             raise ValueError("Provide correct capital!")
#
#     @property
#     def cities(self):
#         return self.__cities
#
#     @cities.setter
#     def cities(self, cities):
#         if isinstance(cities, list):
#             self.__cities = cities
#         else:
#             raise ValueError("Provide a list of cities!")
#
#     def show_info(self):
#         print(f"Country: {self.__name}\nContinent: {self.__continent}\nPopulation: {self.__population}\nPhone code: {self.__phone_code}\n"
#               f"Capital: {self.__capital}\nCities: {self.__cities}")
#
# try:
#     ukraine = Country("Ukraine", "Europe", 42000000, "+380", "Kyiv", ["Kyiv", "Lviv", "Odessa"])
#     georgia = Country("Georgia", "Europe", 3700000, "+995", "Tbilisi", ["Tbilisi", "Kutaisi", "Batumi"])
#     poland = Country("Poland", "Europe", 38000000, "+480", "Warsaw", ["Warsaw", "Kraków", "Poznań"])
#     ukraine.show_info()
#     georgia.show_info()
#     poland.show_info()
# except ValueError as error:
#     print(error)