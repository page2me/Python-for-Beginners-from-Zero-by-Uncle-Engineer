from songline import Sendline

token = 'cpLF1uCJ55bYxeq5J43JlpAQ7xRAVfCnTeujCsdoCyg'
messenger = Sendline(token)

#send message
messenger.sendtext('ดาวโหลดตารางสติกเกอร์: http://cons-robotics.com/LINEAPI/sticker.pdf')

#send sticker
messenger.sticker(255,3)

#send image
messenger.sendimage('https://e7.pngegg.com/pngimages/730/59/png-clipart-bacteria-microorganism-computer-icons-biology-bacteria-miscellaneous-text.png')
