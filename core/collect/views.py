from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

from . models import Table1, Table2, Table3
# Create your views here.

def home(request):
    return render (request, 'index.html')

def collect(request):
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_excel(file, skiprows=3)
        
        # Sélectionner uniquement les données dans la plage spécifiée (par exemple, 10 premières colonnes)
        df = df.iloc[:, :20]  # Sélectionner les 10 premières colonnes
        
        # Supprimer les lignes avec des valeurs NaN dans toutes les colonnes
        df.dropna(axis=0, how='all', inplace=True)
        
        # Supprimer les colonnes avec des valeurs NaN dans toutes les lignes
        df.dropna(axis=1, how='all', inplace=True)

        # Convertir le DataFrame en liste de dictionnaires
        data = df.to_dict(orient='records')
        # Diviser le DataFrame en trois blocs de cinq colonnes chacun
        block1 = df.iloc[:, :5]
        block2 = df.iloc[:, 5:10]
        block3 = df.iloc[:, 10:15]

        # Convertir chaque bloc en liste de dictionnaires
        block1_data = block1.to_dict(orient='records')
        block2_data = block2.to_dict(orient='records')
        block3_data = block3.to_dict(orient='records')

        # inserser les données dans la table 1 
        for index, ligne in block1.iterrows():
            values = ligne.tolist()
            print(f"a la ligne  {index + 1}:")
            Table1.objects.create(
                field1 = values[0],
                field2 = values[1],
                field3 = values[2],
                field4 = values[3],
                field5 = values[4]
            )

        # inserser les données dans la table 2
        for index, ligne in block2.iterrows():
            values = ligne.tolist()
            print(f"a la ligne  {index + 1}:")
            Table2.objects.create(
                field1 = values[0],
                field2 = values[1],
                field3 = values[2],
                field4 = values[3],
                field5 = values[4]
            )

        # inserser les données dans la table 3
        for index, ligne in block3.iterrows():
            values = ligne.tolist()
            print(f"a la ligne  {index + 1}:")
            Table3.objects.create(
                field1 = values[0],
                field2 = values[1],
                field3 = values[2],
                field4 = values[3],
                field5 = values[4]
            )

        
        return HttpResponse('Seules les données du tableau principal ont été conservées.')
    else:
        return HttpResponse('Erreur: Aucun fichier trouvé.')
