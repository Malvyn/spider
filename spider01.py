import requests
import json
import re
from bs4 import BeautifulSoup

# r = requests.get("https://www.baidu.com")
# print(r.status_code)
# print(r.content)
# 使用字典传参
# info = {'username': 'zhangsan', 'password': '123456'}
# r3 =requests.get('http://httpbin.org/get', params=info)
# print(r3.text)

# r4 = requests.get('http://httpbin.org/get?username=zhangsan&password=123456')
# print(r4.text)
# headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
# r5 = requests.get('https://www.zhihu.com', headers=headers)
# print(r5.text)

# Json data

# r6 = requests.get('http://httpbin.org/get').text
# # print(r6)
# # print(type(r6))

# loads 将字符串转化为字典的数据格式(前提条件：字符串的格式必须和字典一致)
# 把字典转化为json字符串，用json.dumps
# r6_dict = json.loads(r6)
# print(r6_dict)
# print(type(r6_dict))
# print(r6_dict['headers']['Host'])

# with open('1.json', 'r') as file:
#     res = file.read()
# print(res)
# print(type(res))
# r_dic2 = json.loads(res)
# print(r_dic2['salary'])

# r = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1550308964340&di=0bc99a5835814e7a667bbbf71d369fe6&imgtype=0&src=http%3A%2F%2Fpic17.nipic.com%2F20111021%2F8633866_210108284151_2.jpg', stream=True)
# with open('1.jpg', 'wb') as file:
#     file.write(r.raw.read())
# with open('2.jpg', 'wb') as file:
#     for i in r.iter_content(2048):
#         file.write(i)

# misic_r = requests.get('http://isure.stream.qqmusic.qq.com/C400000DwvOd2VQYRl.m4a?guid=6657466372&vkey=1D86D6EFA790A86CC62C8119CD0F0FBAFC1846C9A59674F0E87DDE11CACFEA623899F1787D6D0EAF401A2A8330028D11388B0A2C2C5B52BB&uin=0&fromtag=66', stream=True)
# with open('love.mp3', 'wb') as file:
#     for i in misic_r.iter_content(10240):
#         file.write(i)

# info = {'username': 'zhangsan', 'password': '123456'}
# r3 =requests.get('http://httpbin.org/get', cookies=info)
# print(r3.text)

# r = requests.post('http://httpbin.org/post')
# print(r.text)

# timeout
# from requests.exceptions import ConnectionError,ConnectTimeout,RequestException
# try:
#     r = requests.get('https://www.ibeifeng.com', timeout=0.1)
#     print('ok')
# except ConnectTimeout:
#     print('co_timeout')
# except ConnectionError:
#     print('co_error')
# except RequestException:
#     print('error')

# 代理
# proxies = {
#     "http": "http://116.209.52.56:9999",
#     "https": "https://112.87.71.19:9999",
# }
#
# r3 = requests.get('http://httpbin.org/get', proxies=proxies)
# print(r3.text)

# ssl验证
# r = requests.get('https://www.12306.cn', verify=False)
# print(r.content.decode('utf8'))

# str='abcadaffafdaasaasdasasdsadsaasavasssacasc'
# pattern = 'a.c'
# res = re.findall(pattern, str)
# print(res)

# str='abca2casdcasweca.c'
# pattern = re.compile('a[^0-9]c') #^放下[]中间代表非的意思
# res = re.findall(pattern, str)
# print(res)

# str = 'abca2casdcasweca.c'
# pattern ='a\w{2}c'
# res = re.findall(pattern, str)
# print(res)

# *  匹配0-无穷大次数 默认匹配次数最多的情况
# ？ 匹配0 or 1
# + 匹配1-无穷大次数

# str = 'xyyyyyyyyyz'
# pattern ='xy{5,10}z'
# res = re.findall(pattern, str)
# print(res)

# str = 'abcabcacc'
# pattern ='(abc){2}'
# res = re.findall(pattern, str)
# print(res)

# print('\n')
# print(r'\n')

# 2 .提取所有的top放入列表中
# str2 ='top tip top tip to p'
# pattern = re.compile('top')
# res = re.findall(pattern, str2)
# print(res)

# 3. 匹配字符集
#    提取所有的a  b  c 放入列表中  （使用compile）
# str3='bcad'
# pattern = re.compile('[abc]')
# res = re.findall(pattern, str3)
# print(res)

# 4 .匹配行首，且以t开头，中间为i或o，结尾为p，的第一个字符 ： ['top']
# str4 = 'top tip top tip top'
# pattern = re.compile('^t[io]p')
# res = re.findall(pattern, str4)
# print(res)

# 5 .除i或o以外的所有其他字符 ： ['t4p', 't5p']
# str5 ='toptip top tip topt4pt5p'
# pattern = re.compile('t[^io]p')
# res = re.findall(pattern, str5)
# print(res)

# 6. 匹配出下列结果：['abcccb', 'abccb']
# str6='abcccbabccb'
# pattern = re.compile('abc{2,4}b')
# res = re.findall(pattern, str6)
# print(res)

# match
# strs = '1a2mmmmnnn2b3'
# pattern = re.compile('\d[a-z]\d')
# res = re.match(pattern, strs)
# print(res)
# print(res.group())

# search
# strs = 'aaaa1a2mmmmnnn2b3'
# pattern = re.compile('\d[a-z]\d')
# res = re.search(pattern, strs)
# print(res)
# print(res.group())

