from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Accepted-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

response = requests.get('https://appbrewery.github.io/Zillow-Clone/', headers=header)

#colocando o arquivo em hmtl dentro da classe do beautifulsoup
data = response.text
soup = BeautifulSoup(data, 'html.parser')

#criando uma lista com os elementos  css e selecionando os links que estao no ancor/ancora html
all_link_elements = soup.select('.StyledPropertyCardDataWrapper a')
all_links = [link['href'] for link in all_link_elements]
print(f'sao {len(all_links)} links ao todo')
print(all_links)

#criando uma lista com os nomes dos enderecos pelos elementos css e fazendo uma limpeza de dados
all_address_elements = soup.select('.StyledPropertyCardDataWrapper address')
all_addresses = [address.get_text().replace(' | ', '').strip() for address in all_address_elements]
print(f' sao ao todo {len(all_addresses)} enderecos ao todo')
print(all_addresses)

#criando uma lista de precos usando os elementos do css
all_prices_elements = soup.select('.PropertyCardWrapper span')
all_prices = [price.get_text().replace('/mo', '').split('+')[0] for price in all_prices_elements if '$' in price.text]
print(f'ao topo sao {len(all_prices)} precos cadastrados')
print(all_prices)


#apos as listas feitas vamos colocar os dados no nosso formulario

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#para cada link vamos fazer as seguintes açoes:
for i in range(len(all_links)):

    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScGSJ1d51J8ynC5TBYnsYgFp9kw4nvE4A_hvVv4txSYGogVxA/viewform?usp=header')
    time.sleep(3)

    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price = driver.find_element(by=By .XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link = driver.find_element(by=By .XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element(by=By .XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    #adiciona o elemento das listas feitas anteriormente no seu respectivo campo
    address.send_keys(all_addresses[i])
    price.send_keys(all_prices[i])
    link.send_keys(all_links[i])
    submit_button.click()
print('o codido funcionou')