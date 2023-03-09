
"""fi=open("fptout.txt","r",encoding='utf-8')
temp = fi.read().splitlines()
while True:
  try:
    temp.remove("")
  except ValueError:
    break
t=""
for i in temp:
    if not i[0].isnumeric():
        i=i[1:]
    if i[0]!="0":
        i="0"+i
    print(i,type(i))
    if len(i)==12:
        t=t+i+"\n"
fo=open("fpt.txt","w",encoding='utf-8')
fo.write(t)

"""

#temp=(open("fpt.txt","r",encoding='utf-8')).read().splitlines()
from pystyle import Colors, Colorate
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import warnings, time, os, openpyxl  
wb = openpyxl.Workbook() 
sheet = wb.active 
sheet.cell(row = 1, column = 1).value = "Họ và tên"
sheet.cell(row = 1, column = 2).value = "Ngày sinh"
sheet.cell(row = 1, column = 3).value = "Cccd"
sheet.cell(row = 1, column = 4).value = "Số báo danh"
sheet.cell(row = 1, column = 5).value = "Nơi sinh"
sheet.cell(row = 1, column = 6).value = "Nơi thi"
#sheet.cell(row = 1, column = 7).value = "Mã Schoolrank"
sheet.cell(row = 1, column = 7).value = "Top Schoolrank"
sheet.cell(row = 1, column = 8).value = "Điểm trắc nghiệm"
sheet.cell(row = 1, column = 9).value = "Điểm luận"
sheet.cell(row = 1, column = 10).value = "Điểm tổng"
sheet.cell(row = 1, column = 11).value = "Kết quả Học bổng"


warnings.filterwarnings("ignore", category=DeprecationWarning)
options = Options()
options.add_argument("--log-level=3")
options.add_argument("--mute-audio")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)


while True:
    try:
        driver.get('https://hcmuni.fpt.edu.vn/thi-sinh/tra-cuu')
        break
    except:
        continue

kj=input()
count=1
c1=1
for i in range(60001,62068+1):
    check0=False
    while check0==False:
        try:
            f = driver.page_source
            soup = BeautifulSoup(f, "html.parser")
            ipf = driver.find_element_by_id("f205")
            ipf.click()
            ipf.send_keys("FU-"+str(i))
            submit_button = driver.find_element_by_xpath("/html[@id='ctl00_Html1']/body[@id='ctl00_Body']/form[@id='aspnetForm']/div[@id='wrapper']/main[@class='main']/div[@id='ctl00_divCenter']/div[@class='Module Module-252']/div[@class='ModuleContent']/section[@class='fpt-tracuu']/div[@class='container']/div[@class='section-wrapper']/div[@class='row ajaxfilterresponse']/div[@class='col-lg-8']/div[@class='tracuu-form']/div[@class='form-tabs']/div[@id='tab-1']/div[@class='wrap-form btn-wrap']/button[@class='ajaxsearchbutton btn btn-success']")
            check=False
            while check==False:
                try:
                    submit_button.click()
                    check=True
                except:
                    print("f1")
            check=False
            while check==False:
                try:
                    f = driver.page_source
                    check=True
                except:
                    print("f2")
            soup = BeautifulSoup(f, "html.parser")
            text=soup.get_text()
            if "tên" in text:
                print(c1,end=" ")
                count+=1
                text=text[text.find("tên")+3:text.find("%")+1]
                text=text.replace("Năm sinh","")
                text=text.replace("CMND/CCCD","")
                text=text.replace("Số Báo Danh","")
                text=text.replace("Tỉnh/TP trường THPT","")
                text=text.replace("Địa điểm thi","")
                text=text.replace("Mã Schoolrank","")
                text=text.replace("Điểm Trắc nghiệm","")
                text=text.replace("Kết quả Học bổng","")
                text=text.replace("Điểm Luận","")
                text=text.replace("Điểm Tổng","")
                text=text.replace("Top Schoolrank","")
                text=text.replace("\n","&")
                listtext=text.split("&")
                while "" in listtext:
                    listtext.remove("")
                print(Colorate.Horizontal(Colors.yellow_to_red, " ".join(listtext), 1))
                for n in range(1,len(listtext)+1):
                    tg=listtext[n-1]
                    sheet.cell(row = count, column = n).value = tg
                c1=c1+1

            check=False
            while check==False:
                try:
                    time.sleep(0.5)
                    driver.find_element_by_id("f205").clear()
                    check=True
                except:
                    print("f3")
            
            check0=True
        except Exception as e: 
            print(e)

wb.save("sample.xlsx")