from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import numpy as np
import time
driver = webdriver.Chrome()
driver.get("https://www.smartprix.com/mobiles/exclude_out_of_stock-exclude_upcoming-stock")
    
time.sleep(2)
old_height=driver.execute_script("return document.body.scrollHeight")
print(old_height)
while True:
    # driver.execute_script(f"window.scrollTo(0,document.body.scrollHeight*(3/5))")
    try:
        driver.implicitly_wait(4)
        load=driver.find_element(by=By.CLASS_NAME,value="sm-load-more")
        load.click()
       
    except Exception as e:
    # e captures the error details automatically
        print(f"An unexpected error occurred: {e}")
    time.sleep(2)
    
    new_height=driver.execute_script("return document.body.scrollHeight")
    if (new_height==old_height):
        break
    print("new heght:",new_height," old height:",old_height,old_height==new_height )
    
    old_height=new_height
    
html=driver.page_source
with open("smart_phone.html","w",encoding="utf-8") as f:
    f.write(html)




input("Press Enter to close the browser...")