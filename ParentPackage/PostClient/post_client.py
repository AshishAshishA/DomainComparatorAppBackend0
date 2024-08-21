from WebScrappers.PorkbunWebScrapper import PorkbunDomainList
from WebScrappers.NamecheapWebScrapper import NamecheapDomainList
from WebScrappers.SedoWebScrapper import SedoDomainList
from WebScrappers.DynadotWebScrapper import DynadotDomainList
from WebScrappers.BrandbucketWebScrapper import BrandbucketDomainList
from .post_interface import PostInterface
from .format_change_interface import FormatChangeInterface


class PostClientClass:

    def callPost(self,postFormat):
        

        postObject = PostInterface()

        url = 'https://domaincomparatorappbackend0.onrender.com/domains/details1/'
        for postData in postFormat:
            # print('postData -> ',postData)
            postObject.setPayload(url,postData)
            r = postObject.postPayload()
            # print(r.status_code)

    def PorkbunPost(self,domainName):
        
        porkbunDomainList = PorkbunDomainList(domainName)

        porkbunDomainList.create_file()
        domainListObject = porkbunDomainList.create_dict()  

        fciObject = FormatChangeInterface(domainListObject)
        postFormat = fciObject.changeFormat()

        porkbunDomainList.delete_file()

        self.callPost(postFormat)

    def NamecheapPost(self,domainName):
        
        namecheapDomainList = NamecheapDomainList(domainName)

        namecheapDomainList.create_file()
        domainListObject = namecheapDomainList.create_dict()  

        fciObject = FormatChangeInterface(domainListObject)
        postFormat = fciObject.changeFormat()

        namecheapDomainList.delete_file()

        self.callPost(postFormat)

    def SedoPost(self,domainName):
        
        sedoDomainList = SedoDomainList(domainName)

        sedoDomainList.create_file()
        domainListObject = sedoDomainList.create_dict()  

        fciObject = FormatChangeInterface(domainListObject)
        postFormat = fciObject.changeFormat()

        sedoDomainList.delete_file()

        self.callPost(postFormat)

    def DynadotPost(self,domainName):
        
        dynadotDomainList = DynadotDomainList(domainName)

        dynadotDomainList.create_file()
        domainListObject = dynadotDomainList.create_dict()  

        fciObject = FormatChangeInterface(domainListObject)
        postFormat = fciObject.changeFormat()

        dynadotDomainList.delete_file()

        self.callPost(postFormat)

    def BrandbucketPost(self,domainName):
        
        brandbucketDomainList = BrandbucketDomainList(domainName)

        brandbucketDomainList.create_file()
        domainListObject = brandbucketDomainList.create_dict()  

        fciObject = FormatChangeInterface(domainListObject)
        postFormat = fciObject.changeFormat()

        brandbucketDomainList.delete_file()

        self.callPost(postFormat)



    


if __name__ == '__main__':
    postClientObject = PostClientClass() 
    postClientObject.PorkbunPost('BucketMarket')