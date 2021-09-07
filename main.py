"""
Goal is to create python project that will automatically post on instagram.
Considerations will be users to be tagged, hashtags per picture and how often to post.
Goal is a post an hour.
Phase 0 is to research tutorials/download the right modules for project                                 --- DONE
Phase 1 is to be able to simply post 1 picture.                                                         --- DONE
Phase 2 is to have python get all the pictures listed in a folder and add them to a list.               --- DONE
Phase 3 is to have the contents of a txt document (tags) be read by python and added to a list.         --- DONE
Phase 4 is to have python be able to upload a picture, wait 5 minutes and then post another picture.    --- DONE
Phase 5 is to have python get photo/tag information, and then be able to post once an hour.             --- DONE
"""
import os
import shutil
import time

document = open('C://Users//MUTINTA//Pictures//InstaPassWord.txt')
username_Instagram = document.readline().rstrip()
passwordIns_Instagram = document.readline().rstrip()

dir_path = 'ToPost//Pictures//'
dir_list = os.listdir(dir_path)
dir_list.sort()
print(dir_list)

document2 = open('ToPost//Usertags.txt')
usertags_total = document2.read().split('\n')

opening_message = "Meetup for charity, hosted by **********\nModel:  "
hastags = "\n\n\n #models #dfw #nikon #nikond750 #addisontx #getmoney #portrait #portrait_perfection #portrait_ig #portrait_shots"

"""
from PIL import Image
for image in os.listdir(dir_path):
    im = Image.open(dir_path + image)
    newsize = (1080, 1350)
    im1 = im.resize(newsize)
    im1.save(dir_path + "Resized_" + image)
"""



from instabot import Bot

shutil.rmtree('config')
bot = Bot()

bot.login(username = username_Instagram, password = passwordIns_Instagram)
counter = 0

for image in os.listdir(dir_path):
    bot.upload_photo(dir_path + image, caption = opening_message + usertags_total[counter] + hastags)
    counter += 1
    print(f"Printed...{image} and on number {counter}")
    time.sleep(1800)







