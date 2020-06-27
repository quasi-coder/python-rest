__author__ = 'dwiveddi'

import json


def toJson(str):
    return json.loads(str)


def toString(json):
    return json.dumps(json)


def validateJsonStructure(expectedJsonAttributes, j, keyPrefix=""):
    if (isinstance(j, list)):
        for jsonElement in j:
            validateJsonStructure(expectedJsonAttributes, jsonElement)
    else:
        for expectedKey in expectedJsonAttributes:
            if (isinstance(expectedKey, dict)):
                keyValPair = expectedKey
                for key in keyValPair:
                    if (key not in j):
                        raise AssertionError("The json does not contains key = '%s%s'. ActualJsonContent = '%s'" % (
                        keyPrefix, expectedKey, toString(j)))
                    elif (isinstance(keyValPair[key], list)):
                        validateJsonStructure(keyValPair[key], j[key], keyPrefix + key + ".");
                    elif (j[key] != keyValPair[key]):
                        raise AssertionError(
                            "The value of jsonKey = '%s%s' is not matched with expectedValue. Expected = '%s' Actual = '%s'" % (
                            keyPrefix, key, keyValPair[key], j[key]));
            elif (expectedKey not in j):
                raise AssertionError("The json does not contains key = '%s%s'. ActualJsonContent = '%s'" % (
                keyPrefix, expectedKey, toString(j)))
