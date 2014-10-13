#_*_ coding:utf-8 _*_
'''
Created on 2014年10月12日

@author: Administrator
'''
import urllib2

#得到省份代码  01|北京,02|上海,03|天津。。。。。
url1 = 'http://m.weather.com.cn/data5/city.xml'
content = urllib2.urlopen(url1).read()
print content
provinces = content.split(',')

url = 'http://m.weather.com.cn/data3/city%s.xml'
#得到城市代码  0501|哈尔滨,0502|齐齐哈尔,0503|牡丹江,0504|
cities = []
districts = []
line = "{"
for p in provinces:
    try:
        p_code = p.split('|')[0]
        url2 = url % p_code
        content2 = urllib2.urlopen(url2).read()
#         print 'content2:',content2
        cities +=content2.split(',')
#         print 'len:',len(cities)
    except:
        print str(p_code),'失败'
        #得到地区代码  010101|北京,010102|海淀,010103....
# print '长度',len(cities)
for c in cities:
    c_code = c.split('|')[0]
    url3 = url % c_code
    content3 = urllib2.urlopen(url3).read()
#     print 'content3',content3
    districts += content3.split(',')  
for d in districts:
    try:
        d_pair = d.split('|')
        d_code = d_pair[0]
        countyName = d_pair[1]
        url4 = url % d_code
        content4 = urllib2.urlopen(url4).read()
#         print content4
        destination = content4.split('|')[1]
        line += "'%s':'%s',\n" % (countyName,destination)
    except:
        print d_code,'失败了'    
lines = line[0,len(line)]+"}"
file = open("data.txt","w+")
file.writelines(lines)
file.close()

# print countyName + ':' + destination