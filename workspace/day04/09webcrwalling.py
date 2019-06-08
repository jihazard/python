import bs4
import urllib.request

#1.
#
# url = "http://www.ikosmo.co.kr"
# html = urllib.request.urlopen(url)
#
# bsObj = bs4.BeautifulSoup(html,"html.parser")
# print(html.read())
#
# #divstr = bsObj.find("div", {"class":"article fl"})
# #print(divstr)
#
# divstr = bsObj.find_all("div", {"id":"container"})
#
# print(divstr)
#
# h2str = divstr.find("h2")
#
# url = "http://ikosmo.co.kr/?view=dynamicPage&code=center_intro"
# html = urllib.request.urlopen(url)
# bs = bs4.BeautifulSoup(html,"html.parser")
#
# divstr = bs.find("ul",{"class":"info_center"}).text
# strong = bs.find_all("li strong")
#
# print(divstr)
#
# for text in bs.find_all("li strong"):
#     print(text.text)


