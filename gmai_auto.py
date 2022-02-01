# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.keys import Keys
# import time, os
# import webbrowser as web
# import pyautogui as pg

# # print('Enter the gmailid and password')
# # gmailId, passWord = map(str, input().split())
# try:
#     driver = webdriver.Firefox(executable_path='/home/ekudgan/Downloads/Surveillance/geckodriver')
#     driver.get(r'https://accounts.google.com/signin')
#     driver.implicitly_wait(15)
#     time.sleep(2)
    
#     loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
#     loginBox.send_keys('barcdrhr')
  
#     nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
#     nextButton[0].click()
#     time.sleep(2)
    
#     passWordBox = driver.find_element_by_xpath(
#         '//*[@id ="password"]/div[1]/div / div[1]/input')
#     passWordBox.send_keys('vvagashe')
  
#     nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
#     nextButton[0].click()
  
#     print('Login Successful...!!')
# except:
#     print('Login Failed')

# # driver.Manage().Timeouts().ImplicitlyWait(TimeSpan.FromSeconds(15))

# # driver.SwitchTo().Frame("canvas_frame")

# composeBtn = driver.FindElement(By.CssSelector("div[class='T-I J-J5-Ji T-I-KE L3']"))
# composeBtn.Click()

# toBox = driver.FindElement(By.CssSelector("textarea[class='dK nr']"))
# toBox.SendKeys("chaitanya2692@gmail.com")

# subjBox = driver.FindElement(By.CssSelector("input[class='ez nr']"))
# subjBox.SendKeys("This is a test")

# msgBox = driver.FindElement(By.CssSelector("textarea[class='Ak aXjCH']"))
# msgBox.SendKeys("This is a test email sent via Selenium Web Driver")

# sendBtn = driver.FindElement(By.CssSelector("div[class='T-I J-J5-Ji Bq nS T-I-KE L3']>b"))
# sendBtn.Click()


import unittest
from selenium import webdriver

class TestGmail(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox(executable_path='/home/ekudgan/Downloads/Surveillance/geckodriver')

	def testLogin(self):
		driver = self.driver
		driver.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3A44f1212c73eb5236%2C10%3A1628170427%2C16%3A18f17c820b3fd3c4%2C347aad6e349ce72fe5473536f8e13c8bea0acb6deb029a477e329e643617f352%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%222f01006dc03748d49285ad288f2fa69b%22%7D&response_type=code&flowName=GeneralOAuthFlow')
		self.assertIn('Gmail', driver.title)
		loginBox = driver.find_element_by_id('identifierId')
		loginBox.send_keys('email.address@gmail.com')
		pwBox = driver.find_element_by_id('Passwd')
		pwBox.send_keys('!SuperSecretpassw0rd')
		signinBtn = driver.find_element_by_id('signIn')
		signinBtn.click()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)