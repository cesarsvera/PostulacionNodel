from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from google.oauth2 import service_account

# Requiere las claves de acceso del archivo keys.json
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Se realiza la autenticacion de las credenciales
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# Id del google sheet para poder acceder al archivo
SAMPLE_SPREADSHEET_ID = '12Ki_LsleVfz1i9ws-h2zK2kW3K6eKiEt-mFVrzmLgUo'
   
try:
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    # Lectura del sheet
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="Reto1!A1:D").execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    print('Presentacion de las filas en un Array')
    countrys = []
    theme = []
    title = ['Author', 'Sentiment']
    # Array General con todas las filas
    ArrGeneral = []
    # Llenado de la primera fila
    for row in values:
      
      if row[2] not in countrys:
        if row[2] !='Country':
          countrys.append(row[2])
      if row[3] not in theme:
        if row[3] !='Theme':
          theme.append(row[3])
    newArr = title + countrys + theme
    ArrGeneral.append(newArr) 
    contV = 0
    valoreFalse = ["FALSE"]*(len(countrys)+len(theme))
    contador =0
    nombreGen = []
    # Logica para el cambio automatizado de las filas
    for row in values:
      if row[0] != "Author":
        for gn in ArrGeneral:
          if gn[0] != "Author":
            # print(gn[0] != row[0])
            if row[0] == gn[0]:
              # print("entro")
              indexCont =0
              for countr in countrys:
                if row[2] == countr:
                  gn[2+indexCont] = "TRUE"
                indexCont+=1
              indexThem = 0
              for them in theme:
                if row[3] == them:
                  gn[2+len(countrys) + indexThem] = "TRUE"
                indexThem+=1
            
            elif row[0] not in nombreGen:
              # print("que sucede")
              valorTemp = [row[0],row[1]] + valoreFalse
              indexCont =0
              for countr in countrys:
                if row[2] == countr:
                  valorTemp[2+indexCont] = "TRUE"
                indexCont+=1
              indexThem = 0
              for them in theme:
                if row[3] == them:
                  valorTemp[2+len(countrys) + indexThem] = "TRUE"
                indexThem+=1
              ArrGeneral.append(valorTemp)
              nombreGen.append(row[0])
              
          elif gn[0] == "Author" and contador ==0:
            valorTemp = [row[0],row[1]] + valoreFalse
            indexCont =0
            for countr in countrys:
              if row[2] == countr:
                valorTemp[2+indexCont] = "TRUE"
              indexCont+=1
            indexThem = 0
            for them in theme:
              if row[3] == them:
                valorTemp[2+len(countrys) + indexThem] = "TRUE"
              indexThem+=1
            ArrGeneral.append(valorTemp)
            contador+=1
            nombreGen.append(row[0])
            

            
        


    # Impresion por consola de las filas
    print(ArrGeneral)
    # Estructura del nuevo Sheet
    reques_body ={
      'requests':[
        {
          'addSheet': {
            'properties':{
              'title': "NuevoTemplate",
              'index': 0,
              'sheetType': 'GRID',
              'hidden': False
            }
          }
        }
      ]
    }
    vacios = [""]*(len(countrys)-1)
    cabecera = ["","","Country"]+ vacios +["Theme"]
    nuevoArrG = [cabecera] + ArrGeneral
    # Creacion de un nuevo Sheet
    response = sheet.batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=reques_body).execute()
    # Llenado del nuevo Sheet
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="NuevoTemplate!A1", valueInputOption="USER_ENTERED", body={"values":nuevoArrG}).execute()



    
except HttpError as err:
    print(err)
