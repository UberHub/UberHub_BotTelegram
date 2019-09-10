from botocore.vendored import requests
from datetime import datetime, timedelta
import os
import json

def buscarVagas():
    querystring = {"key":os.environ['GOOGLE_API_KEY']}
    url = "https://sheets.googleapis.com/v4/spreadsheets/1QwzK3_XSCqNSWTkWSoTAC1tRzHkOKrdSw9KFh__eMJY/values/A2:D1000"
    response = requests.request("GET", url, data="", params=querystring)
    values = response.json()
    texto = "🏢⚡Vagas - Ecossistema de Inovação de Uberlândia⚡🏢\n\n" 
    for value in values["values"]:
        ativo = value[3].upper()
        if ativo == "SIM" :
            texto = texto+value[0]+"\n"+value[1]+"\n"+value[2]+"\n\n ⏬⏬⏬⏬⏬ \n \n"    
    texto = texto + "💜🚀💜🚀💜🚀\n"
    texto = texto + """😍 Gostou? Compartilhe!!!\n\n⚡Lista de vagas\nhttp://bit.ly/2kdS6Yd \n\n⚡Incluir vagas?\nChame no privado o @FerdinandoKun\n\n""" 
    return texto

def buscarNoticias():
    querystring = {"key":os.environ['GOOGLE_API_KEY']}
    url = "https://sheets.googleapis.com/v4/spreadsheets/1QwzK3_XSCqNSWTkWSoTAC1tRzHkOKrdSw9KFh__eMJY/values/Noticias!A2:D1000"
    response = requests.request("GET", url, data="", params=querystring)
    values = response.json()
    texto = "📰⚡Notícias - Ecossistema de Inovação de Uberlândia⚡📰\n\n" 
    for value in values["values"]:
        ativo = value[2].upper()
        if ativo == "SIM" :
            texto = texto+value[0]+"\n"+value[1]+"\n\n ⏬⏬⏬⏬⏬ \n \n"    
    texto = texto + "💜🚀💜🚀💜🚀\n"
    texto = texto + """😍 Gostou? Compartilhe!!!\n\n ⚡Lista de notícias\nhttp://bit.ly/2kdS6Yd \n\n⚡Incluir notícias?\nChame no privado o @FerdinandoKun\n\n""" 
    return texto

def buscarAgenda():
    d = datetime.now() - timedelta(minutes = -90)
    hojeUberHub = d.strftime('%Y-%m-%dT00:00:00-03:00')
    querystring = {"key":"AIzaSyCUMuDu23XkyduDqDe-8ZyQDS04SIDTYpI",
                    "timeMin":hojeUberHub
                    } 
    url = "https://www.googleapis.com/calendar/v3/calendars/triangulodainovacao@gmail.com/events"           
    response = requests.request("GET", url, data="", params=querystring)
    values = response.json()
    texto = "📅⚡Agenda Oficial - Ecossistema de Inovação de Uberlândia⚡📅\n\n" 
    for value in values["items"]:
        ativo = value["id"]
        if ativo != "5i1s05h31ris3co1a34gjnpukt": #Excluindo evento fixo do calendário
            texto = texto+value["description"]+"\n\n ⏬⏬⏬⏬⏬ \n\n"
    texto = texto + "💜🚀💜🚀💜🚀\n"
    texto = texto + """😍 Gostou? Compartilhe!!!\n\n⚡ Agenda na web \nhttp://bit.ly/agendaunicainovacao \n\n⚡ Incluir evento?\nPreencha o formulário no link http://bit.ly/inserireventoinovacao\n\n""" 
    return texto