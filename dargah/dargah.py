import requests

class Zibal:
    """
        A class to communicate with the zibal portal and perform various operations such as payment and transaction enquiry etc....
    
    Methods
    -------    
    """
    def __init__(self, marchant: str = "zibal") -> None:
        
        """
        Initialize and communication with your portal by marchant.
            - you can get marchant from https://zibal.ir
            - To get the marchant, you have to get the zibal port.

        Args:
            marchant: - The marhchant id required to communicate with your portal by default you can use the marchant of the zibal website
        
        Returns:
            output: - An object is returned from the zibal class and is reserved for your portal by Marchant and you can use this object to create a new payment etc
        """

        self.marchant = marchant
    