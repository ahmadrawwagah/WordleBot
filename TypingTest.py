from importlib.machinery import BYTECODE_SUFFIXES
import time
from wsgiref.simple_server import WSGIRequestHandler
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def checkLet (temprow):
    correct = []
    present = []
    exclude = []
    tempI = 0
    for i in temprow:
        temp = i.get_attribute('evaluation')
        if temp == "correct":
            correct.append([i.get_attribute('letter'),tempI])
        if temp == "present":
            present.append([i.get_attribute('letter'),tempI])
        elif temp == "absent":
            exclude.append(i.get_attribute('letter'))
        tempI += 1
    return correct,present,exclude

def sendWord (actions,word):
    actions.send_keys(word).perform()
    actions.send_keys(Keys.ENTER).perform()

def getRow(gameapp,index):
    sone = gameapp.shadow_root
    gametheme = sone.find_element(By.CSS_SELECTOR, 'game-theme-manager')
    board = gametheme.find_element(By.CSS_SELECTOR,'#game').find_element(By.CSS_SELECTOR,'#board-container').find_element(By.CSS_SELECTOR,'#board')
    rows = board.find_elements(By.CSS_SELECTOR,'game-row')
    gamerowone = rows[index]
    stwo = gamerowone.shadow_root
    row = stwo.find_element(By.CSS_SELECTOR,'.row').find_elements(By.CSS_SELECTOR,'game-tile')
    return row

driver = webdriver.Chrome()
driver.get('https://www.powerlanguage.co.uk/wordle/')
actions = ActionChains(driver)


gameapp = driver.find_element(By.TAG_NAME,'game-app')
webdriver.ActionChains(driver).click_and_hold(gameapp).perform()
webdriver.ActionChains(driver).release().perform()

sendWord(actions, 'adieu')
row = getRow(gameapp,0)
correct,present,exclude = checkLet(row)
print(correct)
print(present)
print(exclude)

time.sleep(3)

sendWord(actions, 'proxy')
row = getRow(gameapp,1)
correct,present,exclude = checkLet(row)
print(correct)
print(present)
print(exclude)

time.sleep(3)

sendWord(actions, 'point')
row = getRow(gameapp,2)
correct,present,exclude = checkLet(row)
print(correct)
print(present)
print(exclude)





