import requests
import random
from lxml import etree
import json
import time
import os

s1 = 'https://y.qq.com/n/yqq/song/004WrpV81DMGHv.html'
s2 = 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
album_url = 'https://y.qq.com/n/yqq/album/003DFRzD192KKD.html'


def get_album_info(album_url):
    r = requests.get(album_url, headers=headers).text
    html = etree.HTML(r)
    songs = html.xpath("//div[@class='songlist__songname']")
    song_list = []
    for i in songs:
        song_url = i.xpath("./span/a/@href")[0]
        # print(song_url[22:-5])
        song_name = i.xpath("./span/a/text()")[0]
        song_list.append({"song_name": song_name, "song_url": song_url[22:-5]})
    return song_list


def get_download_url(songid):
    call_rand = str(random.randint(1000000000, 9999999999))
    vkey_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?' \
               '-=getplaysongvkey' + call_rand + \
               '&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%226657466372%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%226657466372%22%2C%22' \
               'songmid%22%3A%5B%22' \
               + songid + \
               '%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D'
    r2 = requests.get(vkey_url, headers=headers).text
    r2_json = json.loads(r2)
    vkey = r2_json['req_0']['data']['midurlinfo'][0]['vkey']
    url1 = 'http://113.200.90.26/amobile.music.tc.qq.com/' \
           'C400' \
           + songid + \
           '.m4a?guid=6657466372' \
           '&vkey=' + vkey + \
           '&uin=0&fromtag=66'
    return url1


album_urls = get_album_info(album_url)


def download(album_urls,album_name):
    num = 1
    for i in album_urls:
        song_name = i['song_name']
        song_id = i['song_url']
        music_url = get_download_url(song_id)
        r3 = requests.get(music_url, headers=headers, stream=True)
        music_path = "./music/" + album_name+"/"
        if not os.path.isdir(music_path):
            os.mkdir(music_path)
        with open(music_path+song_name+'.mp3', 'wb') as file:
            for i in r3.iter_content(1024):
                file.write(i)
        print('正在下载第{}首歌:{}'.format(num, song_name))
        num += 1
        time.sleep(3)

# download(album_urls,'七里香')
# 所有专辑歌曲下载
album_url1 = 'https://y.qq.com/n/yqq/album/0015rUVB2OUdGA.html#stat=y_new.singer.album.album_pic'

# 获取所有专辑的url
# all_album = 'https://y.qq.com/n/yqq/singer/002J4UUk29y8BY.html#tab=album&'
# r4 = requests.get(all_album, headers=headers).text
# html2 = etree.HTML(r4)
# s = html2.xpath("//span[@class='playlist__title_txt']")
# print(s)

get_albums_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI8870210912327798&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerAlbum%22%3A%7B%22method%22%3A%22get_singer_album%22%2C%22param%22%3A%7B%22singermid%22%3A%22002J4UUk29y8BY%22%2C%22order%22%3A%22time%22%2C%22begin%22%3A0%2C%22num%22%3A30%2C%22exstatus%22%3A1%7D%2C%22module%22%3A%22music.web_singer_info_svr%22%7D%7D'


def get_all_songs(get_albums_url):
    r4 = requests.get(get_albums_url, headers=headers).text
    r4_json = json.loads(r4)
    album_info = r4_json['singerAlbum']['data']['list']
    all_info = []
    for i in album_info:
        album_mid = i['album_mid']
        album_name = i['album_name']
        every_album_url ='https://y.qq.com/n/yqq/album/'+album_mid+'.html'
        all_info.append({album_name: get_album_info(every_album_url)})
    return all_info


Joker_music = get_all_songs(get_albums_url)
for i in Joker_music:
    keys = i.keys()
    all_albums = list(keys)[0]
    download(i[all_albums], list(keys)[0])


