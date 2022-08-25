import requests
from bs4 import BeautifulSoup
import re


class Freelancer:
    def __init__(self):
        self.users = []

    def getFreelancer(self, page):
        r = requests.get(f"https://www.freelancer.mx/freelancers/{page}")

        if r.status_code == 200:

            all_users = re.findall('/u/.+', r.text)
            # eliminar duplicados
            res = [*set(all_users)]

            if res:
                for i in res:
                    self.users.append(i.replace('"', ''))

            # rating = re.findall('data-star_rating="[0-9].[0-9]', r.text)
            # print(rating)

    def getFreelancerData(self):

        if self.users:
            '''
            for i in self.users:
                r = requests.get(f"https://www.freelancer.mx{i}")
                if r.status_code == 200:
                    pass
            '''
            r = requests.get(f"https://www.freelancer.mx{self.users[0]}")
            print(r.url)

            if r.status_code == 200:

                regex = "((https?://cdn)?((?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)"

                soup = BeautifulSoup(r.text, 'html.parser')
                # buscar la foto del perfil
                photo = soup.find_all(
                    "source", attrs={"class": "ng-star-inserted"})

                url_photo = re.findall(regex, str(photo[1]))

                print(url_photo[0][0])

                # precio por hora
                tarifa = soup.find_all(
                    "div", attrs={"class": "NativeElement ng-star-inserted"})

                for i in tarifa:

                    precio = re.findall('\$[0-9]?[0-9] USD / hora', i.text)
                    if precio:
                        print(precio[0])
                        break

                # ubicacion del usuario
                data_elements = soup.find_all(
                    "div", attrs={"class": "NativeElement ng-star-inserted"})

                find_location = '_ngcontent-sc45="" class="NativeElement ng-star-inserted" data-color="dark" data-line-break="false" data-size="xsmall" data-style="normal" data-text-transform="capitalize"'
                location = False
                for i in data_elements:

                    # ubicacion
                    if location == False:

                        if find_location in str(i):

                            print("".join(i.text.split()))
                            location = True

                    # fecha de union
                    if "Se unió" in i.text:
                        print(" ".join(i.text.split()))

                    # numero de recomendaciones
                    if "recomendaciones" in i.text or "Recomendación" in i.text:
                        print(" ".join(i.text.split()))


if __name__ == "__main__":
    data = Freelancer()
    # pages total 840
    data.getFreelancer(1)

    data.getFreelancerData()
