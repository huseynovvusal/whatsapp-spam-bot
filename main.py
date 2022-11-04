import pyautogui
import time
import os


count = int(input("Enter Count : "))
message = input("Enter Message : ")
endMessage = input("Enter End Message If You Want : ")

n = 10

print("Spam Bot starting in" , n , "seconds...")

while n > 0:
    print(n)
    n -= 1
    time.sleep(1)
    os.system("cls")

print("Spam Bot is started...")


def send(message):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")


while count:
    send(message)
    time.sleep(0.1)
    count -= 1


send(endMessage)

os.system("cls")

print("Spam Bot is stopped...")