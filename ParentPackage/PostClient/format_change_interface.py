
from WebScrappers import PorkbunWebScrapper

# Input Format

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

# Output Format 

    # [
    #     {
    # 		"domainName": "google",
    # 		"price": "1000.00",
    # 		"websiteName": {
    # 			"name": "goDaddy"
    # 		},
    # 		"domainSuffix": {
    # 			"suffix": "comcom"
    # 		}
    #     }
    #     .....
    # ]


class FormatChangeInterface:

    def __init__(self,domainListObject):
        self.postFormat=[]
        self.domainListObject = domainListObject

    def changeFormat(self):
        websiteName = self.domainListObject.get('websiteName')
        for data in self.domainListObject.get('domainList'):
            domainName = data.get('domainName').split(".")[0]
            suffix = data.get('domainName').split(".")[1]
            price = data.get('price')
            
            if price[0]=='$':
                price = price[1:]

            domainObject = {
                "domainName": domainName,
                "price": price,
                "websiteName": {
                    "name": websiteName
                },
                "domainSuffix": {
                    "suffix": suffix
                }
            }
            self.postFormat.append(domainObject)

        return self.postFormat


if __name__ == "__main__":
    domainName = "NaguBhaiDhaba"
    porkbunDomainList = PorkbunWebScrapper.PorkbunDomainList(domainName)

    porkbunDomainList.create_file()
    domainListObject = porkbunDomainList.create_dict()
    fciObject = FormatChangeInterface(domainListObject)
    postFormat = fciObject.changeFormat()

    porkbunDomainList.delete_file()

    print(postFormat)
