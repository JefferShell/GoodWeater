#_*_ coding:utf-8 _*_
'''
Created on 2014年10月12日

@author: Administrator
'''
import urllib2

url = 'http://m.weather.com.cn/data3/city%s.xml'
provinces=[]
cities = []
districts = []
lines=""

def getProvinces():
    try:
        url1 = 'http://m.weather.com.cn/data5/city.xml'
        content = urllib2.urlopen(url1).read()
        print content
        provinces = content.split(',')
    except:
        print 'getProvinces----','失败'
    return provinces
def getDeepArea(oldAreas):
    newArea = []
    for oldArea in oldAreas:
        try:
            AreaCode = oldArea.split('|')[0]
            newUrl = url % AreaCode
            content = urllib2.urlopen(newUrl).read()
            newArea +=content.split(',')
        except:
            print 'getDeepArea----',str(AreaCode),'失败'
    return newArea
def getLines(districts):
    line =""
    for d in districts:
        try:
            d_pair = d.split('|')
            d_code = d_pair[0]
            countyName = d_pair[1]
            url4 = url % d_code
            content4 = urllib2.urlopen(url4).read()
    #         print content4
            destination = content4.split('|')[1]
            line += "%s:%s\n" % (countyName,destination)
        except Exception , e:
            print e
            print 'getLines----',d_code,'失败了'
    return  line
def writeData(path):
    try:
        file = open(path,"w+")
        file.writelines(lines)
        file.close()
    except Exception,e:
        print "写入文件失败"
 
if __name__ == '__main__':
     try:
         provinces = getProvinces()
         print "10%"
         citis = getDeepArea(provinces)
         print "20%"
         districts =  getDeepArea(citis)
         print "50%"
         lines=getLines(districts)
         print "80%"
         writeData("d:/data.txt") 
         print "100%"
     except Exception,e:
         print "主程序失败",e
