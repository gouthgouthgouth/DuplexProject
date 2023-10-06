import ifcopenshell

#--------------------------------------------------------------
# Définition de la classe entrée
#--------------------------------------------------------------

class entree:
    
    def __init__(self, ifcDoorElement):
        self.idEntree = None #NA : ID non défini
        self.type = None #NA : type d'entrée non défini
        self.ascenseur = None #NA : Pas d'ascenseur
        self.escalierNbMarche = None
        self.escalierMainCourante = None
        self.reperageEltsVitres = None #NA
        self.largeurPassage = self.getLargeurPassage(ifcDoorElement)
        self.eclairage = None #NA : Pas d'éclairages
        self.typePorte = None #NA : type de porte non défini
        self.espaceManoeuvre = None
        self.largManoeuvreExt = None
        self.longManoeuvreExt = None
        self.largManoeuvreInt = None
        self.longManoeuvreInt = None
        self.typePoignee = None #NA : Pas de poignées

    def getLargeurPassage(self, ifcDoorElement):
        #Retourne la largeur de la porte avec 2 chiffres après la virgule.
        return round(ifcDoorElement.OverallWidth, 2)

#--------------------------------------------------------------
# Définition de la fonction getEntreesList qui
# retourne la liste complète de toutes les entrées.
#--------------------------------------------------------------

def getEntreesList(ifc_file_path):
    entreeList = []
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    for element in ifc_file.by_type('IfcDoor'):
        newEntree = entree(element)
        entreeList.append(newEntree)
    return entreeList