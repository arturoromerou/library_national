from modelos import Editorial
from modelos import Model


class EditorialController:
    """Controlador de Editorial."""
    
    @staticmethod
    def create(name): # Metodo estatico "create" 
        if name != "":
            editorial = Editorial(name) # instancio un objeto en la clase Editorial
            # llamo el metodo create del objeto instanciado para guardarlo en bd
            rowcount = editorial.create() # el metodo "create" retorna el numero de filasafectadas
            if rowcount >= 1:
                return editorial
        return None
    
    # Agregué (Miguel)
    @staticmethod
    #
    def update(self):
        return Editorial.read()

    @staticmethod
    def drop(self):
        return Editorial.Controller(self.eliminar)
