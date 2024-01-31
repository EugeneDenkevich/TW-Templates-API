from enum import Enum


class Menu(Enum):
    HOME = "Home"
    ABOUT = "About"
    HOUSES = "Houses"
    KITCHEN = "Kitchen"
    ENTERTAINMENTS = "Entertainments"
    NEARESTS = "Nearests"
    SPECIAL = "Special"
    RULES = "Rules"
    GALLERY = "Gallery"
    CONTACTS = "Contacts"

    @classmethod
    def list(cls):
        return [m.value for m in cls]
