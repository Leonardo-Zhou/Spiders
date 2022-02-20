# -*- coding: utf-8 -*-
"""
@File    : 创建机场账号.py
@Time    : 2021/11/18 14:45
@Author  : Leonardo Zhou
@Email   : 2974519865@qq.com
@Software: PyCharm
"""
import time
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import requests
import cv2
import numpy as np
import re
from selenium.webdriver import ActionChains
from lxml import etree
import pyperclip
from USER_AGENT import UA_list


class newAccount:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['Airport']['Jssr Account']
        self.url_login = 'https://www.jssrvpn.xyz/auth/login'
        self.url_register = 'https://www.jssrvpn.xyz/auth/register'
        self.url_checkin = 'https://www.jssrvpn.xyz/user/checkin'
        self.url_user = 'https://www.jssrvpn.xyz/user'
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('w3c', False)
        caps = {
            'browserName': 'chrome',
            'loggingPrefs': {
                'browser': 'ALL',
                'driver': 'ALL',
                'performance': 'ALL',
            },
            'goog:chromeOptions': {
                'perfLoggingPrefs': {
                    'enableNetwork': True,
                },
                'w3c': False,
            },
        }
        self.browser = webdriver.Chrome(
            desired_capabilities=caps,
            chrome_options=chrome_options)
        self.browser.get(self.url_register)
        self.headers = {
            'User-Agent': random.choice(UA_list)}
        self.start_x = 50

    def generate_email(self):
        '''
        
        :return: email,password
        '''
        flag = True
        while flag:
            length = random.randint(8, 15)
            name_and_mail = ''.join([chr(random.choice(
                [random.randint(65, 90), random.randint(97, 122)])) for i in range(length)])
            find_query = {'email': name_and_mail}
            password = '12345678'
            if not list(self.db.find(find_query)):
                flag = False
                self.db.insert_one(
                    {'email': name_and_mail, 'password': password})
                
        print('计算的email是:{},密码为{}'.format(name_and_mail, password))
        return name_and_mail, password

    def capture_pic(self):
        '''
        获得验证的图片
        :return: 切割后的图片对象
        '''
        try:
            # 寻找验证开始的按钮
            verify_button = WebDriverWait(
                self.browser, 5, 0.5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "geetest_radar_tip")))
            verify_button.click()

            verification_picture = WebDriverWait(
                self.browser,
                5,
                0.5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "body > div.geetest_fullpage_click.geetest_float.geetest_wind.geetest_slide3 > div.geetest_fullpage_click_wrap > div.geetest_fullpage_click_box > div > div.geetest_wrap > div.geetest_widget > div > a > div.geetest_canvas_img.geetest_absolute > div > canvas.geetest_canvas_bg.geetest_absolute")))
            time.sleep(1)
            verification_picture.screenshot('verification.png')
            background_image_crouped = crop_image(self.start_x, 'verification.png')
            print('背景图片加载完成')
            return background_image_crouped

        except BaseException as e:
            print(e)
            self.browser.quit()

    def get_target_img_url(self):
        data = self.browser.get_log('performance')
        compiled = re.compile(
            r'.*(https://static.geetest.com/pictures/gt/.*\.png)')
        for line in data:
            temp = compiled.match(str(line))
            if temp:
                print('滑块图片url已获得')
                return temp.group(1)

    def download_target_pic(self):
        '''
        
        :return: 滑块的img对象
        '''
        url = self.get_target_img_url()
        response = requests.get(url, headers=self.headers)
        content = response.content
        image = cv2.imdecode(np.asarray(bytearray(response.content), dtype='uint8'), cv2.IMREAD_COLOR)
        print('滑块图片加载成功')
        return image

    def fill_form(self, email, password):
        name_box = self.browser.find_element_by_id('name')
        name_box.send_keys(email)

        email_box = self.browser.find_element_by_id('email')
        email_box.send_keys(email)

        password_box = self.browser.find_element_by_id('passwd')
        re_password_box = self.browser.find_element_by_id('repasswd')
        password_box.send_keys(password)
        re_password_box.send_keys(password)
        print('信息完成填写')
        
    def slider(self):
        '''
        用于完成验证
        :return: None
        '''
        background_image = self.capture_pic()
        target_image = self.download_target_pic()
        x = identify_gap(background_image, target_image)+self.start_x
        slider = WebDriverWait(
                self.browser, 5, 0.5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'geetest_slider_button')))

        action = ActionChains(self.browser)  # 实例化一个action对象
        action.click_and_hold(slider).perform()  # perform()用来执行ActionChains中存储的行为
        print(x)
        # print(get_track(x))
        # for i in range(int(x/5)):
        #     action.move_by_offset(5,0).perform()
        #     action.reset_actions()
        for i in get_track(x):
            action.move_by_offset(i,0).perform()
            action.reset_actions()
        time.sleep(0.5)
        action.release().perform()
        time.sleep(0.5)
        
    def click_confirm_button(self):
        confirm_button = WebDriverWait(
                self.browser, 2, 0.5).until(
                EC.presence_of_element_located(
                    (By.ID,'register-confirm')))
        confirm_button.click()
        time.sleep(1)
        OK_button = self.browser.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]')
        time.sleep(0.1)
        OK_button.click()
        
    def sign_in(self,email,password):
        print('正在下载界面')
        email = email + '@gmail.com'
        # sign_in_button = WebDriverWait(
        #         self.browser, 5, 0.5).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH,'//*[@id="checkin-div"]/a')))
        # print('界面载入成功')
        # sign_in_button.click()
        # OK_button = WebDriverWait(
        #         self.browser, 5, 0.5).until(
        #         EC.presence_of_element_located(
        #             (By.XPATH,'/html/body/div[4]/div/div[3]/button[1]')))
        # OK_button.click()
        # copy_subscribe = self.browser.find_element_by_xpath('//div[@class="buttons"]/a[7]')
        # text = copy_subscribe.get_attribute('data-clipboard-text')
        # print(text)
        data = {
            'email': email,
            'passwd': password,
            'code': None
        }
        # 构造session请求体
        session = requests.session()
        # post请求，登录
        r1 = session.post(self.url_login,data)
        session.get(self.url_user)
        # 每日签到
        r2 = session.post(self.url_checkin)
        response = session.get(self.url_user)
        content = response.content.decode('utf-8')
        # 使用xpath语法
        selector = etree.HTML(content)
        subscribe_url = selector.xpath('//div[@class="buttons"]/a[7]/@data-clipboard-text')[0]
        print(subscribe_url)
        pyperclip.copy(subscribe_url)
        print('订阅链接已经复制')
        time.sleep(1)
        print('程序退出')
        
    def run(self):
        email,password = self.generate_email()
        flag = 1
        while flag != 0 and flag < 4:
            self.fill_form(email,password)
            self.slider()
            try:
                self.click_confirm_button()
                print('第{}次尝试'.format(flag))
                print('成功注册')
                flag = 0
            except Exception as e:
                print('第{}次尝试失败'.format(flag))
                flag += 1
                print(e)
        self.browser.quit()
        self.sign_in(email,password)


