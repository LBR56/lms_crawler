import chromedriver_autoinstaller
from selenium import webdriver
import platform
import os

# 드라이브를 체크하고 없을시 설치
def check_driver():
  # 운영체제 종류 확인
  os_type = platform.system()

  # 크롬 버전 확인
  # 여기서 오류가 발생하면 크롬을 설치
  chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

  driver_path = os.path.abspath(os.path.join(__file__, '..', 'driver', chrome_ver))

  # 파일이 있는지 확인하고 접근
  if os.path.exists(driver_path):
    print(f"chrome driver is insatlled: {driver_path}")
  else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    os.mkdir('driver')
    print(chromedriver_autoinstaller.install(path = os.path.dirname(driver_path)))

# windows만 exe 파일을 사용함
  if os_type == 'Windows':
    driver_path += '/chromedriver.exe'
  else:
    driver_path += '/chromedriver'

  return driver_path

# 브라우저 연결
def get_driver(driver_path):
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	return webdriver.Chrome(driver_path, options=options)

DRIVER = get_driver(check_driver())
