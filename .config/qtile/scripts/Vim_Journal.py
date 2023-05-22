import os
import datetime

now = datetime.datetime.now()
os.system("alacritty -e nvim ~/Documents/Second\ brain/Journals/Daily\ Jorunal/%s-%s-%s.md" %
          (now.year, now.month, now.day))

# os.system( "alacritty -e nvim ~/Documents/Second\ brain/Journals/Daily\ Jorunal/2022-10-30.md")
# print(now.date())
# print("Current date is %s-%s-%s" % (now.year, now.month, now.day))
