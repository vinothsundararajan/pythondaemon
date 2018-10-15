import urllib.request
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

r = urllib.request.urlopen("https://www.cricbuzz.com/cricket-match/live-scores")
read = r.read()
bs = BeautifulSoup(read,'html.parser')

soup1 = bs.find_all('div', attrs={"class": "cb-col-100 cb-col cb-schdl"})

final=[]

for l in range(len(soup1)):
    aaa = str(soup1[l].text)
    a = aaa[:13]
    bbb = str(' Read Preview')
    b = bbb[:13]
    if a == b:
        append="Match not yet started"
    else:
        append=aaa
    final.append(append)
    
    count = 0
toaster = ToastNotifier()

while count <= len(final):
    toaster.show_toast(final[count], final[count + 1])
    count = count + 2
