from bs4 import BeautifulSoup as bs
import time
import re

def preprocessing(text):
  text = re.sub('[\?:]', '', text)
  text = re.sub('[ -]', '_', text)
  return text

def get_recent_node_data(driver, results):
  print('최근 노드 정보 가져오기')
  time.sleep(5)
  html = driver.page_source
  soup = bs(html, 'html.parser')
  # 가장 최근 노드
  soup_recent_node = soup.select('div.section__body')[1]

  # 이름과 설명
  results['node_name'] = preprocessing(soup_recent_node.select_one('div.card__name').text)
  results['node_blurb'] = soup_recent_node.select_one('div.card__blurb').text

  results['node_category'] = soup.select('div.card__category')[3].text

def get_step_name_and_content(driver, results):
  print('스탭 정보 가져오기')
  results['steps'] = {}
  # 전체 스탭 링크를 돌 것
  for i in range(len(results['step_links'])):
    results['step_links'][i].click()
    time.sleep(1)

    # 스탭 제목 수집
    step_title = preprocessing(results['step_links'][i].text.split('\n')[0])
    
    html = driver.page_source
    soup = bs(html, 'html.parser')

    # 스탭의 내용 수집
    results['steps'][step_title] = soup.select_one('div.aiffel-content__body')
    # 바디가 없으면 평가표를 수집
    if results['steps'][step_title] == None:
      results['steps'][step_title] = soup.find('table')
    
    print('스텝 이름', step_title, i + 1, len(results['step_links']))
