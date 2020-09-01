# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ブラウザ指定
browser = webdriver.Firefox()

# ウィンドウの最大化
browser.maximize_window()

# 表示するURLを指定
browser.get('http://www.google.com')

# 検索ボックスの要素を取得
element = browser.find_element_by_name("q")

# キーワード入力
element.send_keys("犬")

# 検索ボタンの要素を取得
submit = browser.find_element_by_name("btnK")

# 検索実行
submit.click()

# ページが表示されるまで10秒待つ
WebDriverWait(browser, 10).until(
  EC.title_contains("犬")
)

# スクリーンショット
browser.save_screenshot("screen.png")

# webページを閉じる
browser.quit()
