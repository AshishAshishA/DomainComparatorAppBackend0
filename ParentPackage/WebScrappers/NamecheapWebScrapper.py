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

class NamecheapDomainList:

    def __init__(self,domainName):
        self.domainName = domainName
        self.domainListObject = {
            'websiteName':'NameCheap',
            'domainList':[]
        }

    def create_file(self):
        driver = webdriver.Chrome()
        driver.get(f"https://www.namecheap.com/domains/registration/results/?domain={self.domainName}")
        time.sleep(2)
        elems = driver.find_elements(By.TAG_NAME, "article")

        with open(f"data/{self.domainName}.html","w",encoding="utf-8") as f:
            for elem in elems:
                try:
                    d = elem.get_attribute("outerHTML")
                    f.write(d)
                except Exception as e:
                    print("NameCheap File-Create exception -> ",e)

        time.sleep(2) 
        elems.clear()
        driver.close()

    def create_dict(self):
        with open(f"data/{self.domainName}.html","rb") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc,'lxml')

        articles = soup.find_all('article',class_='available')

        for article in articles:
            try:
                domainNameInHtml = (article.find('div',class_="name").h2.text)
                priceString = (article.find('span',class_="label").text)
                price = re.search(r'\$\d+\.\d{2}',priceString).group()

                domainObject={
                    'domainName':domainNameInHtml.strip(),
                    'price':price.strip()
                }


                self.domainListObject.get("domainList").append(domainObject)

            except Exception as e:
                print("exception occured -> ",e)
        
        return self.domainListObject
        
    def delete_file(self):
        file_path = f"data/{self.domainName}.html"

        if os.path.exists(file_path):
            time.sleep(2)
            os.remove(file_path)
            print("File deleted successfully!")
        else:
            print("File not found.")


if __name__ == "__main__":
    domainName = "NaguBhaiDhaba"
    namecheapDomainList = NamecheapDomainList(domainName)
    namecheapDomainList.create_file()
    domainListObject = namecheapDomainList.create_dict()
    print(domainListObject)
    namecheapDomainList.delete_file()
