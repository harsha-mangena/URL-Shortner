from tokenize import String
import URL
class Application:
    def __init__(self) -> None:
        #Tokens for random generation of short URL
        self.token = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
    '''
    URL creating method
    return and stores -> shortURL for longURL
    @param : LongURL -> String, token -> String
    '''
    def generateUrl(self, longUrl):
        op = URL.ShortUrl(longUrl, self.token )
        return op
    '''
    Getting already existing longUrl by shortUrl from mySql
    @param : shortUrl -> String
    '''
    def getlongUrl(self, shortUrl) -> String:
        longurl = URL.getLongUrl(shortUrl)
        return longurl
    '''
    Getting the shortUrl
    @param :  longUrl -> String
    '''
    def getShortUrl(self, longUrl) -> String:
        shorturl = URL.getShortUrl(longUrl) 
        return shorturl

a = Application()
print("1)Generate new URL\n2)Get the Short Url\n3)Get the Long Url")
choice = input()
if choice == "1":
    originalUrl = input("Enter URL : ")
    print(a.generateUrl(originalUrl))
elif choice == "2":
    long_url = input("Enter Long Url : ")
    print(a.getShortUrl(long_url))
elif choice == "3":
    short_url = input("Enter Short Url : ") 
    print(a.getlongUrl(short_url))