def crop_image(x_start, filename):
    '''
    
    :param x_start: 开始截取的x值
    :param filename: 文件的名称
    :return: cv2.image对象
    '''
    img_temp = cv2.imread(filename)
    img = img_temp[0:, x_start:]
    return img


def identify_gap(bg, tp):
    '''
    
    :param bg: 背景的图片对象
    :param tp: 滑块的对象
    :return: x坐标
    '''
    # 识别图片边缘
    
    bg_edge = cv2.Canny(bg, 100, 200)
    
    tp_edge = cv2.Canny(tp, 100, 200)
    
    # 转换图片格式
    
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    
    # 缺口匹配
    
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    
    # 绘制方框
    
    th, tw = tp_pic.shape[:2]
    
    tl = max_loc  # 左上角点的坐标
    
    # 返回缺口的X坐标
    return tl[0]


def get_track(distance):      # distance为传入的总距离
    # 移动轨迹
    track=[]
    # 当前位移
    current=0
    # 减速阈值
    mid=distance*4/5
    # 计算间隔
    t=0.2
    # 初速度
    v=1

    while current<distance:
        if current<mid:
            # 加速度为2
            a=4
        else:
            # 加速度为-2
            a=-3
        v0=v
        # 当前速度
        v=v0+a*t
        # 移动距离
        move=v0*t+1/2*a*t*t
        # 当前位移
        current+=move
        # 加入轨迹
        track.append(round(move))
    track[-2] -= 2
    track[-1] -= 2
    track.append(2)
    track.append(1)
    track.append(1)
    track.append(0)
    return track


account = newAccount()
account.run()