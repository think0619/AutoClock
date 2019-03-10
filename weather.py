import requests
import pygame
from baidutts import generateAudio
import datetime
from relayhandler import controlrelay



import time
def getweatherinfo():
    api_url = "https://restapi.amap.com/v3/weather/weatherInfo"
    api_key = "38b627d6ea5257d6bf3ac3e161d1f7db"
    city = "320100"
    extensions = "all"
    getWehURL = api_url+"?key=" + api_key + "&city=" + city + "&extensions=" + extensions + "&output=Json"
    r = requests.get(getWehURL)
    r.encoding = 'utf-8'
    return r

def gettodayNJWeather():
    json_data = getweatherinfo().json()
    result_status = json_data['infocode']
    if result_status == "10000":
        city = json_data["forecasts"][0]['city']
        casts = json_data["forecasts"][0]['casts']
        thisdaycast = city + ":" + casts[0]["date"] + " " + casts[0]["dayweather"] + "转 " + casts[0]["nightweather"] + "温度：" + casts[0]["nighttemp"] + "到" + casts[0]["daytemp"] + "度"

#        print(thisdaycast)
        return thisdaycast

def weatherbroadcast():
    generateAudio(gettodayNJWeather())
    pygame.mixer.init(16000, -16, 1, 1024)
    pygame.mixer.music.load('result.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    time.sleep(60)

def playclockmusic():
    path1 = 'clockmusic/野蜂飞舞马克西姆.mp3'
    path2 = 'clockmusic/金城兰州.mp3'
    path3 = 'clockmusic/default.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(path1)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.load(path2)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.load(path3)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

controlrelay(7,1)
time.sleep(1)
controlrelay(7,0)
time.sleep(1)
controlrelay(7,1)
time.sleep(1)
controlrelay(7,0)
time.sleep(1)


while True:
    now = datetime.datetime.now()
    # 闹钟
    if now.hour == 5 and now.minute == 50:
        playclockmusic()
    elif now.hour == 6 and now.minute == 10:
        weatherbroadcast()
    else:
        controlrelay(7, 0)
    time.sleep(60)









