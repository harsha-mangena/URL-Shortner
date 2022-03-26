#DBMS COnnector
from distutils.log import error
from genericpath import exists
from unittest import result
from xmlrpc.client import Boolean
import mysql.connector as DBconnector\
#Error's
import Error

try:
    connector  = DBconnector.connect(host="localhost", user="root", passwd = "Asdfgh@88", database = "URL")
    cursor = connector.cursor()
        
except:
    Error.databaseConnection()

'''
Checks if the generated shortURL, is already taken or not
If taken re-generares, else stores in shortURL, longURL -> store(longURL, shortURL)
@params -> shortURL -> String 
'''
def isTaken(shortURL) -> Boolean:
    try:
        query = "select * from url_store where shortURL = (%s)";
        value = [(shortURL)]
        exists = cursor.execute(query, value)
        return len(exists[0])
    except:
        return "Error : In is taken "
        

'''
@Params -> longURl, shortURL -> String
'''
def store(shortURL, longURL):
    #Query for storing
    try:
        query = "insert into url_store(shortURL, longURL) values(%s,%s);"
        values = (shortURL, longURL)
        cursor.execute(query, values)
        connector.commit()
    except:
        Error.databaseCommit()
'''
@params -> ShortUrl, give's the longURL
'''
def getlongUrl(shortUrl):
    try:
        query = "select longURL from url_store where shortURL = (%s);"
        value = [(shortUrl)]
        cursor.execute(query, value)
        result = cursor.fetchone()
        return result[0]
    except:
        return Error.databaseConnection()

''''
@params -> LongUrl, give's the shortURL
'''
def getshortUrl(longUrl):
    try:
        query = "select shortURL from url_store where longURL = (%s);"
        value = [(longUrl)]
        cursor.execute(query, value)
        result = cursor.fetchone()
        return result[0]
    except:
        return Error.databaseConnection()

