from selenium import webdriver
import pytest

#prep
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/study_pystuff/test_heroku_0/test_heroku_0/chromedriver.exe")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test Done!")

#tests
# 1) successful login check
def test_login(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("tomsmith")
    driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_class_name("radius").click()

    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "You logged into a secure area!" in element_text
    
# 2) fake username check
def test_fake_username(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("tomjones")
    driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_class_name("radius").click()
        
    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "Your username is invalid!" in element_text

# 3) fake password check
def test_fake_password(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("tomsmith")
    driver.find_element_by_id("password").send_keys("SuperFakePassword!")
    driver.find_element_by_class_name("radius").click()
    
    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "Your password is invalid!" in element_text
    
# 4) successful logout check
def test_logout(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("tomsmith")
    driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_class_name("radius").click()

    driver.find_element_by_xpath('//*[@id="content"]/div/a').click() #2nd button

    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "You logged out of the secure area!" in element_text

# 5) emptiness of username field check
def test_empty_username(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("")
    driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_class_name("radius").click()

    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "Your username field is empty!" in element_text

# 6) emptiness of password field check
def test_empty_password(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("tomsmith")
    driver.find_element_by_id("password").send_keys("")
    driver.find_element_by_class_name("radius").click()

    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "Your password field is empty!" in element_text

# 7) emptiness of username & password fields check
def test_empty_username_and_password(test_setup):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("")
    driver.find_element_by_id("password").send_keys("")
    driver.find_element_by_class_name("radius").click()

    element = driver.find_element_by_xpath('//*[@id="flash"]')
    element_text = element.text
    assert "Your username and password fields are empty!" in element_text
