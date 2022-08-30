import time
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
#     try:
#         driver.find_element(
#             By.CSS_SELECTOR, 'button.sw-button.btn.sw-button--primary.sw-button--big.is-round').click()
#         driver.find_element(By.PARTIAL_LINK_TEXT, '我知道了').click()
#     except Exception as e:
#         pass
    js = 'go_sub();go_subfx();document.querySelector("label.weui-cell.weui-cell_active.weui-check__label").click();save();savefx()'
    driver.execute_script(js)
    fail = None
#     try:
#         time.sleep(3)
#         fail_info = driver.find_element(By.PARTIAL_LINK_TEXT, '确定')
#     except Exception as e:
#         pass
    driver.close()
    if fail:
        return False
    else:
        return True


def yqtb(students: list):

    logger.info('开始执行填报...')
    all_num = len(students)
    cur_num = 0
    suc_num = 0
    for username, password in students:
        cur_num += 1
        if run(username, password):
            suc_num += 1
            logger.info(
                f'{username} 填报失败; ({all_num}个任务中的第{cur_num}个,共成功{suc_num}个)')
        else:
            logger.info(
                f'{username} 填报成功; ({all_num}个任务中的第{cur_num}个,共成功{suc_num}个)')
    logger.info('填报执行完毕')
    if suc_num < all_num:
        raise Exception("填报过程出现异常")


def pushplus(msg: str):
    pushplus_url = 'http://www.pushplus.plus/send'
    data = {
        'token': pushplus_token,
        'content': msg,
        'template': 'json'
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    requests.post(pushplus_url, data=body, headers=headers)


if __name__ == '__main__':
    try:
        students = json.loads(str(config))
        logger.info(f'加载的用户列表: {[username for username, _ in students]}')
        yqtb(students)
    except Exception as e:
        if pushplus_token:
            logger.info('发送错误消息')
            pushplus(str(e))
            raise e
        else:
            logger.error(e)
            raise e
