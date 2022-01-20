from importlib.machinery import BYTECODE_SUFFIXES
import random
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

def sendWord (word):
    actions.send_keys(word).perform()
    actions.send_keys(Keys.ENTER).perform()

def getRow(index):
    gameapp = driver.find_element(By.TAG_NAME,'game-app')
    sone = gameapp.shadow_root
    gametheme = sone.find_element(By.CSS_SELECTOR, 'game-theme-manager')
    board = gametheme.find_element(By.CSS_SELECTOR,'#game').find_element(By.CSS_SELECTOR,'#board-container').find_element(By.CSS_SELECTOR,'#board')
    rows = board.find_elements(By.CSS_SELECTOR,'game-row')
    gamerowone = rows[index]
    stwo = gamerowone.shadow_root
    row = stwo.find_element(By.CSS_SELECTOR,'.row').find_elements(By.CSS_SELECTOR,'game-tile')
    return row

def removeInvalid(dicto,correct,present,absent):
    iterdict =[]
    for i in dicto:
        abs = 1
        cor = 1
        pre = 1
        for letter in absent:
            if letter in i:
                abs = 0
                break
        
        for j in correct:
            if j[0] != i[j[1]]:
                abs = 0
                break

        for k in present:
            if k[0] not in i or k[0] == i[k[1]]:
                pre = 0
                break
        if abs and cor and pre:
            iterdict.append(i)
    return iterdict


driver = webdriver.Chrome()
driver.get('https://www.powerlanguage.co.uk/wordle/')
actions = ActionChains(driver)


gameapp = driver.find_element(By.TAG_NAME,'game-app')
webdriver.ActionChains(driver).click_and_hold(gameapp).perform()
webdriver.ActionChains(driver).release().perform()

with open('WordBank.txt', 'r') as f:
    dicto = [line.strip() for line in f]

sendWord('tares')

iter = 0
while(iter <= 6):
    row = getRow(iter)
    cor,pre,exc = checkLet(row)
    if (len(cor) == 5):
        break
    dicto = removeInvalid(dicto,cor,pre,exc)
    guess = random.choice(dicto)
    #guess = dicto[0]
    time.sleep(2)
    sendWord(guess)
    print(dicto)
    dicto.remove(guess)
    iter += 1













