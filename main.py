"""
Goal is to create python project that will automatically post on instagram.
Considerations will be users to be tagged, hashtags per picture and how often to post.
Goal is a post an hour.
Phase 0 is to research tutorials/download the right modules for project                                 --- DONE
Phase 1 is to be able to simply post 1 picture.                                                         --- DONE
Phase 2 is to have python get all the pictures listed in a folder and add them to a list.
Phase 3 is to have the contents of a txt document (tags) be read by python and added to a list.
Phase 4 is to have python be able to upload a picture, wait 5 minutes and then post another picture.
Phase 5 is to have python get photo/tag information, and then be able to post once an hour.
"""

document = open('C://Users//MUTINTA//Pictures//InstaPassWord.txt')
username_Instagram = document.readline().rstrip()
passwordIns_Instagram = document.readline().rstrip()

print(username_Instagram)
print(passwordIns_Instagram)

from instabot import Bot

bot = Bot()

bot.login(username = username_Instagram, password = passwordIns_Instagram)

bot.upload_photo("C://Users//Mutinta//Pictures//MOTIVATION//y10ZTCG.jpg", caption = "This is a test, kindly ignore")