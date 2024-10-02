import  pytest
from    selenium  import  webdriver
# from tests.test import create_user, login_user, delete_user
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--headless')   
from    selenium.webdriver.common.by  import  By
from    faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(options=options)
driver.maximize_window()

def teardown(driver):
    driver.quit()

def create_user(user_name, user_email, user_password):
    driver.get("https://practice.expandtesting.com/notes/app/register")
    driver.find_element(By.CSS_SELECTOR, "#root > div > div > div").click()    
    assert driver.title == "Notes React Application for Automation Testing Practice"
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#email"))).send_keys(user_email)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#password"))).send_keys(user_password)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#confirmPassword"))).send_keys(user_password)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#name"))).send_keys(user_name)
    for x in range(5):
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "div.form-group > button").click()
    driver.implicitly_wait(2)
    user_created = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success > b").is_displayed()
    assert user_created == True

def login_user(user_email, user_password):
    driver.get("https://practice.expandtesting.com/notes/app/login")  
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys(user_email)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(user_password)
    for x in range(8):
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "div.form-group > button").click()
    driver.implicitly_wait(2)
    user_logged = driver.find_element(By.CSS_SELECTOR, "#navbarSupportedContent > ul > li:nth-child(1) > a").is_displayed()
    assert user_logged == True

def delete_user():
    driver.get("https://practice.expandtesting.com/notes/app/profile")
    for x in range(10):
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.DOWN)
    driver.find_element(By.CSS_SELECTOR, "div.row > div > button").click()
    driver.find_element(By.CSS_SELECTOR, "div.modal-footer > button.btn.btn-danger").click()
    driver.implicitly_wait(5)
    user_deleted = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div:nth-child(2) > div > div > div").is_displayed()
    assert user_deleted == True

