import requests
import time
# from post_client import PostClientClass
from PostClient.post_client import PostClientClass

url = 'https://domaincomparatorappbackend0.onrender.com/domains/searched/'

r = requests.get(url)

print(r.status_code)
post_client_object = PostClientClass()
if r.status_code == 200:
    searchedObjects = (r.json())

    for searchedObject in searchedObjects:
        search_name = searchedObject.get('searchedName')
        stayIndex = searchedObject.get('stayIndex')
    
        if stayIndex > 0:
            # post_client_object.PorkbunPost(search_name)
            # post_client_object.NamecheapPost(search_name)
            # post_client_object.SedoPost(search_name)
            # post_client_object.DynadotPost(search_name)
            post_client_object.BrandbucketPost(search_name)

            time.sleep(2)

            payload = {
                "searchedName": search_name,
                "searchFreq": 0,
                "stayIndex":-7,
            }
        else:
            stayIndex += 1
            payload = {
                "searchedName": search_name,
                "searchFreq": 0,
                "stayIndex":stayIndex,
            }
        requests.post(url,payload)



