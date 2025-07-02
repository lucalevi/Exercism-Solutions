class SpaceAge:
    EARTH_YEAR_IN_SECONDS = 31_557_600
    PLANET_ORBITAL_PERIODS = {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    def _calculate_age(self, orbital_period_earth_years: float) -> float:
        """Helper method to calculate age on a given planet."""
        earth_years = self.seconds / self.EARTH_YEAR_IN_SECONDS
        return round(earth_years / orbital_period_earth_years, 2)

    def on_earth(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["earth"])

    def on_mercury(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["mercury"])

    def on_venus(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["venus"])

    def on_mars(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["mars"])

    def on_jupiter(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["jupiter"])

    def on_saturn(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["saturn"])

    def on_uranus(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["uranus"])

    def on_neptune(self) -> float:
        return self._calculate_age(self.PLANET_ORBITAL_PERIODS["neptune"])
