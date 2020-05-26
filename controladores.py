from modelos import ConnectionDB

class ControllerLibrary:
    library = None

    @classmethod
    def log_library(cls, data_library):
        cls.library = library(data_library['code'])
        return cls.library

class ControllerBooks:

    book = None

    @classmethod
    def log_book(cls, data_book):
        if cls.book is None:
            cls.book = []
        new_book = book(
            data_book['name']
            data_book[]
        )