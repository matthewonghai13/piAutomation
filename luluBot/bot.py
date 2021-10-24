import time
from sys import platform
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

def main():
    options = Options()
    # Prevent Chrome crashing on launch
    options.add_argument("--no-sandbox");
    options.add_argument("--disable-dev-shm-usage");
    # Pretend to run as headed browser, then run in headless
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
    options.add_argument('user-agent={0}'.format(user_agent))
    options.add_argument("--headless")

    if platform == "linux":
        driver = webdriver.Chrome(options=options)
    else:
        import chromedriver_binary  # Adds chromedriver binary to path
        driver = webdriver.Chrome(options=options)
    
    driver.get("https://shop.lululemon.com/p/men-shorts/Pace-Breaker-Short-5-Lined/_/prod10080318?color=0001&sz=XS")
    sleep(10)
    # driver.save_screenshot("out.png")
    if len(driver.find_elements_by_id("purchase-attributes-size-notification-error")) > 0:
        print("Nothing Found.")
    else:
        print("In stock!")
    driver.close()

if __name__ == '__main__':
    main()