import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from captcha_solver import CaptchaSolver
import time
import os
import pytesseract
from PIL import Image
import io
import urllib.request
import cv2

with urllib.request.urlopen("http://www.python.org") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s)

class AccessData:

    def __init__(self, fund_name):



        self.fund_name = fund_name
        self.fund_name = 'BTG PACTUAL ABSOLUTO GLOBAL EQUITIES BRL INSTITUCIONAL FI DE ACOES INVESTIMENTO NO EXTERIOR'
        self.CVM_site = 'https://cvmweb.cvm.gov.br/SWB//Sistemas/SCW/CPublica/CConsolFdo/FormBuscaParticFdo.aspx'


        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("prefs", {
            "download.default_directory": r"/Users/JardielJunior/Desktop/CVM/",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome('/Users/JardielJunior/Desktop/ChromeDriver/chromedriver', chrome_options=self.options)




        self.driver.get(self.CVM_site)
        self.id_fund_name = "txtCNPJNome"
        self.input_field = self.driver.find_element_by_id(self.id_fund_name)
        self.input_field.send_keys(self.fund_name)
        self.deleteCaptcha()
        self.getCaptcha()
        self.solveCaptcha()

    def deleteCaptcha(self):
        try:
            os.remove("/Users/JardielJunior/Downloads/captcha.jpeg")
        except:
            print('There is no Captcha saved.')

    def getCaptcha(self):

        self.captcha_Xpath ='//*[@id="trRandom3"]/td[2]/img'
        img = self.driver.find_element_by_xpath('//img')
        actionChain = ActionChains(self.driver)
        actionChain.context_click(img).perform()
        pyautogui.typewrite(['down','down', 'enter'])
        time.sleep(1)
        pyautogui.typewrite('captcha', interval=0.5)
        pyautogui.press('enter')




    import os
    from python3_anticaptcha import NoCaptchaTaskProxyless
    from selenium import webdriver


    def solveCaptcha(self):
        from PIL import Image

        from pdf2image import convert_from_path
        # img = Image.open('captcha.jpg')
        image = cv2.imread("/Users/JardielJunior/Downloads/captcha.jpeg")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # gray = cv2.medianBlur(gray, 3)

        filename = "{}.png".format("temp")
        cv2.imwrite(filename, gray)
        text = pytesseract.image_to_string(Image.open('temp.png'),
                                    config="-c tessedit_char_black=0123456789")

