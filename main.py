import json
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from sender import QQSender
import logging

env_dist = os.environ
config = env_dist.get("config")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
token = env_dist.get("config")
url = r'https://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'
driver_path = ChromeDriverManager().install()
chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service(driver_path)


def run(username: str, password: str):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    username_element = driver.find_element(By.ID, 'username')
    username_element.send_keys(username)
    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys(password)
    driver.find_element(By.NAME, 'submit').click()
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, '我知道了').click()
    except Exception as e:
        logger.error(e)
    js = 'go_sub();document.querySelector("label.weui-cell.weui-cell_active.weui-check__label").click();save()'
    driver.execute_script(js)
    driver.close()
    logger.info(f'{username} 已完成填报')


def yqtb(students: list):
    logger.info('开始执行填报...')
    for username, password in students:
        run(username, password)
    logger.info('填报执行完毕')


if __name__ == '__main__':
    if token:
        to_qq = "2781372804"
        sender = QQSender(token)
    try:
        students = json.loads(config)
        logger.info(f'加载的用户列表: {[username for username, _ in students]}')
        yqtb(students)
    except Exception as e:
        if token:
            sender.send_private_message(to_qq, e)
        else:
            logger.error(e)

    if token:
        sender.send_private_message(to_qq, '今日填报成功')
