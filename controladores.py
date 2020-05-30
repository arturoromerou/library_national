from modelos import Editorial


class EditorialController():
    """Controlador de Editorial."""
    
    @staticmethod
    def create(**kwargs):
        editorial = Editorial(**kwargs)
        editorial.create()
        return editorial
