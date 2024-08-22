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

class PorkbunDomainList:

    def __init__(self,domainName):
        self.domainName = domainName
        self.domainListObject = {
            'websiteName':'porkbun',
            'domainList':[]
        }

    def create_file(self):
        driver = webdriver.Chrome()
        driver.get(f"https://porkbun.com/checkout/search?prb=769bc09b57&q={self.domainName}.com&tlds=&idnLanguage=&search=search&csrf_pb=4bfc194a0209b0b2d60ce9fe459e76a1")
        time.sleep(2)
        elems = driver.find_elements(By.CLASS_NAME, "searchResultRowTable")

        with open(f"data/{self.domainName}.html","w",encoding="utf-8") as f:
            for elem in elems:
                try:
                    d = elem.get_attribute("outerHTML")
                    f.write(d)
                except:
                    print("NameCheap File-Create exception -> ",e)
                    
        time.sleep(2)
        elems.clear()
        driver.close()

    def create_dict(self):
        with open(f"data/{self.domainName}.html","rb") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc,'lxml')

        mainDivs = soup.find_all('div',class_='row')

        for mainDiv in mainDivs:
            try:
                domainNameInHtml = (mainDiv.find('div',class_="availableDomain").text)
                priceString = (mainDiv.find('span',class_="childContent").text)
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
    porkbunDomainList = PorkbunDomainList(domainName)
    porkbunDomainList.create_file()
    domainListObject = porkbunDomainList.create_dict()
    print(domainListObject)
    porkbunDomainList.delete_file()
