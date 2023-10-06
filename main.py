#--------------------------------------------------------------
# Le script main.py récupère toutes les données recherchées pour
# chaque objet (escalier, tronçon et entrée) depuis les scripts escalier.py, entree.py et troncon.py
#--------------------------------------------------------------

import escalier
import troncon
import entree
import csv
import ifcopenshell
import pandas as pd
import streamlit as st


ifc_file_path = 'Duplex1669037373.5046499.ifc'

#--------------------------------------------------------------
# Initialisation des variables objets et listesObjets.
# listesObjets contient 3 listes, chacune contenant l'ensemble des attributs recherchés.
#--------------------------------------------------------------

objets = ["escalier","troncon", "entree"]
csv_files = ["escaliers.csv","troncons.csv", "entrees.csv"]
listesObjets = [escalier.getEscaliersList(ifc_file_path),
                troncon.getTronconsList(ifc_file_path),
                entree.getEntreesList(ifc_file_path)]

#--------------------------------------------------------------
# Ecriture des 3 fichiers csv contenant les données recherchées.
#--------------------------------------------------------------

for i in range(len(objets)):
    # On itère sur chaque type d'objet

    csv_file_path= csv_files[i]
    objetsList = listesObjets[i]

    with open(csv_file_path, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)

        #--------------------------------------------------------------
        # Ecriture de la 1ère ligne contenant les en-têtes
        #--------------------------------------------------------------
        headers = []
        try:
            for attribut in objetsList[0].__dict__:
                headers.append(attribut)
            writer.writerow(headers)
        except:
            print("No element in list")

        #--------------------------------------------------------------
        # Pour toutes les lignes suivantes, on itère sur chaque élément
        # de la liste objetsList, puis sur chaque attribut.
        # On ajoute alors chaque attribut à la liste attributesValues
        # que l'on écrit dans le fichier csv
        #--------------------------------------------------------------

        attributesValues = []
        for element in objetsList :
            for attribut in element.__dict__:
                try:
                    if(element.__dict__[attribut] != None):
                        attributesValues.append(element.__dict__[attribut])
                    else:

                        #Si l'attribut a pour valeur None on écrit "Non extrait" à la place.

                        attributesValues.append("Non extrait")
                except:
                    attributesValues.append("Non extrait")
            writer.writerow(attributesValues)
            attributesValues = []

#--------------------------------------------------------------
# Affichage des 3 tableaux sur browser via l'application Streamlit
#--------------------------------------------------------------

st.title("Données du Duplex")

for csv in csv_files:

    # Ecriture des tableaux
    data = pd.read_csv(csv)
    st.write(csv, ":")
    st.write(data)

    # Ecriture des boutons pour télécharger le fichier
    if st.button("Exporter", key = csv):
        st.download_button(
            label="Télécharger fichier CSV",
            data=data.to_csv(index=False),
            file_name=csv,
            mime='text/csv',
        )