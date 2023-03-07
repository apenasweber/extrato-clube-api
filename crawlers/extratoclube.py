from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ExtratoClube:
  def __init__(self, cpf, usuario, senha):
    self.cpf = cpf
    self.usuario = usuario
    self.senha = senha
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    )
    options.add_argument("--remote-debugging-port=9222")
    self.driver = webdriver.Chrome(options=options)

  def login(self):
    self.driver.get(
        "http://ionic-application.s3-website-sa-east-1.amazonaws.com/login"
    )
    username_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user"]'))
    )
    password_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
    )
    username_input.send_keys(self.usuario)
    password_input.send_keys(self.senha)
    password_input.send_keys(Keys.ENTER)

  def close_modal(self):
    time.sleep(2)
    WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    ).send_keys(Keys.ESCAPE)

  def access_reports(self):
    extrato_button_click = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/app-root/app-home/ion-app/ion-menu/ion-content/ion-list/ion-item[2]",
            )
        )
    )
    extrato_button_click.click()

  def search_benefits_by_cpf(self):
    benefits_button_click = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card/ion-grid/ion-row[2]/ion-col/ion-card/ion-button[11]',
            )
        )
    )

    self.driver.execute_script(
        "arguments[0].scrollIntoView(true);", benefits_button_click
    )

    benefits_button_click.click()

    cpf_input = WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card/ion-grid/ion-row[2]/ion-col/ion-card/ion-item/ion-input/input',
            )
        )
    )
    cpf_input.send_keys(self.cpf)

    send_cpf_button = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card/ion-grid/ion-row[2]/ion-col/ion-card/ion-button',
            )
        )
    )

    send_cpf_button.click()

  def access_benefits_by_cpf(self):
    benefits_list = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//*[@id="extratoonline"]/ion-row[2]/ion-col/ion-card/ion-grid/ion-row[2]/ion-col/ion-card/ion-item',
            )
        )
    )
    benefits_elements = benefits_list.find_elements(By.XPATH, "*")
    return [benefit.text for benefit in benefits_elements]
