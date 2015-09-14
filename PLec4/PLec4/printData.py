def printData(data, cnt=0):
    for item in data:
        if isinstance(item, list):
            printData(item, cnt+1) #Àç±Í!!!!!
        else:
            print("\t"*cnt, end="")
            print(item)

#isinstance¸¦ ½è´Âµ¥ list¾È¿¡ list°¡ ¸î¹øÀÌ³ª ±í¾îÁö´ÂÁö ¸ğ¸¥´Ù¸é??? Àç±ÍÀç±ÍÀç±ÍÀç±ÍÀç±ÍÀç±ÍÀç±Í