from dataclasses import dataclass

@dataclass
class Disc:
    """
    Class representing a disc found in document by parser.
    """
    mold_name: str
    plastic: str
    manufacturer: str
    price: int

