import os
import re
from basicsFunctions import list_of_files

def speeches_to_lowercase():
    directory = ('./speeches')
    extension = 'txt'
    files_names = list_of_files(directory, extension)
    for name in files_names:
        newName = name.split('.')[0] + '_lowercased.txt'
        with open('./speeches/' + name, 'r') as rawText, open('./cleaned/' + newName, 'w') as minimizedText:
            for line in rawText:
                line = line.lower()
                minimizedText.write(line)
    return True


def lowercase_to_clean():
    directory = ('./cleaned/')
    extension = 'txt'
    files_names = list_of_files(directory, extension)
    for name in files_names:
        newName = name.replace('lowercased', 'cleaned')
        if 'lowercased' in name:
            with open(directory + name, 'r') as lowercasedText, open(directory + newName, 'w') as cleanedText:
                for line in lowercasedText:
                    for character in line:
                        if not (character.isalpha()) and not (character.isnumeric()):
                            line = line.replace(character, ' ')
                    line = re.sub(' +', ' ', line)
                    line = line.lstrip()
                    cleanedText.write(line)
            os.remove(directory + name)
    return True


