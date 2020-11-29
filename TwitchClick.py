import pyautogui, time, winsound

# Update the path for the full file path where you save the ClickButon Img file
#Escape \ with an extra \
path = "D:\\ClickButton.png"

def findButton():
    try:
        find = pyautogui.locateCenterOnScreen(path)
    except:
        print("Error finding button")
    return find

def getMousePos():
    try:
        get = pyautogui.position()
    except:
        print("Get Mouse POS Error")
    return get

def click(x, y):
    pyautogui.click(x, y)

def move(x, y):
    pyautogui.moveTo(x, y)

def main():
    foundClick = 0
    while True:
        clickX, clickY, mouseX, mouseY = [0, 0, 0, 0] 
        print("Locating button")
        c = False
        while c == False:
            found = None
            found = findButton()
            print(found)
            # found = str(found)
            if found == None:
                c = False
                print('image not found')
                time.sleep(15.3)
            else:
                print('Image Found')
                try:
                    clickX, clickY = found
                except:
                    print("Assign click XY")
                print(clickX, clickY)
                try:
                    mouseX, mouseY = getMousePos()
                except:
                    print("get mouse pos error")
                try: 
                    move(clickX, clickY)
                    click(clickX, clickY)
                    click(clickX, clickY)
                except:
                    print("Error clicking button")
                try:
                    move(mouseX, mouseY)
                except:
                    print("Error returning mouse")
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                foundClick += 1
                break              
        print("Sleeping 15 seconds and running loop again")
        print("Buttons found and clicked: ", foundClick)
        time.sleep(15)



main()