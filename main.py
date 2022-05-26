# 사이트에 들어갈 수 있도록 세팅
from settings import DRIVER
import cralwer
import config
import driver
import save

def main():
  # 정보 저장 dict
  results = {}
  # 사이트 실행
  driver.enter_site(DRIVER, config.SITE_URL)
  # 로그인 실행
  driver.log_in(DRIVER, id = config.USER_INFO['id'], pw = config.USER_INFO['pw'])
  # 최근 노드의 이름과 설명 수집
  cralwer.get_recent_node_data(DRIVER, results)
  # 가장 최근 노드 클릭
  driver.click_recent_node(DRIVER)
  # 스탭 링크 수집하기
  driver.collect_step_links(DRIVER, results)
  # 스탭 이름과 컨탠츠 수집하기
  cralwer.get_step_name_and_content(DRIVER, results)
  
  # 스탭 링크 삭제
  del results['step_links']
  # 크롤링 내용 정리 폴더 생성
  save.createFolder(results)
  # 목차 만들기
  save.add_readme(results)
  # 각 내용 만들기
  save.add_step_content(results)

  DRIVER.quit()

if __name__ == '__main__':
  main()