def ReadTextOfFile(filename, mode='r', encoding='utf-8'):
    file = open(filename, mode, encoding=encoding)
    text = file.read()
    file.close()
    return text

#todo: tirar o diretorio pai da string fixa, pq pode dar pau no linux
def TextInfoTrab():
    return ReadTextOfFile('../texts/Text_InfoTrab.txt')

def TextHelpTrab():
    return ReadTextOfFile('../texts/Text_HelpTrab.txt')