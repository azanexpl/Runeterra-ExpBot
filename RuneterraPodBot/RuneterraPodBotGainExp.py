import pyautogui


def nextStep(imgName):
    coords = pyautogui.locateCenterOnScreen(imgName)
    while coords is None:
        coords = pyautogui.locateCenterOnScreen(imgName)
        if coords is None:
            print('Nie znaleziono koordynatow!')
    pyautogui.leftClick(coords.x, coords.y)


def playSequence():
    nextStep('ready.png')
    nextStep('continue.png')


def startGame():
    nextStep('accept.png')
    nextStep('jinxDeck.png')


startGame()
while True:
    playSequence()