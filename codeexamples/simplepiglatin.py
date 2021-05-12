def pig_it(text):
    
    s=text.split(" ")
    sentence = " "
    for i in s:
        if not (i.isalpha()):
                sentence = sentence + i
        elif (i.isalpha()):
            newword=i[1:]+i[0]+"ay"
            sentence = sentence+newword+ " "
              
    return print(sentence)
