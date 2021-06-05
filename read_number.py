import pytesseract
import cv2 as cv
from test import get_num_between, get_word_between
import os

image = cv.imread("money.jpg")
code_string = pytesseract.image_to_string(image, lang='chi_sim')

print(code_string)

# get_num_between(code, "收款金额", "汇总")
# get_word_between(code, "已存入", "的零钱")

money = get_num_between(code_string, "收款金额", "汇总")
name = get_word_between(code_string, "已存入", "的零钱")
time = get_num_between(code_string, "到账通知", "收款金额")
No = get_num_between(code_string, "今日第", "笔收款")

DATA_DIR = 'data/'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
f = open(DATA_DIR + 'wechat_money_data.txt', 'w')
f.write('Name\t\tMoney\t\tTime\t\tNo.')
f.write('\n')

f = open(DATA_DIR + 'wechat_money_data.txt', 'a')
f.write(name + '\t' + money + '\t\t' + time + '\t' + No)
f.write('\n')

f.close()





