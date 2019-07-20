class System:
    def __init__(self):
        self.bodies = []

    def __str__(self):
        return f"{self.bodies}"

    def __repr__(self):
        return f"{self.bodies}"

    def add(self):
        self.bodies.append()

    # this will add celestial body to the list

    def total_mass(self):
        total = 0
        for body in self.bodies:
            total += body
        return total


class Body(System):
    def __init__(self, name, mass):
        super.()__init__(name, mass)
        self.name = name
        self.mass = mass

    def __str__(self):
        return f"{self.name} {self.mass} "

    def __repr__(self):
        return f"{self.bodies} {self.mass} "


class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year
        return

    def __str__(self):
        return f" Name: {self.name} | Mass {self.mass} | Day: {self.day} | Year {self.year} "


class Star(Body):
    def __init__(self, name, mass, type_of_star):
        super().__init__(name, mass)
        self.type_of_star = type_of_star

        return

    def __str__(self):
        return f"  Name: {self.name} | Mass {self.mass} | Type: {self.type_of_star}"


class Moon(Body):
    def __init__(self, name, mass, month, orbital_planet):
        super().__init__(name, mass)
        self.month = month
        self.orbital_planet = orbital_planet
        return

    def __str__(self):
        return f"  Name: {self.name} | Mass {self.mass} | Month: {self.month}|\n I orbit around: {self.orbital_planet}"


earth = Planet("Earth", 234234, 23, 233)
sun = Star("Sun", 32323, "G-type")
earth_moon = Moon("Earth's moon", 3232, 23, earth)


print(earth)
print()
print(sun)
print()
print(earth_moon)


# solar = System()
# solar.add()
# print(solar)
# print(solar.total_mass())


# body1 = Body('body1', 4322)
# print(body1)
