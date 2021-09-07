import os
import shutil
import time

#document is created separately to hold username and password
document = open('C://Users//MUTINTA//Pictures//InstaPassWord.txt')
username_Instagram = document.readline().rstrip()
passwordIns_Instagram = document.readline().rstrip()

#path of pictures
dir_path = 'ToPost//Pictures//'
dir_list = os.listdir(dir_path)
dir_list.sort()
print(dir_list)

#txt document of Instagram usernames. Will be used to tag people when posting pictures
document2 = open('ToPost//Usertags.txt')
usertags_total = document2.read().split('\n')

opening_message = ""    #Enter whatever message you want to the phot you're about to post
hastags = "\n\n\n #models #dfw #nikon #nikond750 #addisontx #getmoney #portrait #portrait_perfection #portrait_ig #portrait_shots"

#the next line is commented out in case you need to change the aspect ratio of the photos you're working with
"""
from PIL import Image
for image in os.listdir(dir_path):
    im = Image.open(dir_path + image)
    newsize = (1080, 1350)
    im1 = im.resize(newsize)
    im1.save(dir_path + "Resized_" + image)
"""


#you need to install instabot for this next part to work
from instabot import Bot

shutil.rmtree('config')
bot = Bot()

bot.login(username = username_Instagram, password = passwordIns_Instagram)
counter = 0

for image in os.listdir(dir_path):
    bot.upload_photo(dir_path + image, caption = opening_message + usertags_total[counter] + hastags)
    counter += 1
    print(f"Posted {image} successfully. Current number of successful posts is {counter}")
    time.sleep(1800)







