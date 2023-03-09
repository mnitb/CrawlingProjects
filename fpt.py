import warnings, time, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings("ignore", category=DeprecationWarning)
options = Options()
options.add_argument("--log-level=3")
options.add_argument("--mute-audio")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_extension("adblocker.crx")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", options=options)


driver.get("https://10fastfingers.com/typing-test/vietnamese")

while True:
	os.system("cls")
	sl = input("press enter to start this sheeeet")
	if sl=="": check=True
	else: check=False
	f = driver.page_source
	soup = BeautifulSoup(f, "html.parser")
	n1 = soup.find("div", {"id": "row1"})
	ipf = driver.find_element_by_id("inputfield")
	for i in n1:
		print([i.text][0], end="\n")
		time.sleep(59/len(n1))
		for j in i.text:
			ipf.send_keys(j)

	"""while int(driver.find_element_by_id("timer").text[2:])>5:
		print(driver.find_element_by_id("timer").text[2:])
		ipf.send_keys(" ")
		time.sleep(2)"""
