#Author:Aakash
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import random
import json
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=<User Data Path>')
options.add_argument('--profile-directory=Default')
browser = webdriver.Chrome(executable_path=r'C:\Users\USER\Downloads\chromedriver_win32\chromedriver',options = options)
browser.get("https://web.whatsapp.com")
page_source = browser.page_source
#20seconds for scanning qr code
time.sleep(20)
soup = BeautifulSoup(page_source, 'html.parser')
	
def send_msg(name,msg):
	browser = webdriver.Chrome(executable_path=r'C:\Users\USER\Downloads\chromedriver_win32\chromedriver')
	browser.get("https://web.whatsapp.com")
	page_source = browser.page_source
	time.sleep(20)
	soup = BeautifulSoup(page_source, 'html.parser')
	
	try:
		user = browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
		user.click()
		msg_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2][@class="{}"]'.format('_1awRl copyable-text selectable-text'))
		msg_box.send_keys(msg)
		msg_button = msg_box.find_element_by_xpath('//button[@class="{}"]'.format('_2Ujuu'))
		msg_button.click()	
	except  NoSuchElementException as nse:
		search_bar =  browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2][@class="{}"]'.format('_1awRl copyable-text selectable-text'))
		search_bar.send_keys(name)
		time.sleep(3)
		try:
			user = browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
			user.click()
			msg_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2][@class="{}"]'.format('_1awRl copyable-text selectable-text'))
			msg_box.send_keys(msg)
			msg_button = msg_box.find_element_by_xpath('//button[@class="{}"]'.format('_2Ujuu'))
			msg_button.click()
		except NoSuchElementException:
			print("Not able to find the person in your contact list")
def msg_status():
	
	div = soup.find('div',class_="_3soxC _2aY82")
	chat_list = div.find_all('div',class_="_1C6Zl")
	unread_msg=[]
	for div in chat_list:
		
		div2 = div.find('span',class_="_1hI5g _1XH7x _1VzZY").text
		
		try:
			div3 = div.find('span',class_="VOr2j").text
			unread_msg.append({"name":div2,"unread":div3})
		except:
			unread_msg.append({"name":div2,"unread":0})
			pass

	return unread_msg	
def caption():
	with open(r"F:\Python projects\Desktop Background\quotes.json") as file:
		quotes = json.load(file)
	length = 0
	while length == 0:
		quote = random.choices(quotes)
		text = quote[0]['text']
		if len(text)<120:
			length=1
	
	
	profile = browser.find_element_by_xpath('//*[@id="side"]/header/div[1]/div/img[@class="{}"]'.format('_3t3gU rlUm6 _1VzZY'))
	
	profile.click()
	time.sleep(5)
	about_icon_div = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4][@class="{}"]'.format("_32vnm _2k4Ax _2zqsv"))
	about_icon = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div[@class="{}"]'.format("_9uumR"))
	about_icon.click()
	about = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/div/div[2][@class="{}"]'.format("_1awRl copyable-text selectable-text"))
	about.clear()
	about.send_keys(text)
	checker = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/div/div/div[4]/div[2]/div[1]/span[2]/div[@class="{}"]'.format("_9uumR"))
	checker.click()
	
