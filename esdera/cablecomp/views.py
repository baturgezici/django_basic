from django.shortcuts import render
import sqlite3
import pandas as pd

# Create your views here.

def index(request):
    return render(request, 'cablecomp/index.html')

def about(request):
    return render(request, 'cablecomp/about.html')

def cables(request):

    cnx = sqlite3.connect('db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM data", cnx, index_col='id')
    table_dict = df.to_dict('records')

    return render(request, 'cablecomp/cables.html', {'table_dict': table_dict})