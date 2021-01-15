from selenium import webdriver
import unittest
import time
import re


# тестирование карусели главной страницы
class TestCarusel(unittest.TestCase):

    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # получение активной картинки
    def getStatusPictures(self, pictures):
        statusPictures = []
        for picture in pictures:
            statusPictures.append(
                True if re.search(r'carousel-item active', picture.get_attribute("outerHTML")) else False)
        return statusPictures

    # тестирование кнопок карусели переключения слайдов
    def testCarouselMoving(self):
        driver = self.driver
        pictures = []
        for i in range(1, 4):
            pictures.append(driver.find_element_by_id("slide" + str(i)))
        # кнопка вперед
        carouselNextButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/a[2]")
        carouselNextButton.click()
        time.sleep(1)
        indexNextPage = self.getStatusPictures(pictures).index(False)
        nextPage = driver.find_element_by_xpath("slide" + str(indexNextPage + 1))
        self.assertEqual(pictures[indexNextPage], nextPage)
        # #кнопка назад
        carouselNextButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/div/div[1]/a[1]")
        carouselNextButton.click()
        time.sleep(1)
        indPrev = self.getStatusPictures(pictures).index(False)
        prevPage = driver.find_element_by_xpath("slide" + str(indPrev + 1))
        self.assertEqual(pictures[indPrev], prevPage)

