# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 22:03:25 2021

@author: Calven
"""

from selenium import webdriver
import time
#from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pandas as pd

    
driver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')


inf_list = []


url = "https://www.instagram.com/"
driver.get(url)

#login
time.sleep(5)
username=driver.find_element_by_css_selector("input[name='username']")
password=driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("username")
password.send_keys("password")
login = driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(5)

#save your login info?
alert = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

alert2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

user_list = [
""
]


for user in user_list:
    url = "https://www.instagram.com/" + user + "/"

    driver.get(url)

    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    body = soup.find('body')
    script = body.find('script')
    page_json = script.text.strip().replace('window._sharedData =', '').replace(';', '')


    elem = driver.find_element_by_tag_name("body")
    """
    no_of_pagedowns = 20

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1
    """
    
# Get 12 latest posts
    d = []
    data = json.loads(page_json)
    follower = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
    post_count = 0
    
    for post in data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']:
        timestamp = post['node']['taken_at_timestamp']
        likedby = post['node']['edge_liked_by']['count']
        comments = post['node']['edge_media_to_comment']['count']
        isVideo = post['node']['is_video']
        caption = post['node']['edge_media_to_caption']
        
        postdate = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print('Liked by :',likedby)
        print('comments :',comments)
        print('caption :',caption)
        
        try:
            captionText = caption.get('edges')[0].get('node').get('text')
        except IndexError:
            captionText = ""
        inf_list.append({'User': user, 'Followers':follower, 'Postdate': postdate, 'Likes': likedby, 'Comments':comments,'Caption':captionText, 
                         'Industry':'General', 'Country':'Singapore'})

        post_count += 1
        
        if post_count ==12:
            break
        time.sleep(3)
    
        
    time.sleep(45)

real_df = pd.DataFrame(inf_list)
real_df.to_csv('influencer.csv', mode='a', header=False)

