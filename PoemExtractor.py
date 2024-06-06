import os

class PoemExtractor:
    def __init__(self) -> None:
        self.poem_names = list()
        self.poem = list()
        self.start_mark = False
        self.end_mark = False

    def getPoemNames(self, file_name):
        # Using readlines()
        file = open(file_name, 'r')
        Lines = file.readlines()
        
        # Strips the newline character
        for line in Lines:
            char = line[0]
            if char.isalpha():
                self.poem_names.append(line)

        return self.poem_names
    
    def getPoem(self, file_name, poem_name):
        # Using readlines()
        file = open(file_name, 'r')
        Lines = file.readlines()
        
        # Strips the newline character
        for line in Lines:
            if line == poem_name :
                self.start_mark = True
                continue
            else : 
                if self.start_mark == True:
                    # Strips the newline character
                    char = line[0]
                    if char.isalpha():
                        self.end_mark = True
                        break

                    if self.end_mark == False:
                        self.poem.append(line)

        return self.poem

if __name__ == '__main__':
    file_directory = os.path.dirname(os.path.realpath(__file__))
    file_name = file_directory + '\\A dome of many coloredglass2.txt'
    poemExtractor = PoemExtractor()
    poem_names = poemExtractor.getPoemNames(file_name)

    # for name in poem_names:
    #     poem = poemExtractor.getPoem(file_name, name)
    #     print('POEM : {}'.format(name))
    #     print('\t{}'.format(poem))

    poem = poemExtractor.getPoem(file_name, poem_names[0])
    print('POEM : {}'.format(poem_names[0]))
    print('\t{}'.format(poem))
