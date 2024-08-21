from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
import os

# OutPut Format

    # {
    #     wbName:"goDaddy",
    #     domainList:[
    #         {
    #             domainName:"google.comcom",
    #             price:"1000.00"
    #         },
    #         .....
    #     ]
    # }

class SedoDomainList:

    def __init__(self,domainName):
        self.domainName = domainName
        self.domainListObject = {
            'websiteName':'sedo.com',
            'domainList':[]
        }

    def create_file(self):
        driver = webdriver.Chrome()
        driver.get(f"https://sedo.com/search/?keyword={self.domainName}")
        time.sleep(10)
        elems = driver.find_elements(By.CLASS_NAME, "item-result")

        with open(f"data/{self.domainName}.html","w",encoding="utf-8") as f:
            for elem in elems:
                d = elem.get_attribute("outerHTML")
                f.write(d)
            
        time.sleep(10)

        elems.clear()
        driver.close()

    def create_dict(self):
        with open(f"data/{self.domainName}.html","rb") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc,'lxml')

        mainDivs = soup.find_all('div',class_='item-result')

        for mainDiv in mainDivs:
            try:
                domainNameInHtml = (mainDiv.div.label.span.text)
                priceString = (mainDiv.find('div',class_="item-price").text)
                
                priceWithComma = re.search(r'\b\d{1,3}(?:,\d{3})+\b',priceString).group()
                price = ""

                for p in priceWithComma:
                    if p != ',':
                        price += p  

                print(domainNameInHtml,' ',price)
                domainObject={
                    'domainName':domainNameInHtml,
                    'price':price
                }


                self.domainListObject.get("domainList").append(domainObject)

            except Exception as e:
                print("exception occured -> ",e)
        
        return self.domainListObject
        
    def delete_file(self):
        file_path = f"data/{self.domainName}.html"

        if os.path.exists(file_path):
            time.sleep(5)
            os.remove(file_path)
            print("File deleted successfully!")
        else:
            print("File not found.")


if __name__ == "__main__":
    domainName = "NaguBhaiDhaba"
    sedoDomainList = SedoDomainList(domainName)
    sedoDomainList.create_file()
    domainListObject = sedoDomainList.create_dict()
    print(domainListObject)
    sedoDomainList.delete_file()
