from lxml import etree
import time

# html = etree.HTML(open('web.html', encoding='UTF-8').read())
# result = etree.tostring(html, pretty_print=True, encoding='utf-8').decode('utf-8')
# print(result)

# print(time.altzone)
# print(time.asctime())
# t1 = time.clock()
# for i in range(1, 100000):
#     pass
# t2 = time.clock()
# print(t2-t1)

#获取当前时间戳
# print(time.time())
# time.sleep(2)
# print(time.localtime())#get currect time tuple
# tupl = time.localtime()
# print(tupl[0])
# print(tupl.tm_year)
# print(time.time())
# tup1 = time.localtime(1550343612.3882923)
# print(time.localtime(1550343612.3882923))
# timestamp = time.mktime(tup1)
# print(timestamp)

# f = time.strftime('%Y-%m-%d %H:%M:%S', tup1)
# print(f)
#
# s = time.strptime('2019-02-24 15:42:01', '%Y-%m-%d %H:%M:%S')
# print(s)
#将字符串的时间"2017-10-10 23:40:00"转换为时间戳和时间元组
# s = time.strptime('2017-10-10 23:40:00', '%Y-%m-%d %H:%M:%S')
# print(s)
# print(time.mktime(s))

#字符串格式更改。如提time = "2017-10-10 23:40:00",想改为 time= "2017/10/10 23:40:00"
# f = time.strptime('2017-10-10 23:40:00', '%Y-%m-%d %H:%M:%S')
# s = time.strftime('%Y/%m/%d %H:%M:%S', f)
# print(s)

#将时间戳为1542088432转换为指定格式日期  如：2018-10-10 10:51:45
# tup3 = time.localtime(1542088432)
# str3 = time.strftime('%Y-%m-%d %H:%M:%S', tup3)
# print(str3)
#获得三天前此时的时间是多少
now = time.time()  # 当前时间戳
twl = now - 3 * 24 * 60 * 60  # 12天前的时间戳
tup4 = time.localtime(twl)
print(time.strftime('%Y/%m/%d %H:%M:%S', tup4))


