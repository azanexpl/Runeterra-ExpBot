import pyautogui
import time

def nextStep(imgName):
    coords=pyautogui.locateCenterOnScreen(imgName)
    x, y = pyautogui.position()
    while coords is None:
        x, y = pyautogui.position()
        coords = pyautogui.locateCenterOnScreen(imgName)
    if coords is not None:
        pyautogui.leftClick(coords.x, coords.y)
    pyautogui.moveTo(x, y)
        
def nextStep2(imgName, imgName2):
    coords=pyautogui.locateCenterOnScreen(imgName)
    coords2=pyautogui.locateCenterOnScreen(imgName2)
    x, y = pyautogui.position()
    while coords is None and coords2 is None:
        x, y = pyautogui.position()
        coords = pyautogui.locateCenterOnScreen(imgName)
        coords2 = pyautogui.locateCenterOnScreen(imgName2)
    if coords is not None:
        pyautogui.leftClick(coords.x, coords.y)
    else:
        pyautogui.leftClick(coords2.x, coords2.y)
    pyautogui.moveTo(x, y)

def startGame():
    nextStep('gameIcon.png')
    nextStep2('playButton.png', 'playButton2.png')

def playSequence():
    jestemZmeczony = False
    nextStep2('playButtonGame.png', 'playButtonGame2.png')
    nextStep('settings.png')
    nextStep('surrender.png')
    nextStep('ok.png')
    time.sleep(8)
    if pyautogui.locateCenterOnScreen('isExhausted.png'):
        jestemZmeczony = True
    nextStep('continue.png')
    if jestemZmeczony is True:
        return True
    else:
        return False

def playGamesAI():
    aiExpExhausted = False
    nextStep2('vsAI.png', 'vsAI2.png')
    nextStep2('jinxDeck.png', 'jinxDeck2.png')
    while aiExpExhausted is False:
        aiExpExhausted = playSequence()

def playGamesPlayer():
    playerExpExhausted = False
    nextStep('vsPlayerDark.png')
    nextStep2('vsPlayer.png', 'vsPlayer2.png')
    nextStep2('jinxDeck.png', 'jinxDeck2.png')
    while playerExpExhausted is False:
        playerExpExhausted = playSequence()

startGame()
playGamesAI()
playGamesPlayer()