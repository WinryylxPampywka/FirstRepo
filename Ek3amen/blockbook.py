import requests
response = requests.get("https://httpbin.org/get")
print(response.content)
#print(type(response.content))

#print(response.text)

response2 = requests.post("https://www.quotegarden.com/mind.html",
                          data="test data",
                          headers={"h1" : "Test Title"}
                          )
print(response2.text)