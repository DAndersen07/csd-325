"""Assignment 7 - Dustin Andersen.

Format a city and country with optional population and language.
The demonstration calls run only when this file is executed directly,
so importing the function into the test file does not print examples.
"""


def city_country(city, country, population=None, language=None):
    """Return City, Country with population and language when provided."""
    result = f"{city.title()}, {country.title()}"
    # None allows a population of zero to be included correctly.
    if population is not None:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


if __name__ == '__main__':
    # Two arguments: city and country.
    print(city_country('Santiago', 'Chile'))
    # Three arguments: city, country, and population.
    print(city_country('Santiago', 'Chile', 5000000))
    # Four arguments: city, country, population, and language.
    print(city_country('Santiago', 'Chile', 5000000, 'Spanish'))
