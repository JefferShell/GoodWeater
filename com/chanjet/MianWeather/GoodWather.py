#_*_ coding:utf-8 _*_
'''
Created on 2014��10��13��

@author: administrator
'''

import urllib2
import json
# import sys
# import locale
# 
# def p(f):
#     print '%s.%s(): %s' % (f.__module__, f.__name__, f())
# p(sys.getdefaultencoding)

class weather:
    cityName = "北京"
    url = 'http://www.weather.com.cn/data/cityinfo/%s.html'
    def __init__(self):
        self.initApp()
    def initApp(self):
        try:
            cityName = raw_input("请输入您坐在地区的名字:\t");
            cityName = cityName.decode("utf-8")
            cityCode = self.getCityCode(cityName)
            codeUrl = self.url % cityCode
            result = urllib2.urlopen(codeUrl).read()
#             print result
            data = json.loads(result)
            result = data['weatherinfo']
            print "城市:\t",result['city'],'\n'
            print "城市编码:\t",result['cityid'],'\n'
            print "最低温度:\t",result['temp1'],'\n'
            print "最高温度:\t",result['temp2'],'\n'
            print "天气:\t",result['weather'],'\n'
            print "截至时间:\t",result['ptime'],'\n'
        except:
            print "请重新输入吧!!!没找到"
            self.initApp()
    def getCityCode(self,cityName):
        cities={}
        file = open("d:/data.txt","r")
        line = file.readline()
        while line :
            try:
                line = line.replace("\n","")
                line = line.decode("utf-8")
                code_name = line.split(":")
                code=code_name[1]
                name=code_name[0]
                if name==cityName:
                    file.close()
                    return code
                line = file.readline()
            except:
                print code_name,"失败了"
        print "没找到哇"
         
 
if __name__ == '__main__':
    w = weather()