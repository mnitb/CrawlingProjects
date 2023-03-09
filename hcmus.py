#hust
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import warnings, time, os,openpyxl 
from selenium.webdriver.common.by import By

wb = openpyxl.Workbook() 
sheet = wb.active 
sheet.cell(row = 1, column = 1).value = "MSSV"
sheet.cell(row = 1, column = 2).value = "CCCD"
sheet.cell(row = 1, column = 3).value = "Họ và tên"
sheet.cell(row = 1, column = 4).value = "Nv"
sheet.cell(row = 1, column = 5).value = "Ngành/Nhóm ngành"
sheet.cell(row = 1, column = 6).value = "PTXT"
sheet.cell(row = 1, column = 7).value = "Ghi chú"



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
        driver.get('https://tsdh.hcmus.edu.vn/ketqua')
        break
    except:
        continue


row=1

for i in range(22125001,22125300):
    f = driver.page_source
    driver.find_elements(By.CLASS_NAME, 'form-control')[0].clear() 
    driver.find_elements(By.CLASS_NAME, 'form-control')[0].send_keys(i)
    driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div[1]/form/div/div[2]/div[2]/div/input')[0].click()

    etct=driver.page_source
    sp = BeautifulSoup(etct, "html.parser")
    text=sp.get_text()
    if  "Không tìm thấy kết quả tra cứu" not in text:
        text=text[text.find("báo")+3:text.find("©")]
        listinfo=list(line for line in text.split('\n') if line.strip() != '')
        print(listinfo)
        row+=1
        try:
            sheet.cell(row = row, column = 1).value = listinfo[2]#MSSV
            sheet.cell(row = row, column = 2).value = listinfo[1]#CCCD
            sheet.cell(row = row, column = 3).value = listinfo[3]#TEN
            sheet.cell(row = row, column = 4).value = listinfo[4]#NV
            sheet.cell(row = row, column = 5).value = listinfo[5]#NGHANH
            sheet.cell(row = row, column = 6).value = listinfo[7]#PHUONGTHUC
            sheet.cell(row = row, column = 7).value = listinfo[8]#GHICHU
        except:
            continue 
while True:
    try:
        wb.save("mtrg-clc.xlsx")
        break
    except:
        continue