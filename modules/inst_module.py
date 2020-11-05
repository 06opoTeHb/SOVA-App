from modules.InstagramAPI import InstagramAPI
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5 import QtCore
import datetime
from geopy.geocoders import Nominatim
import json
import urllib
import time
from requests.exceptions import HTTPError
import os
import string
import random
global_path_scr = None

def INST_GetAppPath(main_path):
    global global_path_scr
    global_path_scr = str(main_path)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class Osintgram:
    api = None
    user_id = None
    target = ""

    unique_s = get_random_string(10)
    geolocator = Nominatim(user_agent=unique_s)

    def __init__(self, log, paswd):
        self.api = InstagramAPI(log, paswd)
        try:
            self.api.login()
        except:
            print("Сессия ИНСТАГРАМ не создана")

    def __getAdressesTimes__(self, id):
        only_id = {} #var only for max_next_id parameter | pagination
        photos = [] # only photos
        a = None #helper
        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']
                
            photos.append(a)

            if not 'next_max_id' in only_id:
                break
        
        
        locations = {}

        for i in photos: #extract location from photos, related
            for j in i:
                if 'lat' in j.keys():
                    lat = j.get('lat')
                    lng = j.get('lng')

                    locations[str(lat) + ', ' + str(lng)] = j.get('taken_at')

        address = {}
        for k,v in locations.items():
            details = self.geolocator.reverse(k) #locate for key
            unix_timestamp = datetime.datetime.fromtimestamp(v) # read timestamp as a value
            address[details.address] = unix_timestamp.strftime('%Y-%m-%d %H:%M:%S')


        sort_addresses = sorted(address.items(), key=lambda p: p[1], reverse=True)  #sorting

        return sort_addresses

    def __getUserFollowigs__(self, id):
        following = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''
            _ = self.api.getUserFollowings(id, maxid=next_max_id)
            following.extend(self.api.LastJson.get('users', []))
            next_max_id = self.api.LastJson.get('next_max_id', '')

        len(following)
        unique_following = {
            f['pk']: f
            for f in following
        }
        len(unique_following)
        return following

    def __getTotalFollowers__(self, user_id):
        followers = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = self.api.getUserFollowers(user_id, maxid=next_max_id)
            followers.extend(self.api.LastJson.get('users', []))
            next_max_id = self.api.LastJson.get('next_max_id', '')

        return followers

    def getHashtags(self, id):
        """pc.printout("Searching for target hashtags...\n")

        text = []
        only_id = {}
        a = None #helper
        hashtags = []
        counter = 1
        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
                with open('data.json', 'w') as outfile:
                    json.dump(only_id, outfile)

            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']

            try:
                for i in a:
                    c = i.get('caption', {}).get('text')
                    text.append(c)
                    #print str(counter) + ' ' + c
                    counter = counter +1
            except AttributeError:
                pass

            if not 'next_max_id' in only_id:
                break

        hashtag_counter = {}

        for i in text:
            for j in i.split():
                if j.startswith('#'):
                    hashtags.append(j.encode('UTF-8'))

        for i in hashtags:
            if i in hashtag_counter:
                hashtag_counter[i] += 1
            else:
                hashtag_counter[i] = 1

        sortE = sorted(hashtag_counter.items(), key=lambda value: value[1], reverse=True)

        if(self.writeFile):
            file_name = "output/" + self.target + "_hashtags.txt"
            file = open(file_name, "w")
            for k,v in sortE:
                file.write(str(v) + ". " + str(k.decode('utf-8'))+"\n")
            file.close()

        for k,v in sortE:
            print( str(v) + ". " + str(k.decode('utf-8')))"""

    def getTotalLikes(self, id):
        string_to_return = ""
        like_counter = 0
        only_id = {}
        a = None #helper
        counter = 0
        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']
            try:
                for i in a:
                    c = int(i.get('like_count'))
                    like_counter += c
                    counter = counter +1
            except AttributeError:
                pass
            if not 'next_max_id' in only_id:
                break
        string_to_return = str(like_counter) + " лайков(а) в " + str(counter) + " записях(и)"
        return string_to_return

    def getTotalComments(self, id):
        string_to_return = ""
        comment_counter = 0
        only_id = {}
        a = None #helper
        counter = 0
        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']
            try:
                for i in a:
                    c = int(i.get('comment_count'))
                    comment_counter += c
                    counter = counter +1
            except AttributeError:
                pass
            if not 'next_max_id' in only_id:
                break
        string_to_return = str(comment_counter) + " комментариев(я) в " + str(counter) + " записях(и)"
        return string_to_return

    def getPeopleTaggedByUser(self, id):
        ids = []
        username = []
        full_name = []
        post = []
        only_id = {}
        a = None #helper
        counter = 1
        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']
            try:
                for i in a:
                    c = i.get('usertags').get('in')
                    for cc in c:
                        if cc.get('user').get('pk') not in ids:
                            ids.append(cc.get('user').get('pk'))
                            username.append(cc.get('user').get('username'))
                            full_name.append(cc.get('user').get('full_name'))
                            post.append(1)
                        else:
                            index = ids.index(cc.get('user').get('pk'))
                            post[index] += 1
                        counter = counter +1
            except AttributeError:
                pass
            if not 'next_max_id' in only_id:
                break
        if len(ids) > 0:
            return post, full_name, username, ids
        else:
            return 0,0,0,0

    def getAddrs(self, id):
        addrs = self.__getAdressesTimes__(id)
        return addrs

    def getFollowers(self, id):
        followers = self.__getTotalFollowers__(id)
        model = QStandardItemModel()
        count_profiles = len(followers)
        count_model = 0
        if count_profiles != 0:
            model.setHorizontalHeaderLabels(
                ['id', 'username', 'закрытый', 'верифицирован', 'полное имя'])
            for item in followers:
                item1 = QStandardItem()
                item2 = QStandardItem()
                item3 = QStandardItem()
                item4 = QStandardItem()
                item5 = QStandardItem()
                try:
                    id = item['pk']
                except:
                    id = "?"
                try:
                    username = item['username']
                except:
                    username = "?"
                try:
                    fullname = item['full_name']
                except:
                    fullname = "?"
                try:
                    is_verified = item['is_verified']
                    if is_verified == True:
                        verif = "+"
                    elif is_verified == False:
                        verif = "-"
                except:
                    verif = "?"

                try:
                    is_private = item['is_private']
                    if is_private == True:
                        private = "+"
                    elif is_private == False:
                        private = "-"
                except:
                    private = "?"

                item1.setText(str(id))
                item2.setText(str(username))
                item3.setText(str(private))
                item4.setText(str(verif))
                item5.setText(str(fullname))
                item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                model.setItem(count_model, 0, item1)
                model.setItem(count_model, 1, item2)
                model.setItem(count_model, 2, item3)
                model.setItem(count_model, 3, item4)
                model.setItem(count_model, 4, item5)
                count_model += 1
        else:
            count_profiles = "no users"
        return model, count_profiles

    def getFollowings(self, id):
        followings = self.__getUserFollowigs__(id)
        model = QStandardItemModel()
        count_profiles = len(followings)
        count_model = 0
        if count_profiles != 0:
            model.setHorizontalHeaderLabels(
                ['id', 'username', 'закрытый', 'верифицирован', 'полное имя'])
            for item in followings:
                item1 = QStandardItem()
                item2 = QStandardItem()
                item3 = QStandardItem()
                item4 = QStandardItem()
                item5 = QStandardItem()
                try:
                    id = item['pk']
                except:
                    id = "?"
                try:
                    username = item['username']
                except:
                    username = "?"
                try:
                    fullname = item['full_name']
                except:
                    fullname = "?"
                try:
                    is_verified = item['is_verified']
                    if is_verified == True:
                        verif = "+"
                    elif is_verified == False:
                        verif = "-"
                except:
                    verif = "?"

                try:
                    is_private = item['is_private']
                    if is_private == True:
                        private = "+"
                    elif is_private == False:
                        private = "-"
                except:
                    private = "?"

                item1.setText(str(id))
                item2.setText(str(username))
                item3.setText(str(private))
                item4.setText(str(verif))
                item5.setText(str(fullname))
                item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                item5.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                model.setItem(count_model, 0, item1)
                model.setItem(count_model, 1, item2)
                model.setItem(count_model, 2, item3)
                model.setItem(count_model, 3, item4)
                model.setItem(count_model, 4, item5)
                count_model += 1
        else:
            count_profiles = "no users"
        return model, count_profiles

    def getUserID(self, username):
        string_to_return = "null"
        try:
            content = urllib.request.urlopen("https://www.instagram.com/" + username + "/?__a=1" )
        except urllib.error.HTTPError as err:
            if(err.code == 404):
                string_to_return = "null"
                print("Oops... " + username + " non exist, please enter a valid username.")
        try:
            data = json.load(content)
            string_to_return = data['graphql']['user']['id']
        except:
            string_to_return = "null"
        return string_to_return

    def getUserInfo(self, username):
        string_to_return = ""
        string_to_report = ""
        result = "bad"
        content = None
        try:
            content = urllib.request.urlopen("https://www.instagram.com/" + str(username) + "/?__a=1" )
        except urllib.error.HTTPError as err: 
            if(err.code == 404):
                string_to_return = "error: " + "Инстаграм не знает такого пользователя..."
                result = "bad"
        try:
            time.sleep(1)
            data = json.load(content)
            data = data['graphql']['user']
            result = "good"
            string_to_return += "<p align=\"center\"><h3>Информация о пользователе</h3></p>"
            string_to_report += "<p align=\"center\"><h3>Информация о пользователе</h3></p>"
            try:
                photo = data["profile_pic_url_hd"]
                f_path = str(global_path_scr) + "\\temp\\inst_" + str(username) + ".jpg"
                if not os.path.exists(f_path):
                    urllib.request.urlretrieve(photo, f_path)
                string_to_return += "<p align=\"center\"><img src=\"" + f_path + "\" title=\"Аватар\"></p>"
            except:
                pass
            string_to_return += ("<b>Пользователь:</b> <big>" + username + "</big> ")
            string_to_report += ("<b>Пользователь:</b> <big>" + username +  "</big> ")

            try:
                is_private = data["is_private"]
                if is_private == True:
                    string_to_return += ("<br>Закрытый аккаунт, больше информации нет")
                    string_to_report += ("<br>Закрытый аккаунт")
                else:
                    string_to_return += ("<br>Открытый аккаунт")
                    string_to_report += ("<br>Открытый аккаунт")
            except:
                pass

            try:
                fullname = data["fullname"]
                if fullname != "":
                    string_to_return += ("<br><b>Full name:</b> " + fullname)
                    string_to_report += ("<br><b>Full name:</b> " + fullname)
            except:
                pass

            try:
                id = data["id"]
                if id != "":
                    string_to_return += ("<br><b>ID:</b> <code>" + str(id) + "</code>")
                    string_to_report += ("<br><b>ID:</b> <code>" + str(id) + "</code>")
            except:
                pass

            try:
                count_records = str(data["edge_owner_to_timeline_media"]["count"])
                if count_records != "":
                    string_to_return += ("<br><b>Всего постов: </b>" + str(count_records))
                    string_to_report += ("<br><b>Всего постов: </b>" + str(count_records))
            except:
                pass

            try:
                biography = data["biography"]
                if biography != "":
                    string_to_return += ("<br><b>Биография (о себе): </b>" + biography)
                    string_to_report += ("<br><b>Биография (о себе): </b>" + biography)
            except:
                pass

            try:
                followings = data["edge_follow"]["count"]
                if followings != "":
                    string_to_return += ("<br><b>Подписки: </b>" + str(followings))
                    string_to_report += ("<br><b>Подписки: </b>" + str(followings))
            except:
                pass

            try:
                followers = data["edge_followed_by"]["count"]
                if followers != "":
                    string_to_return += ("<br><b>Подписчики: </b>" + str(followers))
                    string_to_report += ("<br><b>Подписчики: </b>" + str(followers))
            except:
                pass

            try:
                external_url = data["external_url"]
                if external_url != None:
                    string_to_return += ("<br><b>Ссылка: </b>" + external_url)
                    string_to_report += ("<br><b>Ссылка: </b>" + external_url)
            except:
                pass

            try:
                external_url_2 = data["external_url_linkshimmed"]
                if external_url_2 != None:
                    string_to_return += ("<br><b>Ссылка: </b>" + external_url_2)
                    string_to_report += ("<br><b>Ссылка: </b>" + external_url_2)
            except:
                pass

            try:
                has_channel = data["has_channel"]
                if has_channel == True:
                    string_to_return += ("<br>Имеет канал")
                    string_to_report += ("<br>Имеет канал")
            except:
                pass

            try:
                is_business_account = data["is_business_account"]
                if is_business_account == True:
                    string_to_return += ("<br>Бизнес-аккаунт")
                    string_to_report += ("<br>Бизнес-аккаунт")
            except:
                pass


        except Exception as err:
            string_to_return = "error:" + str(err)
            result = "bad"

        return result, string_to_return, string_to_report

    def getUserPhoto(self, id, l, username):
        result = "bad"
        limit = l
        a = None #helper
        counter = 0

        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']
            try:
                for item in a:
                    if counter == limit:
                        break
                        result = "bad"
                    else:
                        result = "good"
                    if "image_versions2" in item:
                        counter = counter + 1
                        url = item["image_versions2"]["candidates"][0]["url"]
                        photo_id = item["id"]
                        end = str(global_path_scr) + "\\reports\\" + username +  "_" + photo_id + ".jpg"
                        urllib.request.urlretrieve(url, end)
                    else:
                        carousel = item["carousel_media"]
                        for i in carousel:
                            if counter == limit:
                                break
                            counter = counter + 1                     
                            url = i["image_versions2"]["candidates"][0]["url"]
                            photo_id = i["id"]
                            end = str(global_path_scr) + "\\reports\\" + username +  "_" + photo_id + ".jpg"
                            urllib.request.urlretrieve(url, end)

            except AttributeError:
                pass
            except KeyError:
                pass
            if not 'next_max_id' in only_id:
                break
        return result

    def getMediaType(self, id):
        a = None #helper
        counter = 0
        photo_counter = 0
        video_counter = 0
        carousel_counter = 0
        while True:
            if (a == None):
                self.api.getUserFeed(id)
                a = self.api.LastJson['items']#photos 00, 01, 02...
                only_id = self.api.LastJson #all LastJson with max_id param
            else:
                self.api.getUserFeed(id, only_id['next_max_id']) #passing parameter max_id
                only_id = self.api.LastJson
                a = self.api.LastJson['items']
            try:
                for item in a:
                    if "media_type" in item:
                        if item["media_type"] == 1:
                            photo_counter = photo_counter + 1
                        elif item["media_type"] == 2:
                            video_counter = video_counter + 1
                        elif item["media_type"] == 8:
                            carousel_counter = carousel_counter + 1
                        counter = counter + 1
            except AttributeError:
                pass
            except KeyError:
                pass
            if not 'next_max_id' in only_id:
                break

        if counter > 0:
            return counter, photo_counter, video_counter, carousel_counter
        else:
            return counter, photo_counter, video_counter, carousel_counter