from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    # driver.get 打开一个指定网页
    driver.get("file:///C:/Users/YSL/PycharmProjects/ui-auto-test/html/demo1.html")
    pass