from selenium import webdriver

url = "https://www.espn.com/soccer/schedule"

browser = webdriver.chrome()
browser.get(url)
browser.find_element_by_xpath('https://www.espn.com/soccer/team/_/id/380/wolverhampton-wanderers').click()