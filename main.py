from pynput.keyboard import Key,Controller
import time
import os

Keyboard = Controller()

print("Enter Count")
count = int(input())
print("Enter Message")
message = input()
print("Enter End Message")
endMessage = input()

n = 10

print("Spam Bot starting in" , n , "seconds...")

while n > 0:
    print(n)
    n -= 1
    time.sleep(1)
    os.system("cls")

print("Spam Bot is started...")


def send(message):
    for letter in message:
        Keyboard.press(letter)
        Keyboard.release(letter)

    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)


while count:
    send(message)
    time.sleep(0.1)
    count -= 1


send(endMessage)

os.system("cls")

print("Spam Bot is stopped...")