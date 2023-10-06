import ifcopenshell

#--------------------------------------------------------------
# Définition de la classe tronçon
#--------------------------------------------------------------

class troncon:
    
    def __init__(self, ifcSlabElement):
        self.idtroncon = None #NA : ID non défini
        self.From = None
        self.to = None
        self.longueur = None
        self.typetroncon = None
        self.statutVoie = None #NA : pas de voie publique ici
        self.pente = None
        self.devers = None
        self.accessibiliteGlobale = None

#--------------------------------------------------------------
# Définition de la fonction getTronconsList qui
# retourne la liste complète de touts les tronçons.
#--------------------------------------------------------------

def getTronconsList(ifc_file_path):
    TronconsList = []
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    for element in ifc_file.by_type('IfcSlab'):
        newTroncon = troncon(element)
        TronconsList.append(newTroncon)
    return TronconsList