import time
import random
from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumOpenUrl():
    def __init__(self) -> None:
        self.useragentpath = "./user-agents.txt"
        self.USER_AGENTS = self.load_useragents()  # 加载UserAgents 1000个

    def load_useragents(self):
        """加载useragents头1000个,并随机取一个用."""
        USER_AGENT = []
        with open(self.useragentpath) as files:
            for item in files.readlines():
                USER_AGENT.append(item.strip())
        print("USER_AGENT_NUM:", len(USER_AGENT))
        return USER_AGENT

    def refreshSeleniumConfigure(self):
        """配置chrome浏览器配置文件,模拟不同的人访问网页."""
        # 基本配置
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # 配置无头访问
        # chrome_options.add_argument('--disable-gpu')  # Google推荐 防bug
        # chrome_options.add_argument('--window-size=1920,1080')  # 配置访问的分辨率
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--no-gpu')
        # chrome_options.add_argument('--disable-setuid-sandbox')
        # chrome_options.add_argument('--single-process')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--user-agent=%s' % random.choice(self.USER_AGENTS))
        # ip代理
        # ip = "127.0.0.1:7890"
        # ip = "192.168.31.242:7890"
        # chrome_options.add_argument(f"--proxy-server={ip}")
        return chrome_options

    def visitUrl(self, url):
        chrome_options = self.refreshSeleniumConfigure()
        # 查看本机ip，查看代理是否起作用
        # browser.get("http://httpbin.org/ip")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        # 访问网页
        browser.get(url)
        browser.save_screenshot("1.png")
        time.sleep(15)
        # 2倍速播放
        # a = browser.find_element(By.XPATH, '//*[@id="bilibili-player"]/div/div/div[1]/div[1]/div[12]/div[2]/div[2]/div[3]/div[2]/ul/li[1]')
        # a.click()
        # 截图，退出
        browser.save_screenshot("click1.png")
        browser.close()  # 关闭当前页面
        browser.quit()  # 关闭浏览器


if __name__ == "__main__":
    sou = SeleniumOpenUrl()
    # 播放100次
    for i in range(100):
        print(f"第{i}次播放.")
        # sou.visitUrl("https://www.bilibili.com/video/BV13W4y1a7k2")
        sou.visitUrl("http://httpbin.org/ip")
