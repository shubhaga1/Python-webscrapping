from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://indiacovidresources.in/full")

#res = driver.find_elements_by_xpath("//*[@id='screenScrollView0']")
res = driver.find_elements_by_xpath('//*[@id="all-cities"]')
print(len(res))
