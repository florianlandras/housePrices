baseUrl = 'https://www.hemnet.se/salda/'
city = 'soderkopings-kommun'



data = {'typeBostad': ['villa'],
        'sizeMin': [""],
        'sizeMax': [""],
        'nbrOfRoomMin': [""],
        'nbrOfRoomMax': [""],
       
        }

df = pd.DataFrame(data)
dfA = str(df["typeBostad"])
dfB = str(df["sizeMin"] )
dfC = str(df["sizeMax"])
dfD = str(df["nbrOfRoomMin"])
dfE = str(df["nbrOfRoomMax"])
dfF = str(df["typeBostad"] )

type(dfA)



typeBostad = ''
sizeMin =''
sizeMax = ''
nbrDeChambreMin = ""
nbrDeChambreMax = ""


def is_not_blank(s):
    return bool(s and s.strip())

url = baseUrl+city

def dataJson () :

    html = requests.get(url) 
    dataLayer = re.findall("dataLayer = (.+?);\n", html.text, re.S)
    varJson = json.loads(dataLayer[0])
    cityId = varJson[1]["results"]["locations"][0]["id"]
    

    return cityId

dataJson()

def newUrl() :
    
    # si typeBostad & 
    newUrl = ""
    
    if is_not_blank(typeBostad) == False and is_not_blank(sizeMin) == False and is_not_blank(sizeMax) == False and is_not_blank(sizeMin) and is_not_blank(sizeMin) :
        
        newUrl = baseUrl + "bostader?location_ids%5B%5D=" + str(dataJson()) + "&sold_age=all"
    
    if is_not_blank(typeBostad) == True and is_not_blank(sizeMin) == False and is_not_blank(sizeMax) == False and is_not_blank(sizeMin) and is_not_blank(sizeMin) :
        
        newUrl = baseUrl + "bostader?location_ids%5B%5D=" + str(dataJson()) + "&item_types%5B%5D="+ typeBostad + "&sold_age=all"
    
   #if is_not_blank(typeBostad) == False and is_not_blank(sizeMin) == True and is_not_blank(sizeMax) == False :
        
        newUrl = baseUrl + "bostader?location_ids%5B%5D=" + str(dataJson()) + "&item_types%5B%5D="+ typeBostad + "&sold_age=all"
        
    #if is_not_blank(typeBostad) == False and is_not_blank(sizeMin) == False and is_not_blank(sizeMax) == True :
        
        newUrl = baseUrl + "bostader?location_ids%5B%5D=" + str(dataJson()) + "&item_types%5B%5D="+ typeBostad + "&sold_age=all"
        
    #if is_not_blank(typeBostad) == True and is_not_blank(sizeMin) == True and is_not_blank(sizeMax) == True :
        
        newUrl = baseUrl + "bostader?location_ids%5B%5D=" + str(dataJson()) + "&item_types%5B%5D="+ typeBostad + "&sold_age=all"
    return newUrl

# nouvelle adresse format : https://www.hemnet.se/salda/bostader?location_ids%5B%5D=18002&item_types%5B%5D=villa&sold_age=all


#newUrl = baseUrl + "bostader?location_ids%5B%5D=" + str(dataJson()) + "&sold_age=all"

newUrl()