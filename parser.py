from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()


try:
    driver.get(url='https://chaika.am/hy/doctors')
    time.sleep(3)
    dc_name = driver.find_elements(By.CLASS_NAME, 'dc__name')
    df_prof = driver.find_elements(By.CLASS_NAME, 'dc__specs')
    for i, j in zip(dc_name, df_prof):
        print(f'{i.text} --> {j.text}')
        print('----------------------------------------------')
except Exception as ex:
    print(ex.__class__.__name__)
finally:
    driver.close()
    driver.quit()