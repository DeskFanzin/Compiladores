class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __repr__(self):
        return '(' + self.type + ' ' + self.text + ')'

def lexer(s):
    tokens = []
    s += '$'
    i = 0

    # find all tokens in 's' and place them as Token objects in 'tokens'
    for i in s:
        if s[i] == ' ':
            i += 1
            continue
        elif s[i] == '+':
            i += 1
            tokens.append(Token('PLUS', '+'))
        elif s[i] == '*':
            i += 1
            tokens.append(Token('TIMES', '*'))
        elif s[i].isdigit():
            number = s[i]
            i += 1
            while s[i].isdigit():
                number += s[i]
                i += 1
            tokens.append(Token('NUMBER', number))
        elif s[i] == '$':
            tokens.append(Token('END', '$'))
            break
        else:
            print('unknown character')

    return tokens

lexer("oi 2 + 2 * 3")