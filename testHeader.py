from selenium import webdriver
import unittest
import random
import time
import re


# Тестирование универсальной шапки для страниц
class TestHeader(unittest.TestCase):

    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr)
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # Загрузка разделов приложения
    def testWorkingChoosingSection(self):
        driver = self.driver

        sectionNamesArray = ["", "", "News", "Favorites"]
        for index in range(1, 5):
            if index == 1 or index == 2 or index == 5:
               continue
            loadSectionButton = driver.find_element_by_xpath("//*[@id=\"navbarNav\"]/ul[1]/li[{}]".format(index))
            loadSectionButton.click()
            time.sleep(2)
            title_name = driver.current_url
            self.assertEqual(title_name,(self.networkAdr + "/" + sectionNamesArray[index-1]))



