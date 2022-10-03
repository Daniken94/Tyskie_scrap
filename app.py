from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Creating webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(10) # wait max 10 seconds to load DOM
driver.get('https://browarytyskie.pl/')

# Accept all cookies

cookie = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="button--component acceptAll"]')))
cookie.click()

# Fill verification age form, check remember me and entry to website

age_verification_day = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@name="gate[day]"]')))
age_verification_day.send_keys("20")
age_verification_month = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@name="gate[month]"]')))
age_verification_month.send_keys("05")
age_verification_year = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@name="gate[year]"]')))
age_verification_year.send_keys("1994")

remember_me = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@name="gate[rememberme]"]')))
remember_me.click()

entry = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="btn btn--red-full btn--big"]')))
entry.click()

# Scrapping data
# Website title

print("********************")
print(driver.title)
print("********************")

# Titles from slick list. This titles has got href to another page

titles = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="slick-track"]')))
print(titles.text)
print("********************")

# Scrap titles and text from carousel articles
# Get one article and spin carousel until the result is the same as the first

title_art_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="banner slick-slide slick-current slick-active"]')))
print(title_art_1.text)

title_art_2 = ""

if title_art_1 != title_art_2:
    next_slide = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="btn btn--red-full slick-arrow--next slick-arrow"]')))
    next_slide.click()

    title_art_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="banner slick-slide slick-current slick-active"]')))

    if title_art_2 != title_art_1:
        print("********************")
        print(title_art_2.text)
    else:
        driver.quit()


driver.quit()


