import json
import os
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import logging

env_dist = os.environ
config = env_dist.get("config")
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

url = r'https://yqtb.nwpu.edu.cn/wx/ry/jrsb.jsp'
driver_path = ChromeDriverManager().install()
chrome_options = Options()
chrome_options.add_argument('--headless')
service = Service(driver_path)
pushplus_token = env_dist.get("pushplus")


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
    fail_info = None
    try:
        fail_info = driver.find_element(By.PARTIAL_LINK_TEXT, '确定')
    except Exception as e:
        pass
    if fail_info:
        logger.info(f'{username} 填报失败, 可能是因为不在允许时间内')
    else:
        logger.info(f'{username} 已完成填报')
    driver.close()


def yqtb(students: list):
    logger.info('开始执行填报...')
    for username, password in students:
        run(username, password)
    logger.info('填报执行完毕')


def pushplus(token):
    pushplus_url = 'http://www.pushplus.plus/send'
    data = {
        'token': token,
        'content': '今日已经填报',
        'template': 'json'
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(pushplus_url, data=body, headers=headers)


if __name__ == '__main__':
    students = json.loads(config)
    logger.info(f'加载的用户列表: {[username for username, _ in students]}')
    yqtb(students)
    if not pushplus_token:
        logger.info("不存在 PUSHPLUS ，请重新检查")
    else:
        pushplus(pushplus_token)
