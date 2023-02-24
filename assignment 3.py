#list of cars and their prices
print=('Welcome to Crella cars garage')
cars={'Gmc':'$300,000',
      'Cadillac':'$145,000',
      'Land rover':'$564,000',
      'Dodge':'$111,000',
      'Jeep':'$222,000',
      'Fiat':'$367,000',
      'Kia':'$24,000',
      'Chrysler':'$765,000',
      'Mitsubishi':'$888,900',
      'Acura':'$56,788',
      'Scion':'$64,325',
      'Nisan':'$6,546',
      'Chevrolet':'$255,154',
     'Honda':'$546,954',
      'Ford':'$89,876',
      'Volswagen':'$56,451',
      'Toyota':'$5000',
      'Hyundai':'$5,654',
      'Volvo':'$52,555',
      'Mini':'$51,554',
      'Mercedes-benz':'$556,645',
      'Mazda':'$55,164',
      'Subaru':'$55,348',
      'Audi':'$959,415',
      'Buick':'$641,656',
      'Porsche':'$56,565',
      'Lexus':'$566,546',
      'Porshe':'$56,454',
      'Tesla':'$964,865',
      'Jaguar':'$786,000',
      'Ram':'$654,888'}
carName=input("input carName.").strip()
#check if carBrand in carName
if carName in cars:
    print("carName available")
 #if carName in carBrand is available,get its price
    carprice=cars[carName]
    print(f"The price of {carName} is {carprice}.")
else:
    #if carname not in carBrand
    print("sorry, carName is unavailable.")
         
    
    

