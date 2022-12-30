from selenium import webdriver
import time
import pyqt
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
hedef = pyqt.ad
sayi = int(pyqt.gonderilecek_sayi)
FotoURL = pyqt.link
print(hedef, "kişisine seçtiğiniz fotoğraf ile", sayi, "kez saldırılıyor...")

while True:
    try:
        hedefson = driver.find_element(by="xpath", value='//*[@title="%s"]' % hedef).click()
        break
    except:
        hedef = hedef.capitalize()
        

#----------------------------------------------------------------------------------------------------------------------------------------------------------

driver.switch_to.new_window('tab')
driver.get(FotoURL)
foto = driver.find_element("xpath", "/html/body/img")
pyautogui.click(button='right', x=495, y=560)
pyautogui.press(['down', 'down', 'down', "enter"])
pyautogui.hotkey("ctrl", "1")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

WebDriverWait
time.sleep(2)
for i in range(sayi):
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.6)
              
time.sleep(2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(0.1)
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
driver.quit
print("Saldırı tamamlandı")
time.sleep(7)