# 贪婪和非贪婪模式
str2 = "<span>ssss</span><a>aaaa</a><script>alert('hello')</script><a href="">bbbb</a><span>7777</span>"
# pattern = re.compile("<a.*</a>")
# print(pattern.findall(str2))

# 非贪婪模式
# pattern = re.compile("<a.*?</a>")
# print(pattern.findall(str2))
# findall()
# strs = '1a2mmmmnnn2b37g8'
# pattern = re.compile('(\d)[a-z](\d)')
# res = re.finditer(pattern, strs)
# print(res)
# for i in res:
#     print(i.group())

# str = '1a2bbb3c4df5'
# pattern = re.compile(r'[a-z]')
# print(re.split(pattern, str))

# sub
# strs = '1a2bbb3c4d5d'
# pattern = re.compile('[a-z]')
# res = re.sub(pattern, 'xyz', strs)
# print(res)

# subn
# strs = '1a2bbb3c4d5d'
# pattern = re.compile('[a-z]')
# res = re.subn(pattern, 'xyz', strs)
# print(res)

# 分组替换
# strs = '1a2mmmmnnn2b37g8'
# # pattern = re.compile('(\d)[a-z](\d)')
# # print(pattern.sub(r'\2---\1', strs))

# str1 = 'helloworald,hahcat,efadsf'
# pattern = re.compile('(\w+)')
# res = re.match(pattern, str1)
# print(res)

# strs = '你好,hello,,杨abc幂'
# pattern = re.compile('[\u4e00-\u9fa5]')
# print(pattern.findall(strs))

# str = '''313156566@qq.com
#     hjasd23@163.com
#     http://www.abc.com.cn
#     https://www.sae.com
#     ftp://www.nnn.org
#     ftps://www.jksad.net'''
# pattern = re.compile(r'[a-zA-Z]+://w{3}\.\w+(\.\w+){1,2}')
# res = re.finditer(pattern, str)
# for i in res:
#     print(i.group())


# str='广东省得到广州市'
# pattern = re.compile("[\u4E00-\u9FA5]+$")
# if re.findall(pattern, str):
#     print('全是中文')
# else:
#     print('不全是中文')

# str ='13811119999'
# pattern = re.compile("(1[35789]\d)\d{4}(\d{4})")
# res = re.sub(pattern, r'\1****\2', str)
# print(res)

# script = """以下内容不显示：<script    language='javascript'>alert('cc');</script>
# <p>fdgdfgdgsdg</p>
# <script>alert('dd');</script>"""
# pattern = re.compile(r'<script.*?</script>')
# res = re.sub(pattern, "", script)
# print(res)

# str='''
#     <img name="photo" src="../public/img/img1.png" />
#     <img name='news' src='xxx.jpg' title='news' />
#     '''
# pattern = re.compile(r'src=[\'"](.*?)[\'"]')
# res = re.findall(pattern, str)
# print(res)

# Beautiful Soup
# r = requests.get('https://www.ibeifeng.com').text
# soap = BeautifulSoup(r, 'html.parser')
# print(soap)

r = open('webhtml.html', encoding='utf8').read()
soup = BeautifulSoup(r, 'html.parser')
# print(soup.div.attrs['id'])

# print(soup.article.children)
# for i in soup.article.children:
#     print(i)

# print(soup.em.parents)

# 兄弟元素
# print(soup.article.next_sibling.next_sibling)
# print(soup.article.previous_sibling.previous_sibling)

# print(soup.find_all('div'))
# print(soup.find_all(href=re.compile('http://www.*')))

# print(soup.find_all(['a', 'div']))
# print(soup.find_all(id=True))

# print(soup.find_all(id='main'))
# print(soup.find_all(name='div', attrs=("name", "sec")))
# print(soup.find_all(name='div', attrs=("class", "one")))
# print(soup.find_all( 'div', limit=2))
# print(soup.find_all(class_="one", limit=1))
# print(soup.find_all(attrs={"data-foo":"value"}))
# print(soup.find(id='left').find_all('a')[2:])
# for i in soup.find(id='left').find_all('a'):
#     print(i)
#     print(i.text)
#     print(i.attrs['href'])

start_url = 'http://www.runoob.com/python/python-100-examples.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r = requests.get(start_url, headers=headers).content.decode('utf8')
soup = BeautifulSoup(r, 'html.parser')
links = soup.find(id='content').find_all('a', limit=100)
num = 1
for i in links:
    a = 'http://www.runoob.com' + i.attrs['href']
    r2 = requests.get(a, headers=headers).content.decode('utf8')
    soup2 = BeautifulSoup(r2, 'html.parser')
    ques = soup2.find(id='content').find_all("p")[1].text
    # 如果后面的例子的标签结构发生了变化，再异常处理
    # try except
    try:
        ans = soup2.find(class_='hl-main').text
    except AttributeError:
        ans = soup2.find('pre').text
    with open('py100.txt', 'a', encoding='utf8') as file:
        file.write("\n" + ques + "\n" + ans + "\n" + '=' * 80)
    print('现在下载到第%s个' % (num))
    num += 1

# a3 ='http://www.runoob.com/python/python-exercise-example41.html'
# r3 = requests.get(a3, headers=headers).content.decode('utf8')
# soup3 = BeautifulSoup(r3, 'html.parser')
# ques = soup3.find(id='content').find_all("p")[1].text
# # print(ques)
# ans = soup3.find('pre').text
# print(ans)