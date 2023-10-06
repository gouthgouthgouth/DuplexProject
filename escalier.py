import ifcopenshell

#--------------------------------------------------------------
# Définition de la classe escaliers
#--------------------------------------------------------------

class escalier:
    
    def __init__(self, ifcStairElement):
        self.idEscalier = None #NA : ID non défini
        self.etatRevetement = None #NA : état indisponible
        self.mainCourante = None
        self.dispositifVigilance = None #NA : état indisponible
        self.contrasteVisuel = None #NA : état indisponible
        self.largeurUtile = None
        self.mainCouranteContinue = None
        self.prolongMainCourante = None
        self.nbMarches = self.getNbMarches(ifcStairElement)
        self.nbVoleeMarches = None
        self.hauteurMarche = self.getHauteurMarche(ifcStairElement)
        self.giron = self.getGiron(ifcStairElement)
    
    def getNbMarches(self, ifcStairElement):
        #Renvoie le nombre de marches de l'escalier ifcStairElement
        return ifcStairElement.IsDecomposedBy[0].RelatedObjects[0].get_info()['NumberOfRiser']
    
    def getHauteurMarche(self, ifcStairElement):
        #Renvoie la hauteur des marches de l'escalier ifcStairElement
        return round(ifcStairElement.IsDecomposedBy[0].RelatedObjects[0].RiserHeight, 2)
    
    def getGiron(self, ifcStairElement):
        #Renvoie la longueur du giron des marches de l'escalier ifcStairElement
        return round(ifcStairElement.IsDecomposedBy[0].RelatedObjects[0].TreadLength, 2)

#--------------------------------------------------------------
# Définition de la fonction getEscaliersList qui
# retourne la liste complète de toutes les escaliers.
#--------------------------------------------------------------

def getEscaliersList(ifc_file_path):
    escalierList = []
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    for element in ifc_file.by_type('IfcStair'):
        newEscalier = escalier(element)
        escalierList.append(newEscalier)
    return escalierList