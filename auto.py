from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def dummy_sleep(sec, browser):
    wait = WebDriverWait(browser, 1)

    for i in range(sec):
        try:
            xpath = 'dummy'
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            pass

def main1():#リンククリック
    browser = webdriver.Chrome(executable_path="./chromedriver")#ブラウザのオブジェクトの作成

    # id input
    browser.get("https://*******************")#ge ブラウザが自動的に起動してURLにアクセスします
    xpath1 = '/html/body/app-root/div/div/app-login/div[3]/div/div[2]/div/div/form[1]/div[1]/div[1]/div[2]/input'
    elem = browser.find_element_by_xpath(xpath1)#cssセレクタメゾットにxpathのパスの文字列を代入
    elem.send_keys('*'+Keys.RETURN)
    dummy_sleep(3,browser)

    #password input
    xpath2 = '/html/body/app-root/div/div/app-login/div[3]/div/div[2]/div/div/form[1]/div[1]/div[2]/div[2]/input'
    elem = browser.find_element_by_xpath(xpath2)#cssセレクタメゾットにxpathのパスの文字列を代入
    elem.send_keys('*'+Keys.RETURN)
    dummy_sleep(10,browser)

    browser.close()
    browser.quit()#ブラウザを閉じる
main1()
