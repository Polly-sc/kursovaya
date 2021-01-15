from selenium import webdriver
import unittest
import time


#тестирование добавления новости в избранную со страницы новости по нажатию кнопки "Добавить в избранное"
class TestNewsFavorites(unittest.TestCase):

    def setUp(self):
        self.networkAdr = "http://localhost:8080"
        chromePath = "/Users/polinasetinina/Desktop/TestWebProg/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get(self.networkAdr + "/news")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def favoritePost(self, urlPost):
        driver = self.driver
        driver.get("http://localhost:8080/news" + "/" + urlPost)

        postName = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/p").text
        favoriteButton = driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/a/div/footer/span/button")
        favoriteButton.click()
        time.sleep(2)


        buttonRefFav = driver.find_element_by_xpath("//*[@id=\"navbarNav\"]/ul/li[4]/a/a")
        buttonRefFav.click()
        time.sleep(2)

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
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/div[1]/main/section/div/div/h5").text,
                         postName)
        # favoriteList = self.driver.execute_script("return localStorage.getItem('Favorites')")
        # self.assertTrue(postName in favoriteList)

    def testFavoritePost(self):
        self.favoritePost("vystavka-roma-aetena-v-inzhenernom-corpuse")
