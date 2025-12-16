# import required packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#start the selenium browser session 
driver = webdriver.Chrome()


# load desired page in the browser
# time.sleep(5)
driver.get("https://duckduckgo.com/")

#access the controls on the page
time.sleep(5)

search_box = driver.find_element(By.Name,"q")

#interact with the control
#for ch in "dkte college ichalkaranji":
# search_box.send_keys(ch)
#time.sleep(0.2)

search_box.send_keys("dkte college ichalkaranji")
search_box.send_keys(Keys.RETURN)

# wait for the result
print("Later Page Title:", driver.title)

# stop the session
time.sleep(20)


