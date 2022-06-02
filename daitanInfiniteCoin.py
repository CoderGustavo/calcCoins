val = float(input("Digite o valor: ")) #Here is getting the value

def makeChange(val): #this function bellow will
    res = [] # save the final result
    example = [0, 0, 0, 0] # this list is a example the returns
    coins = [1, 5, 10, 25] # this list save the coins (pennies, nickels, dimes, quarters)

    total = val # total receive the val
    currentCoin = coins[0] # get the current coin, starting using the pennies
    totalCoinsUsed = 0 # total current coin useds 

    for i, c in enumerate(coins): # this for is run in everything inside the array coins
        indexes = [0] # start indexes list using 0
        vals = [] # start vals list
        while True: # this while insert the current index up to indexes will be index
            if indexes[-1] == i: break
            indexes.append(indexes[-1]+1)

        for a in indexes: vals.append(coins[a]) # this for is adding in vals list the corresponding coin

        vals.sort(reverse=True) # here is sorting the list

        if len(vals) < 4: falta = 4 - len(vals) # here the variable falta is getting whats missing up to complete 4 index in list
        else: falta = 0
            
        for u in range(0, falta): vals.insert(0, 0) # here is adding 0 in start up to complete 4 index in vals list

        currentCoin = max(vals) #getting the higher number from vals list

        while True: # this while is calculating how many each coins need, then add the coins in final list
            if total >= currentCoin:
                total -= currentCoin
                totalCoinsUsed += 1
            else:
                if totalCoinsUsed > 0:
                    currentIndex = vals.index(currentCoin)
                    example[currentIndex] = totalCoinsUsed
                if currentCoin == 25 and currentCoin in vals:
                    currentCoin = 10
                elif currentCoin == 10 and currentCoin in vals:
                    currentCoin = 5
                elif currentCoin == 5 and currentCoin in vals:
                    currentCoin = 1
                totalCoinsUsed = 0
                if total == 0:
                    currentCoin = max(vals)
                    total = val
                    res.append(example)
                    example = [0, 0, 0, 0]
                    break;
    return res # returning the final result list


print(makeChange(val)) #show the final result list in the screen