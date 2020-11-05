from pprint import pprint
import urllib.request
import json

#https://rossvyaz.ru/about/otkrytoe-pravitelstvo/otkrytye-dannee/reestr-otkrytykh-dannykh - база данных


def ApiRegiusName(num):
    url = "https://api.regius.name/iface/phone-number.php?phone=" + num
    InfoList = None
    getInfo = None
    string_to_return = ""
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    if InfoList != None:
        try:
            string_to_return += (InfoList.get("company"))
        except:
            pass
        try:
            string_to_return += ("<br>" + InfoList.get("region") + "</br>")
        except:
            pass
    if string_to_return != "" and string_to_return != "<br></br>":
        return string_to_return
    else:
        return "empty"

def ApiSubnets(num):
    url = "http://rosreestr.subnets.ru/?get=num&format=json&num=" + num
    InfoList = None
    getInfo = None
    string_to_return = ""
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    if InfoList != None:
        items = InfoList.get("0")
        if items != None:
            try:
                string_to_return += (items.get("operator"))
            except:
                pass
            try:
                string_to_return += ("<br>" + items.get("region") + "</br>")
            except:
                pass
            if string_to_return == "" or string_to_return == "<br></br>" or len(string_to_return) == 1:
                return "empty"
            else:
                return string_to_return

def ApiHtmlWeb(num, TOKEN = None):
    if TOKEN == None:
        url = "https://htmlweb.ru/geo/api.php?json&telcod=" + num
    else:
        url = ("http://htmlweb.ru/geo/api.php?json&telcod=" + num + "&api_key=" + TOKEN)
    InfoList = None
    getInfo = None
    string_to_return = ""
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        pass
    try:
        InfoList = json.load(getInfo)
    except:
        pass
    if InfoList != None:
        try:
            f_name = InfoList.get("fullname")
            string_to_return += f_name
        except:
            pass
        try:
            item_0 = InfoList.get("0")
            if item_0 != None:
                try:
                    name = item_0.get("name")
                    string_to_return += ("<br>" + name)
                except:
                    pass
        except:
            pass
        try:
            item_1 = InfoList.get("1")
            if item_1 != None:
                try:
                    name = item_1.get("name")
                    string_to_return += ", " + name + "</br>"
                except:
                    pass
        except:
            pass
        try:
            limit = InfoList.get("limit")
            string_to_return += "<br>лимит api:" + str(limit) + "</br>"
        except:
            pass
    if string_to_return != "":
        return string_to_return
    else:
        return "empty"