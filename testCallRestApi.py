__author__ = 'dwiveddi'

from iRest import restHelper

url="http://localhost:8080/employees"
headers={"Content-Type": "application/json"}
data = "{\"name\": \"Samwise Gamgee\", \"role\": \"gardener\"}"
expectedResponse = restHelper.ExpectedResponse(200, "{\"id\":3,\"name\":\"Samwise Gamgee\",\"role\":\"gardener\"}",None,False,
                                               contentJsonAttributes=[{"id": 3}, {"name": "Samwise Gamgee"}, {"role":"gardener"}])
response= restHelper.call("POST",url,headers,data,expectedResponse=expectedResponse)


#url="http://localhost:8081/tests/200";
#headers={"Content-Type": "application/json","A":"B"};
#data="{\"name\":\"Divyashree\"}";
#expectedResponse = restHelper.ExpectedResponse(200, "Message from GET of /test/text", headers, False,
                                    #contentJsonAttributes=[ {"hello": "world"}, {"my": "divyashree dwivedi"}, {"x" : [{"a" : "a1"}, {"b":[{"c":"c1"}]}]}]);
#response= restHelper.call("POST",url,headers,expectedResponse=expectedResponse);

