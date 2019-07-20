class System:
    def __init__(self):
        self.bodies = []

    # def __str__(self):
    #     return f"{self.bodies}"
    # def __repr__(self):
    #     return f"{self.bodies}"
    def __repr__(self):
        return f"{self.bodies}"

    def add(self, body):
        if body not in self.bodies: 
            self.bodies.append(body)
       
           

    def total_mass(self):
        # make regex to see if no characters present
        total = 0
        for body in self.bodies:
            total += body.mass
        return f"The total mass is {total}"


class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        return

    def __str__(self):
        return f"{self.name} {self.mass} "

    def __repr__(self):
        return f"{self.name} {self.mass} "


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
        return f"""  Name: {self.name} | Mass {self.mass} | Month: {self.month} |
        ----------> I orbit around: {self.orbital_planet}"""


earth = Planet("Earth", 100, 23, 233)
sun = Star("Sun", 200, "G-type")
earth_moon = Moon("Earth's moon", 300, 23, earth)


# system1 = System()
# system1.add(earth)
# system1.add(sun)
# print(system1)
# print(system1.total_mass())


body1 = Body(earth, earth.mass)
body2 = Body(sun, sun.mass)

system1 = System()
system1.add(body1)
system1.add(body1)
system1.add(body2)


# print(body1)
print(system1)
# print(system1.total_mass())


# print(earth)
# print(sun)
# print(earth_moon)
# bod1 = Body(earth, sun)
# bod2 = Body(earth, earth_moon)
# bod3 = Body(sun, earth_moon)
# system1 = System()
# system1.add(bod1)
# # print(bod1.mass)
# system1.add(bod2)
# system1.add(bod3)
# print(system1.total_mass())
# new_body = Body(earth, sun)
# system1.add(new_body)
# print(system1)
# solar = System()
# solar.add(new_body)
# print(system1.total_mass())
