from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

prod = "DSLR"
top10 = {}
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)
driver.get("https://www.flipkart.com")
wait.until(EC.visibility_of_element_located((By.XPATH, '(//button)[2]')))
time.sleep(2)
close = driver.find_element(By.XPATH, "(//button)[2]")
close.click()

inputprod = driver.find_element(By.NAME, "q")
inputprod.send_keys(prod)
search = driver.find_element(By.XPATH, '//form//button')
search.click()

for i in range(1, 11):
    pathName = '(//a//div[contains(text(),"Camera")])[' + str(i) + ']'
    pathPrice = '(//a/div[2]/div[2]/div[1]/div[1]/div[1])[' + str(i) + ']'
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, pathName)))
    pname = driver.find_element(By.XPATH, pathName).text
    pprice = driver.find_element(By.XPATH, pathPrice).text[1:]
    pprice = pprice.replace(",", "")
    top10[pname] = int(pprice)

print(type(top10))
print(top10)
# sorteddict = sorted(top10.items(), key=lambda kv: (kv[1], kv[0]))
top10list=list(top10.items())
print("------------"+str(top10list))
n = len(top10list)
for i in range(n-1):
    for j in range(i+1, n):
        if top10list[i][1] > top10list[j][1]:
            t = top10list[i]
            top10list[i] = top10list[j]
            top10list[j]=t
sortdict = dict(top10list)
keylist = list(sortdict.keys())
vallist = list(sortdict.values())
for i in range(0, 10):
    print(i+1, ") ", keylist[i], "\n", vallist[i])
