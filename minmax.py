def mini(inlist):
    answer = None 
    for item in inlist:
        if answer == None:
            answer = item
        if item < answer:
            answer = item
    return (answer)