import re


string = 'do[ declare list(\'diatari_105\' . \'insote_564\' ) ==> "enen". ], [\
declare list( \'edenen\' .\'dianqu\' . \'leeser_273\'. \'anan_772\' ) ==>\
"usreon". ],[declare list(\'tibeor\' . \'bealari\' . \'esle\' ) ==>\
"esedso". ], od'
 
def main(message):
    lastIndex = 0
    dictionary = {}
    keys = []
    indexes = []
    listes = []
    values = []
    keys = re.findall(r'"(.*?)"', message)
    dot = message.find('.', message.find('.') + 1)
    for i in range(0, len(message)):
        if(message[i] == ','):
            indexes.append(i)
    for i in range(0, len(indexes)):
        if i == 0:
            listes.append(message[:indexes[i]])
        else:
            listes.append(message[lastIndex:])
        lastIndex = indexes[i]
    for i in range(0, len(listes)):
        values.append(re.findall(r"'([^']*)'", listes[i]))
        dictionary[keys[i]] = values[i]
    return dictionary

print(main(string))