from selenium import webdriver
import unittest
import random
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#тестирование регистрации пользователя
class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr + "/register")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #регистрация пользователя
    def registration(self, username, password, password2):
        driver = self.driver

        driver.find_element_by_xpath("//*[@id=\"inputUsername\"]").send_keys(username)
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"repeatPassword\"]").send_keys(password2)
        time.sleep(1)
        regButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/form/form/div[2]/div/button")
        regButton.click()
        time.sleep(2)

    #переход по ссылкам из регистрации
    def testRegistrationRefs(self):
        driver = self.driver

        refSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/form/form/div[2]/p/a/a")
        refSignIn.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, (self.networkAdr + "/Login"))
        time.sleep(2)
        driver.back()
        time.sleep(2)

        refNews = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/form/form/div[1]/a/a")
        refNews.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, (self.networkAdr + "/news"))
        time.sleep(2)
        driver.back()
        time.sleep(2)


    #тест успешной регистрации пользователя
    def testRegistration(self):
        driver = self.driver
        self.registration("userNew2563", "1234567", "1234567")
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/h2").text, "Вы зашли как userNew2563")

    #тест неправильной регистрации пользователя
    def testRegistrationError(self):
        driver = self.driver
        self.registration("userNew", "password1", "password")

        #проверка появления диалогового окна с предупреждением
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Пароли не совпадают")
