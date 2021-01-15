from selenium import webdriver
import unittest
import time
#тестирование карусели главной страницы
class TestProfile(unittest.TestCase):

    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr + "/favorites")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #проверка перехода на страницы входа и регистрации по кнопкам, если пользователь еще не зашел в свой профиль
    def testProfilePage(self):
        driver = self.driver

        buttonSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p[2]/button[1]")
        buttonSignIn.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, (self.networkAdr + "/login"))
        time.sleep(2)
        driver.back()
        time.sleep(2)

        buttonRegistration = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p[2]/button[2]")
        buttonRegistration.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, (self.networkAdr + "/register"))
        time.sleep(2)
        driver.back()

    #переход в избранное выход из профиля пользователя по кнопке "Выход"
    def testExit(self):
        driver = self.driver
        buttonSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p[2]/button[1]")
        buttonSignIn.click()
        time.sleep(1)

        driver.find_element_by_xpath("//*[@id=\"username\"]").send_keys("user1")
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("123456")
        time.sleep(1)
        signInButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div/form/form/div[2]/div/button")
        signInButton.click()
        time.sleep(2)

        FavoritesButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p/button[2]")
        FavoritesButton.click()
        time.sleep(2)
        driver.back()
        time.sleep(2)

        buttonExit = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p/button[1]")
        buttonExit.click()
        time.sleep(2)
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/h2").text, "Необходимо авторизоваться для получения доступа к избранному.")

