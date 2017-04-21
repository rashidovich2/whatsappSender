from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, sys, os
import argparse as arg

parser = arg.ArgumentParser()
parser.add_argument('-t','--target', help='enter the name you want to send message to', required=True)
content = parser.add_mutually_exclusive_group()
content.add_argument('--messages', nargs='+', help='enter messages in quotes seperated by space')
content.add_argument('--file', help='enter absolute location of the file')
args = parser.parse_args()

def openWebWhatsapp(driver):
	driver.get('https://web.whatsapp.com/')

def sendMedia(target, file):
	wait = WebDriverWait(driver, 600)
	sidebar_locate = '//span[contains(@title, "' + target + '")]'
	chat_window = wait.until(EC.presence_of_element_located((By.XPATH, sidebar_locate)))
	chat_window.click()
	attach_locate = '//button[@title="Attach"][@class="icon icon-clip"]'
	attach = wait.until(EC.presence_of_element_located((By.XPATH, attach_locate)))
	attach.click()
	media_locate = '//input[@type="file"][@accept="image/*,video/*"]'
	media = wait.until(EC.presence_of_element_located((By.XPATH, media_locate)))
	media.send_keys(file)
	send_locate = '//button[@class="btn btn-round btn-l"]'
	send = wait.until(EC.presence_of_element_located((By.XPATH, send_locate)))
	send.click()

def sendText(target, *message):
	wait = WebDriverWait(driver, 600)
	sidebar_locate = '//span[contains(@title, "' + target + '")]'
	chat_window = wait.until(EC.presence_of_element_located((By.XPATH, sidebar_locate)))
	chat_window.click()
	input_locate = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
	input_box = wait.until(EC.presence_of_element_located((By.XPATH, input_locate)))

	for i in range(len(args.messages)):
		input_box.send_keys(args.messages[i] + Keys.ENTER)
		time.sleep(1)

driver = webdriver.Chrome('/home/vpatel95/Downloads/chromedriver')
openWebWhatsapp(driver)
if args.messages:
	sendText(args.target, args.messages)
if args.file:
	sendMedia(args.target, args.file)


