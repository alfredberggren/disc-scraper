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
    url: str

    def __hash__(self):
        return hash(self.mold_name)

    def __eq__(self, other):
        return (
            self.mold_name == other.mold_name
            and self.plastic == other.plastic
            and self.manufacturer == other.manufacturer
        )

