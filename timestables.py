# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 21:31:40 2022

@author: louis
"""

#Enter your username here
user='louis'

import pandas
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()

options.add_argument("start-maximized") #Forces chrome to start maximised

#Removes chrome being controlled by automated software warning. 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#Gathering user data
options.add_argument(r"user-data-dir=C:\Users\louis\AppData\Local\Google\Chrome\chromedriver")

#Directs python to webdriver location
driver = webdriver.Chrome(executable_path=r'./chromedriver_win32/chromedriver.exe', options=options)
driver.get('https://www.drfrostmaths.com/dashboard.php')#Launches webdriver

#function that click on an object
def click(type, string):
    button = driver.find_element(type, string)
    button.click()
    
def getanswer(type, string):
    data = driver.find_element(type, string)
    question = data.get_attribute('innerHTML')
    print(question)
    question = question.replace(" ÷ ", "/")
    question = question.replace(" × ", "*")
    print(question)
    answer = pandas.eval(question)
    print(answer)
    return answer

#opens menu
click('xpath', '//*[@id="mainmenu-button"]')

#clicks start practice
click('xpath', '//*[@id="dashboard-practicebutton"]')       

#clicks practice
click('xpath', '//*[@id="practice-timestables"]')
click('xpath', '//*[@id="homework-type-selection"]/div/div[1]/button')

#clicksstart
click('xpath', '//*[@id="question"]/a')
time.sleep(2) #program waits so dr frost can update

#works out answer
#getanswer('xpath', '//*[@id="question"]')

"""
#prepares to type answer in
click('xpath', '//*[@id="calculator-display"]')

#types answer
answerbox = driver.find_element("xpath", '//*[@id="calculator-display"]')
answerbox.send_keys(str(answer)) 
time.sleep(0.1)#program waits so dr frost can update
"""

for score in range(20):
    time.sleep(0.5)#program waits so dr frost can update
    #works out answer
    #getanswer('xpath', '//*[@id="question"]')
    data = driver.find_element('xpath', '//*[@id="question"]')
    question = data.get_attribute('innerHTML')
    print(question)
    question = question.replace(" ÷ ", "/")
    question = question.replace(" × ", "*")
    print(question)
    answer = pandas.eval(question)
    print(answer)
    #prepares to type answer in
    click('xpath', '//*[@id="calculator-display"]')
    answer=str(answer)
    #question = question.replace(".0", "")
    #types answer
    answerbox = driver.find_element("xpath", '//*[@id="calculator-display"]')
    answerbox.send_keys(answer) 
