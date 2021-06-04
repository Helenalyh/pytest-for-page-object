from pytest import mark
import os.path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test.page_objects.trial_page import WikiPage
from test.page_objects.trial_page import AmazonPage
from test.page_objects.trial_page import IMDbPage
from test.page_objects.training_ground_page import TrainingGooglePage


@mark.wiki
def test__wiki__page(chrome_driver):
    wiki_page = WikiPage(driver=chrome_driver)
    wiki_page.go()
    wiki_page.talkButton.click()
    assert wiki_page.talkButton.text=='Talk', "Unexpected talk button text"

@mark.image
def test_image_page(chrome_driver):
    img_page = TrainingGooglePage(driver=chrome_driver)
    img_page.go()
    img_page.searchBar.input_text('broccoli')
    img_page.searchBar.input_text(Keys.ENTER)
    infos=[]
    for i in range (1,2):
        img=img_page.findImage(i)
        img.download('/Users/yihongli/Desktop/selePics/','broccoli',i)
        infos.append(img.getInfo())
    assert os.path.isfile('/Users/yihongli/Desktop/selePics/broccoli1.png')
    assert any("Broccoli" in s for s in infos), "No Brocolli in info list"

@mark.amazon 
def test_amazon_page(chrome_driver):
    amazon_page= AmazonPage(driver=chrome_driver)
    amazon_page.go()
    amazon_page.emailInput.input_text('yihongli@andrew.cmu.edu')
    assert amazon_page.contiButton.text=="Continue", "Unexpected continue button text"
    amazon_page.contiButton.click()
    amazon_page.pwdInput.input_text('xxxxxxxx')
    amazon_page.signInButton.click()

@mark.imdb
def test_imdb_page(chrome_driver):
    imdb_page=IMDbPage(driver=chrome_driver)
    imdb_page.go()
    castList=imdb_page.cast.getCastList()
    assert "Robin Williams ... John Keating" in castList, "Wrong cast list"
