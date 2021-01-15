from selenium import webdriver
import unittest
import time


#тестирование страницы новостей
class TestNews(unittest.TestCase):
    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr + "/news")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #переход на страницу новости
    def testProducts(self):
        driver = self.driver
        product = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/a/a/div/p")
        product.click()
        time.sleep(2)
        productName = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p").text
        self.assertEqual(productName, "Выставка Roma Aeterna в Инженером корпусе")
        driver.back()
        time.sleep(2)

        product = driver.find_element_by_xpath("//*[@id =\"app\"]/div[1]/main/section/div/div[1]/a/a/div")
        product.click()
        time.sleep(2)
        productName = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p").text
        self.assertEqual(productName, "Вышел трейлер фильма о Ван Гоге, стилизованный под его картины")
        driver.back()
        time.sleep(2)
        productsNames = ["Рисунки Сергея Чобана – финалисты конкурса KRob", "Выставка «Золотой век архитектурной графики».", "Золотое равновесие"]
        for i in range(1, 4):
            product = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/div[2]/a[{}]/a/div".format(i))
            product.click()
            time.sleep(2)
            productName = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p").text
            self.assertEqual(productName, productsNames[i - 1])
            driver.back()
            time.sleep(2)
