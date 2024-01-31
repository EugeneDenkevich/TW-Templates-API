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

    @classmethod
    def to_russian(cls):
        d = {
            cls.HOME.value: "Главная",
            cls.ABOUT.value: "О нас",
            cls.HOUSES.value: "Проживание",
            cls.KITCHEN.value: "Кухня",
            cls.ENTERTAINMENTS.value: "Развлечения",
            cls.NEARESTS.value: "Ближайшие места",
            cls.SPECIAL.value: "Свадьбы",
            cls.RULES.value: "Плавила поведения",
            cls.GALLERY.value: "Галерея",
            cls.CONTACTS.value: "Контакты",
        }

        return d
