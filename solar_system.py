class System:
    bodies = []
    planets = []
    stars = []
    moons = []

    def __init__(self):
        pass

    # def __str__(self):
    #     return f"{self.bodies}"
    # def __repr__(self):
    #     return f"{self.bodies}"
    def __repr__(self):
        return f"{self.bodies}"

    def add_body(self, body):
        if body not in self.bodies:
            System.bodies.append(body)
        return body

    def add_planet(self, planet):
        try:
            if planet.id == "planet":
                if planet not in System.planets:
                    System.planets.append(planet)
            return planet
        except:
            print("ERROR: YOU CANNOT ADD SOMETHING THAT IS NOT A PLANET! ")

    def add_star(self, star):
        try:
            if star.id == "star":
                if star not in System.stars:
                    System.stars.append(star)
            return star
        except:
            print("ERROR: YOU CANNOT ADD SOMETHING THAT IS NOT A STAR! ")

    def add_moon(self, moon):
        try:
            if moon.id == "moon":
                if moon not in System.moons:
                    System.moons.append(moon)
            return moon
        except:
            print("ERROR: YOU CANNOT ADD SOMETHING THAT IS NOT A MOON! ")


    def total_mass(self):

        total = 0
        for body in self.bodies:
            total += body.mass
        return f"The total mass is {total}"

    @classmethod
    def total_mass_of_system(cls):

        total = 0
        for body in cls.bodies:
            total += body.mass
        for planet in cls.planets:
            total += planet.mass
        for star in cls.stars:
            total += star.mass
        for moon in cls.moons:
            total += moon.mass

        return f"The total mass is {total}"

    @classmethod
    def all_planets(cls, system):
        for planets in cls.planets:
            return f"{cls.planets}"

    @classmethod
    def all_stars(cls, system):
        for star in cls.stars:
            return f"{cls.stars}"

    @classmethod
    def all_moons(cls, system):
        for moon in cls.moons:
            return f"{cls.moons}"


class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        return

    def __str__(self):
        return f"{self.name} {self.mass}"

    def __repr__(self):
        return f"{self.name} {self.mass}"


class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.id = "planet"
        self.day = day
        self.year = year
        return

    def __str__(self):
        return f" Name: {self.name} | Mass {self.mass} | Day: {self.day} | Year {self.year}"


class Star(Body):
    def __init__(self, name, mass, type_of_star):
        super().__init__(name, mass)
        self.id = 'star'
        self.type_of_star = type_of_star
        return

    def __str__(self):
        return f"  Name: {self.name} | Mass {self.mass} | Type: {self.type_of_star}"


class Moon(Body):
    def __init__(self, name, mass, month, orbital_planet):
        super().__init__(name, mass)
        self.id = 'moon'
        self.month = month
        self.orbital_planet = orbital_planet
        return

    def __str__(self):
        return f"""  Name: {self.name} | Mass {self.mass} | Month: {self.month} |
        ----------> I orbit around: {self.orbital_planet}"""


earth = Planet("Earth", 100, 23, 233)
jupitar = Planet("Jupitar", 5, 12, 210)
mars = Planet("Mars", 1222, 4, 110)
sun = Star("Sun", 200, "G-type")
earth_moon = Moon("Earth's moon", 300, 23, earth)


# system1 = System()
# system1.add_body(earth)
# system1.add_body(sun)
# print(system1)
# print(system1.total_mass())

body1 = Body(earth, earth.mass)
body2 = Body(sun, sun.mass)
body3 = Body(jupitar, jupitar.mass)

system1 = System()
system1.add_body(body1)
system1.add_body(body1)
system1.add_body(body2)
system1.add_body(body3)
system1.add_planet(jupitar)
system1.add_planet(earth)
system1.add_planet(mars)
# system1.add_planet(sun) # uncomment to catch error
# system1.add_star(jupitar) # uncomment to catch error
# system1.add_moon(sun) # uncomment to catch error
system1.add_star(sun)

# print(System.all_stars(system1))
print(System.all_planets(system1))
print(System.total_mass_of_system())
# print(body1)
# print(system1)

# print(system1.total_mass())


# print(earth)
# print(sun)
# print(earth_moon)
# bod1 = Body(earth, sun)
# bod2 = Body(earth, earth_moon)
# bod3 = Body(sun, earth_moon)
# system1 = System()
# system1.add_body(bod1)
# # print(bod1.mass)
# system1.add_body(bod2)
# system1.add_body(bod3)
# print(system1.total_mass())
# new_body = Body(earth, sun)
# system1.add_body(new_body)
# print(system1)
# solar = System()
# solar.add_body(new_body)
# print(system1.total_mass())
