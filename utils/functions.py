import webbrowser
import os
import requests
import json

def open_browser_work():
    urlMokaly = "https://app.mokaly.com"
    urlSolutto = "https://sistema.solutto.com.br"
    webbrowser.get().open(urlMokaly)
    webbrowser.get().open(urlSolutto)
    return
    
def open_docker():
    os.startfile(r"C:\Program Files\Docker\Docker\Docker Desktop.exe")
    return
    
def open_spotify():
    os.startfile(r"C:\Users\linnu\AppData\Roaming\Spotify\Spotify.exe")
    return
    
def open_activity_log():
    url = "https://docs.google.com/spreadsheets/d/1RSzL6znaYHFxXjD1XSs7yJyDPp2XB_WJnkDOfgai7fQ/edit#gid=0"
    webbrowser.get().open(url)
    return
   
def open_visual_studio():
    os.startfile(r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe")
    return
   
def open_email():
    url = "https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)
    return
    
def get_weather():
    token = "c7212b735890fad4b51b6b17a3acc2c9"
    cityId = 0
    consultType = 1
    
    if consultType == 1:
        city = "pinhais"
        state = "pr"
        url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={city}&state={state}&token={token}"
        response = requests.request("GET", url)
        returnReq = json.loads(response.text)
        cityId = returnReq[0]["id"]
        
        url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{token}/locales"
        payload = f"localeId[]={cityId}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.request("PUT", url, headers=headers, data=payload)
        
        consultType = 2
    
    if consultType == 2:
        print(cityId)
        url = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{cityId}/current?token={token}"   
        response = requests.request("GET", url) 
        returnReq = json.loads(response.text)
        
    returnString = f"hoje em {city} está fazendo {returnReq['data']['temperature']} graus, a condição atual é {returnReq['data']['condition']} e a sensação térmica é de {returnReq['data']['sensation']} graus"
    return returnString

def searchFor(search_term, youtube = False):
    url = ""
    if youtube:
        url = "https://www.youtube.com/results?search_query=" + search_term
    else:
        url = "https://google.com/search?q=" + search_term
    
    webbrowser.get().open(url)
    return