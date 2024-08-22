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

class BrandbucketDomainList:

    def __init__(self,domainName):
        self.domainName = domainName
        self.domainListObject = {
            'websiteName':'BrandBucket',
            'domainList':[]
        }

    def create_file(self):
        driver = webdriver.Chrome()
        driver.get(f"https://www.brandbucket.com/search?q={self.domainName}")
        time.sleep(10)
        elems = driver.find_elements(By.CLASS_NAME, "dataOverlay")

        with open(f"data/{self.domainName}.html","w",encoding="utf-8") as f:
            for elem in elems:
                try:
                    d = elem.get_attribute("outerHTML")
                    f.write(d)
                except Exception as e:
                    print('Brandbucket create_file exception -> ',e)
                
        time.sleep(2)

        elems.clear()
        driver.close()

    def create_dict(self):
        with open(f"data/{self.domainName}.html","rb") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc,'lxml')

        mainDivs = soup.find_all('div',class_='dataOverlay')

        for mainDiv in mainDivs:
            try:
                data = mainDiv.find_all('span')
                domainNameInHtml = data[0].text
                price = data[1].text
                # print(domainNameInHtml, priceString)
                # price = re.search(r'\$\d+\.\d{2}',priceString).group()

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
    domainName = "Express"
    brandbucketDomainList = BrandbucketDomainList(domainName)
    brandbucketDomainList.create_file()
    domainListObject = brandbucketDomainList.create_dict()
    print(domainListObject)
    porkbunDomainList.delete_file()
