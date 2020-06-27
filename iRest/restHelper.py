__author__ = 'dwiveddi'

import requests
from iJson import jsonHelper;


class ExpectedResponse(object):
    statusCode = -1
    isExactContentCheckRequired = False
    contentJsonAttributes = None
    content = None
    headers = {}

    def __init__(self, statusCode, content, headers, isExactContentCheckRequired, contentJsonAttributes):
        self.statusCode = statusCode
        self.content = content
        self.headers = headers
        self.isExactContentCheckRequired = isExactContentCheckRequired
        self.contentJsonAttributes = contentJsonAttributes


def call(httpMethod, url, headers=None, data=None, files=None, expectedResponse=None):
    if httpMethod == "GET":
        response = requests.get(url, headers=headers)
    elif httpMethod == "POST":
        response = requests.post(url, headers=headers, data=data)
    elif httpMethod == "PUT":
        response = requests.put(url, headers=headers, data=data)
    elif httpMethod == "PATCH":
        response = requests.patch(url, headers=headers, data=data)
    elif httpMethod == "DELETE":
        response = requests.delete(url, headers=headers, data=data)
    else:
        raise NameError("httpMethod = '%s' is not handled", httpMethod)

    if expectedResponse != None:
        validateResponse(expectedResponse, response)
    return response


def validateResponse(expectedResponse, response):
    if (response.status_code != expectedResponse.statusCode):
        raise AssertionError("Expected Status code '%s' doesn't match actualCode '%s'" % (
            expectedResponse.statusCode, response.status_code))
    if (expectedResponse.isExactContentCheckRequired):
        if (response.content != expectedResponse.content):
            raise AssertionError("Expected Response Content '%s' doesn't match actual content '%s'" % (
                expectedResponse.content, response.content))
    elif (expectedResponse.contentJsonAttributes != None):
        jsonHelper.validateJsonStructure(expectedResponse.contentJsonAttributes, jsonHelper.toJson(response.content))
