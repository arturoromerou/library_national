from modelos import Editorial


class EditorialController():
    """Controlador de Editorial."""
    
    @staticmethod
    def create(**kwargs):
        if "name" in kwargs and kwargs["name"] is not None:
            editorial = Editorial(**kwargs)
            editorial.create()
            return editorial
        return None

    @staticmethod
    def read():
        return Editorial.read()
        
