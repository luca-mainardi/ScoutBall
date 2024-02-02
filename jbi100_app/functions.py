import pandas as pd


def change_age(age_column_value):
    """
    Receives an age value with the format years-days
    :param age_column_value
    :return: The age in years only
    """

    # Split the string by '-' and take the first part
    age = age_column_value.split('-')[0]
    # Convert to int
    return int(age)


def country_to_code(country_name):
    """
    Receives country name and converts it to country code
    :param country_name
    :return: country_code
    """

    country_name_to_code = {
        'Argentina': 'ARG',
        'Australia': 'AUS',
        'Belgium': 'BEL',
        'Brazil': 'BRA',
        'Cameroon': 'CMR',
        'Canada': 'CAN',
        'Costa Rica': 'CRI',
        'Croatia': 'HRV',
        'Denmark': 'DNK',
        'Ecuador': 'ECU',
        'England': 'ENG',
        'France': 'FRA',
        'Germany': 'DEU',
        'Ghana': 'GHA',
        'Iran': 'IRN',
        'IR Iran': 'IRN',
        'Japan': 'JPN',
        'Korea Republic': 'KOR',
        'Mexico': 'MEX',
        'Morocco': 'MAR',
        'Netherlands': 'NLD',
        'Poland': 'POL',
        'Portugal': 'PRT',
        'Qatar': 'QAT',
        'Saudi Arabia': 'SAU',
        'Senegal': 'SEN',
        'Serbia': 'SRB',
        'Spain': 'ESP',
        'Switzerland': 'CHE',
        'Tunisia': 'TUN',
        'United States': 'USA',
        'Uruguay': 'URY',
        'Wales': 'WAL'
    }

    country_code = country_name_to_code.get(country_name, 'Unknown')

    return country_code


def country_to_continent(country_name):
    """
    Receives country name and converts it to continent name where it belongs to
    :param country_name
    :return: continent name
    """

    country_continent_mapping = {
        'Argentina': 'South America',
        'Australia': 'Oceania',
        'Belgium': 'Europe',
        'Brazil': 'South America',
        'Cameroon': 'Africa',
        'Canada': 'North America',
        'Costa Rica': 'North America',
        'Croatia': 'Europe',
        'Denmark': 'Europe',
        'Ecuador': 'South America',
        'England': 'Europe',
        'France': 'Europe',
        'Germany': 'Europe',
        'Ghana': 'Africa',
        'Iran': 'Asia',
        'IR Iran': 'Asia',
        'Japan': 'Asia',
        'Korea Republic': 'Asia',
        'Mexico': 'North America',
        'Morocco': 'Africa',
        'Netherlands': 'Europe',
        'Poland': 'Europe',
        'Portugal': 'Europe',
        'Qatar': 'Asia',
        'Saudi Arabia': 'Asia',
        'Senegal': 'Africa',
        'Serbia': 'Europe',
        'Spain': 'Europe',
        'Switzerland': 'Europe',
        'Tunisia': 'Africa',
        'United States': 'North America',
        'Uruguay': 'South America',
        'Wales': 'Europe'
    }

    country_continent_name = country_continent_mapping.get(country_name, 'Unknown')

    return country_continent_name
