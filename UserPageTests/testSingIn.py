from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#тестирование регистрации пользователя
class TestSingIn(unittest.TestCase):

    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr + "/login")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


    #переход по ссылкам из регистрации
    def testRegistrationRefs(self):
        driver = self.driver

        refRegister = driver.find_element_by_xpath("//*[@id=\"app\"]/div/form/form/div[2]/p/a/a")
        refRegister.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, (self.networkAdr + "/register"))
        time.sleep(2)
        driver.back()
        time.sleep(2)

        refNews = driver.find_element_by_xpath("//*[@id=\"app\"]/div/form/form/div[1]/a/a")
        refNews.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, (self.networkAdr + "/news"))
        time.sleep(2)
        driver.back()
        time.sleep(2)

    #вход пользователя на сайт
    def signIn(self, username, password):
        driver = self.driver

        driver.find_element_by_xpath("//*[@id=\"username\"]").send_keys(username)
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password)
        time.sleep(1)
        signInButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div/form/form/div[2]/div/button")
        signInButton.click()
        time.sleep(2)

    #тестирование успешного входа на сайт
    def testSignIn(self):
        driver = self.driver
        self.signIn("user1", "123456")
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/h2").text, "Вы зашли как user1")

    #тестирование неправильного входа на сайт
    def testSignInError(self):
        driver = self.driver
        self.signIn("user59576", "password")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Неправильно введен логин или пароль")

