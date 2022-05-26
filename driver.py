from selenium.webdriver.common.by import By

def enter_site(driver, url):
  driver.get(url)
  driver.implicitly_wait(10)

def log_in(driver, id, pw):
  print('로그인 시도')
  # 로그인 시도
  try:
    driver.find_element(By.CSS_SELECTOR, 'input').send_keys(id)
    driver.find_element(By.CSS_SELECTOR, 'input[type=password]').send_keys(pw)
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    driver.implicitly_wait(10)
  except:
    # 로그인 실패는 로그인 중임
    print('로그인 중')
  print('로그인 완료')

def click_recent_node(driver):
  print('최근 노드로 이동')
  driver.find_elements(By.CSS_SELECTOR, 'div.section__body')[1].click()
  driver.implicitly_wait(10)
  print('첫 목차로 이동')
  driver.find_element(By.CSS_SELECTOR, 'div.step-wrap').click()
  driver.implicitly_wait(10)

def collect_step_links(driver, results):
  print('스탭 링크 수집')
  results['step_links'] = driver.find_elements(By.CSS_SELECTOR, 'div.stepMain__sidebar a')