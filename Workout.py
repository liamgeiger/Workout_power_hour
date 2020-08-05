# -*- coding: utf-8 -*-
"""
Created on Thurs Apr 16 2020

@author: liamg_000
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from itertools import repeat

#get email/passwords from text file
e = open("email.txt","r")
p = open("pw.txt","r")
user_email= e.read()
user_pw= p.read()
#Open up spotify web player in new chrome window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://open.spotify.com/')
#select/click login
login_button1 = driver.find_element_by_class_name('_2221af4e93029bedeab751d04fab4b8b-scss._1edf52628d509e6baded2387f6267588-scss')
login_button1.click()
#input email/password
time.sleep(6)
email = driver.find_element_by_id('login-username')
password = driver.find_element_by_id('login-password')
email.send_keys(user_email)
password.send_keys(user_pw)
#click login
login_button = driver.find_element_by_id('login-button')
login_button.click()
time.sleep(6)
#select playlist/play
#you must edit this string to your prefered playlist
playlist = driver.find_element_by_link_text('Letterkenny S1-8 - Updated')
playlist.click()
time.sleep(3)
play = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/div/div/div[2]/section/div[3]/div/button[1]')
play.click()
time.sleep(10)
#define skip button
skip = driver.find_element_by_class_name('control-button.spoticon-skip-forward-16')
pause = driver.find_element_by_class_name('control-button.spoticon-pause-16.control-button--circled')
time.sleep(54)
pause.click()
time.sleep(10)
skip.click()
#skip every 60 seconds
for i in repeat(None, 3):
    time.sleep(54)
    pause.click()
    time.sleep(10)
    skip.click()
print('congrats')