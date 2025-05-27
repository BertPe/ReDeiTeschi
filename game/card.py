from enum import Enum

class Color(Enum):
    VERDE = "Verde"
    GIALLO = "Giallo"
    VIOLA = "Viola"
    NERO = "Nero"
    ROSSO = "Rosso"     # Pirati
    ORO = "Oro"         # Skull King
    CELESTE = "Celeste" # Sirene
    BIANCO = "Bianco"   # Fuga

class Card:
    def __init__(self, color: Color, number: int = None, is_special: bool = False, name: str = ""):
        self.color = color
        self.number = number
        self.is_special = is_special
        self.name = name

    def __repr__(self):
        if self.is_special:
            return f"{self.name} ({self.color.value})"
        else:
            return f"{self.number} {self.color.value}"

    def __eq__(self, other):
        return (self.color == other.color and self.number == other.number and
                self.is_special == other.is_special and self.name == other.name)

    def __hash__(self):
        return hash((self.color, self.number, self.is_special, self.name))
