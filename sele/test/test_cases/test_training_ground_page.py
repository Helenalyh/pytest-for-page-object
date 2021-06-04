from pytest import mark
from test.page_objects.training_ground_page import TrainingGooglePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@mark.training
def test_training_page(chrome_driver):
    trng_page = TrainingGooglePage(driver=chrome_driver)
    trng_page.go()
    trng_page.searchBar.input_text('cauliflower')
    trng_page.searchBar.input_text(Keys.ENTER)
    

    trng_page.go()
    trng_page.searchBar.input_text('Interstellar')
    trng_page.searchBar.input_text(Keys.ENTER)
    trng_page.goto('wikipedia').click()

