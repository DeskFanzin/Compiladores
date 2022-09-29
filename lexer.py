def lexer(string):
    tokens = []
    token = ""
    for char in string:
        if char == " ":
            if token != "":
                tokens.append(token)
            token = ""
        else:
            ##finding onyl arithmetic operators
            if char in "+*":
                token += char
            ## finding only numbers
            elif char.isdigit():
                token += char
                
    if token != "":
        tokens.append(token)
    print(tokens)
    return tokens

lexer("1 + 2 - 3 * 200 /  AEMKSKMFGSRML DJKASFNJADSFKSS kkk HAHAHAH2H***AHAHHAAH 21U412U412NDSKAJ")