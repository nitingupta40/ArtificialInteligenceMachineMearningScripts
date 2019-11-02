# -*- coding: utf-8 -*-
"""
Created on Wed Sep 09 17:06:34 2015

@author: nitin
"""

import httplib
from xml.dom.minidom import parse, parseString, Node
devKey = '4ac469d4-9dde-4071-9f8a-1841027cc274'
appKey = 'freelanc-cd19-4ae3-9d8f-2c21b9a3b3dc'
certKey = 'a6c68921-10b3-4124-b3d4-68ab41769cd0'
userToken ='AgAAAA**AQAAAA**aAAAAA**JRnwVQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AGmISjDZeKoQWdj6x9nY+seQ**KPwCAA**AAMAAA**M0Q63h5cU5Z2a5GNExz3287WsjXk1PBfZQGOUAjyJFfHXdOPjqdC9fHurg17uHjjML1VTkNAIkpwFOM8VscHH5vGk84TV00Df0J4p8IY8KhUwCGdXEKFn2JbDfHAl74L8vuYrlQI3mFlH8SwS5medkdK1pXnXMdBFZUsHsj0yKuIXr7//qO19oFOnfTF5V9EEjpW38j3Nu2goJ2A9kieT4KDYXnGzqADdG7CWlqE8+wYwYKaQo6WOhTPwDHMySdsUsE0ivwOYNPwc9qGkN/UWTmq6jsp7vAVht0+urA/+5Q1Xj0UAE++pcc3zbuSiDZ4r8mmMEvA5/YgKvaY0uMgDtbiONQyBLaRKuLG4tZ8eJXUd6/m/PRFtk4g5WKpXNQlrL42yqG2q1tFyVtbWXScaCH5GWciR5K0kVD90RFpQagjgCLlvA5ohO7xSPv97ubwb0UFRB0GfaXThGE7q7ahCHb+o6Vy64auwyJulVPyv7MElXkOwJTZjiV4ci5orXBznBo6E95VmYQSvpfe/MpaJseTXdPW+LkWmLIMeVPdjY/deVva9R6VSgDVbQ5qt8G+NZo3fTxSGpqSjvIa0egwBnmmv8/pf8yns5bxvspLpK/0mUn89YPbnifGpR0UMNZ0EkYEape98RV3p4unUqiWo2oPcUXBEUbX65q5ZtOC5NPYwPGQP8j/LXtjcuhKGm7g1xnN+qAKccE4GfcKPFnrruSBDPInNSAb9D3FuB94N4toehCWT5hzE/nl9qmRpjFz'
serverUrl ='api.ebay.com'
def getHeaders(apicall,siteID="0",compatabilityLevel = "433"):  
    headers = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatabilityLevel,             
               "X-EBAY-API-DEV-NAME": devKey,             
               "X-EBAY-API-APP-NAME": appKey,             
               "X-EBAY-API-CERT-NAME": certKey,             
               "X-EBAY-API-CALL-NAME": apicall,             
               "X-EBAY-API-SITEID": siteID,             
               "Content-Type": "text/xml"}
    return headers
    
def sendRequest(apicall,xmlparameters):  
    connection = httplib.HTTPSConnection(serverUrl)  
    connection.request("POST", '/ws/api.dll', xmlparameters, getHeaders(apicall))  
    response = connection.getresponse()  
    if response.status != 200:    
        print "Error sending request:" + response.reason  
    else:    data = response.read()    
    connection.close()  
    return data

def getSingleValue(node,tag):  
    nl=node.getElementsByTagName(tag)  
    if len(nl)>0:    
        tagNode=nl[0]    
        if tagNode.hasChildNodes():      
            return tagNode.firstChild.nodeValue  
    return '-1'
    
def doSearch(query,categoryID=None,page=1):  
    xml = "<?xml version='1.0' encoding='utf-8'?>"+      
    "<GetSearchResultsRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\        
    "<RequesterCredentials><eBayAuthToken>" +\        
    userToken +\        "</eBayAuthToken></RequesterCredentials>" + \       
    "<Pagination>"+\          "<EntriesPerPage>200</EntriesPerPage>"+\          
    "<PageNumber>"+str(page)+"</PageNumber>"+\        "</Pagination>"+\        
    "<Query>" + query + "</Query>"  
    if categoryID!=None:    
        xml+="<CategoryID>"+str(categoryID)+"</CategoryID>"  
    xml+="</GetSearchResultsRequest>"
    data=sendRequest('GetSearchResults',xml)  
    response = parseString(data)  
    itemNodes = response.getElementsByTagName('Item');  
    results = []  
    for item in itemNodes:    
        itemId=getSingleValue(item,'ItemID')    
        itemTitle=getSingleValue(item,'Title')    
        itemPrice=getSingleValue(item,'CurrentPrice')    
        itemEnds=getSingleValue(item,'EndTime')    
        results.append((itemId,itemTitle,itemPrice,itemEnds))  
    return results