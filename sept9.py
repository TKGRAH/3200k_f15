def random_point():
    """Create function named random_point that returns a random latitude, longitude tuple.

    >>> latitude, longitude = random_point()
    >>> -180 <= latitude <= 180
    True
    >>> -90 <= longitude <= 90
    True
    
    """
    pass

    from random import randrange
    latitude = randrange(-180, 180)
    longitude = randrange(-90, 90)
    return latitude, longitude

if __name__ == '__main__':
    import doctest
    doctest.testmod()
