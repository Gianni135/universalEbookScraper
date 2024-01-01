import pyautogui
import os
from PIL import Image
from time import sleep
pyautogui.FAILSAFE = False

def countdown(secondsBeforeCountDown, countdownDuration):
    sleep(secondsBeforeCountDown)
    for i in range(1,countdownDuration+1)[::-1]:
        print(str(i) + " seconds remaining...")
        sleep(1)

print("Position your cursor on the top left corner of the first page")
countdown(3, 5)
x1, y1 = pyautogui.position()
print("Top left corner position acquired: " + str(x1) + ' ' + str(y1))

print("Position your cursor on the bottom right corner of the page")
countdown(3, 5)
x2, y2 = pyautogui.position()
print("Bottom right corner position acquired: " + str(x2) + ' ' + str(y2))

screenshotList = []
numOfPages = int(input("Enter the number of pages: "))
pageLoadTime = int(input("Enter the wait time in seconds for the next page to be loaded (default=10): "))
print("Position your cursor on next page button and and don't move it until the capture process is completed")
countdown(3, 5)
 
if not os.path.exists("./images"):
    os.makedirs("./images") 

for i in range(numOfPages):
    myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    myScreenshot.save(r'./images/page' + str(i+1) + '.png')
    screenshotList.append('page' + str(i+1) + '.png')
    print("Page " + str(i+1) + " Acquired")
    pyautogui.click() #go to the next page
    sleep(pageLoadTime)

images = [
    Image.open("./images/" + f)
    for f in screenshotList
]
pdf_path = "./book.pdf"

images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
