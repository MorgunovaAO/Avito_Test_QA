import time
from datetime import datetime
from time import sleep

from playwright.sync_api import Page, Route, expect
import re

def test1(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test1.json"))
    # Подмена значений счетчиков на "1000"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test1_' + now_day + '.png')

def test2(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test2.json"))
    # Подмена значений счетчиков на "1001"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test2_' + now_day + '.png')

def test3(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test3.json"))
    # Подмена значений счетчиков на "999"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test3_' + now_day + '.png')

def test4(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test4.json"))
    # Подмена значений счетчиков на "1000000"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test4_' + now_day + '.png')

def test5(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test5.json"))
    # Подмена значений счетчиков на "1000001"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test5_' + now_day + '.png')

def test6(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test6.json"))
    # Подмена значений счетчиков на "999999"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test6_' + now_day + '.png')

def test7(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test7.json"))
    # Подмена значений счетчиков на "1000000000"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test7_' + now_day + '.png')

def test8(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test8.json"))
    # Подмена значений счетчиков на "1000000001"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test8_' + now_day + '.png')

def test9(page: Page):

    page.route("**/web/1/charity/ecoImpact/init", lambda route: route.fulfill(path="responses/data_test9.json"))
    # Подмена значений счетчиков на "999999999"
    page.goto('https://www.avito.ru/avito-care/eco-impact')
    page.locator(selector='.desktop-impact-items-F7T6E').click()
    now_day = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    page.screenshot(type='png', path='output/screen_test9_' + now_day + '.png')