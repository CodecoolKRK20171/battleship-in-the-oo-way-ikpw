class Ship:


    def __init__(self, positions, name, is_vertical):

        """
        Contains squares objects that togather creates ships

        Parameters
        ----------
        positions: tuple of square objects togather creating ship
        name: name of the ship (out of 5 possible ships)
        
        Returns
        -------
        None
        """

        self.name = name
        self.positions = positions
        self.is_vertical = is_vertical
