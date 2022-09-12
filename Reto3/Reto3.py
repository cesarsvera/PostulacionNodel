from msilib.schema import Error
import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# Coloca el Chromo Drive
driver = webdriver.Chrome(ChromeDriverManager().install())
# Ingreso del link de la pagina a manejar
driver.get("http://www.pbclibrary.org/raton/mousercise.htm")
act = ActionChains(driver)
# Reglas de cada pagina
reglas = {
    1: "//input",
    2: "//a",
    3: "//a",
    4: "//a",
    5: "//a",
    6: "//a",
    7: "//a",
    8: "//a",
    9: "//a",
    10: "9",
    11: "10",
    12: "11",
    13: "12",
    14: "13",
    15: "//a",
    16: "//a",
    17: "//input",
    18: "//input",
    19: "//button",
    20: "//input",
    21: "//a",
    22: "//a",
    23: ["//tr[2]//td[1]/img","//tr[2]//td[2]/img","//tr[2]//td[3]/img","//tr[2]//td[4]/img","//tr[2]//td[5]/img","//tr[2]//td[6]/img","//tr[2]//td[7]/img","//tr[2]//td[8]/img","//tr[2]//td[9]/img","//tr[2]//td[10]/img","//tr[2]//td[11]/img","//a"],
    24: ["//tr[2]/td[1]/form/input","//tr[2]/td[3]/form/input","//tr[3]/td[1]/form/input","//tr[3]/td[3]/img","//tr[4]/td[1]/img", "//tr[4]/td[3]/img", "//tr[5]/td[1]/img", '//a'],
    25: ["//tr[2]/td[1]/img", "//tr[2]/td[2]/img", "//tr[2]/td[3]/img", "//tr[2]/td[4]/img", "//tr[3]/td[1]/img", "//tr[3]/td[2]/img", "//tr[3]/td[3]/img", "//tr[3]/td[4]/img", "//a"],
    26: ["//*[@id='red-slider']/div[2]","//*[@id='green-slider']/div[2]", "//*[@id='blue-slider']/div[2]", "//a"],
    27:"//a",
    28:"//a",
    29:"//a",
    30:"//a",
    31:"//a",
    32:"//a",
    33:"//a",
    34: ["//input[1]", "//input[2]","//input[3]","//input[4]","//input[5]","//input[6]","//input[7]","//input[8]","//input[9]", "//a"],
    35: ["//input[3]","//input[1]","//input[4]", "//input[7]"],
    36: ["//input[1]", "//input[2]","//input[3]","//input[4]","//input[5]","//input[6]","//input[7]","//input[8]","//input[9]", "//a"],
    37: ["//input[2]","//input[5]"],
    38: ["//select", "//select/option[6]", "//a"],
    39: ["//select", "//select/option[2]", "//input"],
    40: ["//option[6]", "//a"],
    41: ["//option[3]","//input"],
    42: ["//input[1]", "//input[2]", "//input[3]"]
    

}

claves = list(reglas.keys())
# Codigo de para el manejo en cada pagina
for i in range(1,len(claves)+1):
    print(i)
    if  1<=i<=9 or 15<=i<=22 or i ==33:
        
        web_element = driver.find_element(By.XPATH, str(reglas.get(i)))
        web_element.click()
        time.sleep(1)
    if 10<=i <=14:
        
        web_element = driver.find_element(By.LINK_TEXT, str(reglas.get(i)))
        web_element.click()
        time.sleep(1)
    if 23<=i<=24 or 34<=i <= 41:
        for c in reglas.get(i):
            web_element = driver.find_element(By.XPATH, str(c))
            
            web_element.click()
            time.sleep(1)
    if i == 25:
        for c in reglas.get(i):
            web_element = driver.find_element(By.XPATH, str(c))
            act.double_click(web_element).perform()
            time.sleep(1)
    if i == 26:
        cont =0
        for c in reglas.get(i):
            web_element = driver.find_element(By.XPATH, str(c))
            if cont == 2:
                web_element.click()
                time.sleep(1)
            else:
                act.click_and_hold(web_element).move_to_element_with_offset(web_element,0, 24).click().perform()
                time.sleep(1)
                cont+=1
    if 27<=i<=29 :
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        web_element = driver.find_element(By.XPATH, str(reglas.get(i)))
        web_element.click()
        time.sleep(1)
    if i == 30:
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        time.sleep(1)
        web_element = driver.find_element(By.XPATH, str(reglas.get(i)))
        web_element.click()
        time.sleep(1)
    if i ==31:
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        web_element = driver.find_element(By.XPATH, str(reglas.get(i)))
        web_element.click()
        time.sleep(1)
    if i ==32:
        web_element = driver.find_element(By.XPATH, str(reglas.get(i)))
        web_element.click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)
    if i ==42:
        contador =0
        for c in reglas.get(i):
            web_element = driver.find_element(By.XPATH, str(c))
            if contador ==0:
                web_element.send_keys("Cesa Steven")
                time.sleep(1)
            elif contador == 1:
                web_element.send_keys("Cesa Steven")
                time.sleep(1)
            else:
                web_element.click()
                time.sleep(1)
            contador+=1


    



