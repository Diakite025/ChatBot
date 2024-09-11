import json
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Spécifiez le chemin complet vers chromedriver.exe
chrome_driver_path = "C:\\Users\\matyl\\OneDrive\\Bureau\\ProjetWebScrapping\\projetchatbot\\driver\\chromedriver.exe"
# Configurer le service Chrome
chrome_service = ChromeService(chrome_driver_path)

# Créez une instance du navigateur Chrome en utilisant le service
driver = ChromeDriver(service=chrome_service)

# URL de la page principale contenant les liens vers les pages des batteries
main_url = "https://www.nkon.nl/fr/rechargeable/batterie-chimique/li-ion.html"

# Ouvrez la page web principale dans le navigateur
driver.get(main_url)

# Créez une liste pour stocker les données des batteries
battery_list = []

while True:
    # Attendez que l'élément "products-grid" soit présent
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "products-grid"))
    )

    # Trouver tous les batteries sur la page principale
    product = driver.find_element(By.CLASS_NAME, "products-grid")
    battery_names = product.find_elements(By.CLASS_NAME, "product-name")

    # Parcourez les pages de batteries
    for link in range(len(battery_names)):
        # Recueillez à nouveau les liens à chaque itération
        battery_names = driver.find_elements(By.CLASS_NAME, "product-name")

        if link < len(battery_names):
            battery_url = battery_names[link].find_element(By.TAG_NAME, "a").get_attribute("href")
            print("Accéder à la page de la batterie :", battery_url)

            # Accédez à la page de la batterie
            driver.get(battery_url)

            try:
                # Attendez que l'élément "short-description" soit présent
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "short-description"))
                )

                # Trouver le <div> contenant les caractéristiques
                characteristics_div = driver.find_element(By.CLASS_NAME, "short-description")

                # Trouver tous les éléments <th> dans la classe "label"
                th_elements = characteristics_div.find_elements(By.CLASS_NAME, "label")

                # Vérifiez si toutes les caractéristiques recherchées sont présentes
                required_characteristics = ["Poids - g", "Capacité typ. - mAh", "Tension nominale", "Min. capacité - mAh", "Marque", "EAN / GTIN"]
                all_required_present = all(required in [th.text.strip() for th in th_elements] for required in required_characteristics)

                if all_required_present:
                    characteristics = {}
                    for th in th_elements:
                        th_text = th.text.strip()
                        if th_text == "EAN / GTIN":
                            td_element = th.find_element(By.XPATH, "./following-sibling::td")
                            td_text = td_element.text.strip()
                            characteristics["_id"] = td_text
                        elif th_text != "EAN / GTIN" and th_text in required_characteristics:
                            td_element = th.find_element(By.XPATH, "./following-sibling::td")
                            td_text = td_element.text.strip()
                            characteristics[th_text] = td_text
                    characteristics["URL"] = battery_url
                    battery_list.append(characteristics)

            except Exception as e:
                print("Erreur lors de l'accès aux caractéristiques de la batterie:", str(e))

            # Revenez à la page précédente pour accéder aux autres batteries
            driver.execute_script("window.history.go(-1)")

    # Recherchez le bouton "Next" pour passer à la page suivante
    next_button = driver.find_elements(By.CLASS_NAME, "next")
    if not next_button:
        print("Aucun bouton 'Next' trouvé. Fin de la pagination.")
        break  # Sortez de la boucle si le bouton "Next" n'est pas trouvé

    # Cliquez sur le bouton "Next" pour accéder à la page suivante
    next_button[0].click()
    print("Passage à la page suivante.")

# Sérialisez la liste en format JSON avec UTF-8
battery_json_str = json.dumps(battery_list, ensure_ascii=False, indent=4)

# Écrivez le JSON dans un fichier en utilisant l'encodage UTF-8
with open("battery_data.json", "w", encoding="utf-8") as json_file:
    json_file.write(battery_json_str)

# Fermez le navigateur une fois que vous avez terminé
driver.quit()
