# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class TestSmokeTests():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adminPage(self):
    self.driver.get("https://ross-owen.github.io/cse270-teton")
    self.driver.set_window_size(1325, 792)
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("bad-username")
    self.driver.find_element(By.ID, "password").send_keys("bad-password")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    WebDriverWait(self.driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".errorMessage"), "Invalid username and password."))
  
  def test_commonHeader(self):
    self.driver.get("https://ross-owen.github.io/cse270-teton/")
    self.driver.set_window_size(1038, 672)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title > h1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-title > h2")
    assert len(elements) > 0
    assert self.driver.title == "Teton Idaho CoC"
  
  def test_directoryPage(self):
    self.driver.get("https://ross-owen.github.io/cse270-teton/")
    self.driver.set_window_size(1237, 777)
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
  
  def test_homePage(self):
    self.driver.get("https://ross-owen.github.io/cse270-teton/")
    self.driver.set_window_size(1140, 802)
    self.driver.find_element(By.CSS_SELECTOR, ".header-top").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".main-news > h3")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > h4")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
  
  def test_joinPage(self):
    self.driver.get("https://ross-owen.github.io/cse270-teton/")
    self.driver.set_window_size(1479, 802)
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("Ross")
    self.driver.find_element(By.NAME, "lname").send_keys("Owen")
    self.driver.find_element(By.NAME, "bizname").send_keys("My Owen Business")
    self.driver.find_element(By.NAME, "biztitle").send_keys("Manager")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
  