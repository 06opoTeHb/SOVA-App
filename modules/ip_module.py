"""
BASE: 1. "https://ipinfo.io/" + ip + "/json" ~50k/month
      2. "http://api.whois.vu/?s=ip&q=" + [ip|site] ~???
      3. "http://free.ipwhois.io/json/" + ip ~10k/month
      4. "http://ip-api.com/json/" + ip ~45/minute
"""

import urllib.request
import json
import pprint


def IpInfo_Io(ip, TOKEN=None):
    getInfo = None
    ip_address = ip
    InfoList = None
    if TOKEN != None:
        url = "https://ipinfo.io/" + ip_address + "?token=" + TOKEN
    else:
        url = "https://ipinfo.io/" + ip_address + "/json"
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    useful = False
    string_to_return = ""
    string_to_return += ("<b>ipinfo.io:</b>")
    try:
        string_to_return += ("<br>Расположение: <i>" + str(InfoList.get("loc")) + "</i>")
        useful = True
    except:
        pass
    try:
        string_to_return += ("<br>Город: <i>" + str(InfoList.get("city")) + "</i>")
        useful = True
    except:
        pass
    try:
        string_to_return += ("<br>Регион: <i>" + str(InfoList.get("region")) + "</i>")
        useful = True
    except:
        pass
    try:
        string_to_return += ("<br>Код страны: <i>" + str(InfoList.get("country")) + "</i>")
        useful = True
    except:
        pass
    try:
        string_to_return += ("<br>Хост: <i>" + str(InfoList.get("hostname")) + "</i>")
        useful = True
    except:
        pass
    try:
        string_to_return += ("<br>ASN: <i>" + str(InfoList.get("org")) + "</i>")
        useful = True
    except:
        pass
    try:
        string_to_return += ("<br>Часовой пояс: <i>" + str(InfoList.get("timezone")) + "</i>")
        useful = True
    except:
        pass
    if string_to_return != "":
        string_to_return += "<br></br>"
    if useful == True:
        return string_to_return
    else:
        return "Empty"

def Api_Whois_Vu(ip):
    url = "http://api.whois.vu/?s=ip&q=" + ip
    getInfo = None
    InfoList = None
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    string_to_return = ""
    string_to_return += ("<b>api.whois.vu:</b>")
    try:
        string_to_return += (InfoList.get("whois"))
    except:
        pass
    string_to_return += "<br></br>"
    return string_to_return

def Free_Ipwhois_Io(ip):
    url = "http://free.ipwhois.io/json/" + ip
    getInfo = None
    InfoList = None
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    string_to_return = ""
    string_to_return += ("<b>free.ipwhois.io:</b>")
    useful = False
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Расположение: <i>" + str(InfoList.get("latitude")) + "," + str(InfoList.get("longitude")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Город: <i>" + str(InfoList.get("city")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Регион: <i>" + str(InfoList.get("region")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Страна: <i>" + str(InfoList.get("country")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Код страны: <i>" + str(InfoList.get("country_code")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Соседи: <i>" + str(InfoList.get("country_neighbours")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>ASN: <i>" + str(InfoList.get("asn")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Компания: <i>" + str(InfoList.get("org")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>ISP: <i>" + str(InfoList.get("isp")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Часовой пояс: <i>" + str(InfoList.get("timezone")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Часовой пояс: <i>" + str(InfoList.get("timezone_name")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Время GMT: <i>" + str(InfoList.get("timezone_gmt")) + "</i>")
            useful = True
    except:
        pass
    try:
        currStr = InfoList.get("latitude")
        if currStr != None:
            string_to_return += ("<br>Валюта: <i>" + str(InfoList.get("currency")) + "</i>")
            useful = True
    except:
        pass
    if useful == True:
        return string_to_return
    else:
        return "Empty"

def IP_API_com(ip):
    url = "http://ip-api.com/json/" + ip
    InfoList = None
    getInfo = None
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    string_to_return = ""
    try:
        string_to_return += ("<b>ip-api.com:</b>")
        string_to_return += ("<br>Расположение: <i>" + str(InfoList.get("lat")) + "," + str(
            InfoList.get("lon")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Город: <i>" + str(InfoList.get("city")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Регион: <i>" + str(InfoList.get("regionName")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Индекс: <i>" + str(InfoList.get("zip")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Страна: <i>" + str(InfoList.get("country")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Код страны: <i>" + str(InfoList.get("countryCode")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>ASN: <i>" + str(InfoList.get("as")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Компания: <i>" + str(InfoList.get("org")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>ISP: <i>" + str(InfoList.get("isp")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>Часовой пояс: <i>" + str(InfoList.get("timezone")) + "</i>")
    except:
        pass
    try:
        string_to_return += ("<br>IP: <i>" + str(InfoList.get("query")) + "</i>")
    except:
        pass
    if string_to_return != "":
        string_to_return += "<br></br>"
    return string_to_return