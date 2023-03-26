from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()

driver.get('https://steamdb.info/charts/')
driver.find_element(By.CSS_SELECTOR, "#table-apps_length select").click()
driver.find_element(By.XPATH, '//*[@id="table-apps_length"]/label/select/option[7]').click()
time.sleep(5)
games_data = driver.find_element(By.CSS_SELECTOR, '#table-apps tbody')
data = games_data.text.splitlines()
mpg_list = []
for game in data:
    game = game.split(' ')
    game_position = game[0]
    game_name_in_list = game[1: -4]
    game_name = " ".join(game_name_in_list)
    all_time_peak = game[-2]
    mpg_list.append((game_position, game_name, all_time_peak))

with open('mpg_data', 'w', encoding='utf-8') as mpg:
    csv_file = csv.writer(mpg, delimiter=" ", skipinitialspace=True)
    csv_file.writerow(("Ranking", "Game Name", "All time peak"))
    csv_file.writerows(mpg_list)
