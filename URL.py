from random import randint
from tokenize import String
import DataStore
import Error

'''
Method for generating and storing the longURL, shortURL
'''
def ShortUrl(longUrl, tokens)->String:
    shortUrl = "https://short/"
    for i in range(8):
        shortUrl += tokens[randint(0, len(tokens)-1)]
    #Storing in Database
    DataStore.store(shortUrl, longUrl)
    #Return ShortUrl
    return shortUrl

'''
Method for getting  LongURL 
@params : shortUrl -> String 
'''
def getLongUrl(shortUrl)->String:
    longUrl = DataStore.getlongUrl(shortUrl)
    return longUrl

'''
Methos for getting shortURL
@params : longUrl -> String
'''
def getShortUrl(longUrl) -> String:
    shortUrl = DataStore.getshortUrl(longUrl)
    return shortUrl
    