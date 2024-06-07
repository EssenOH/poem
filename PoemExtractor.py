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
        
        for line in Lines:
            char = line[0]
            if char.isalpha():
                self.poem_names.append(line)

        return self.poem_names
    
    # designed to use with automatically detected poem names, then it doesn't require of conversion for lower case or upper case.
    def getPoem(self, file_name, poem_name):
        self.poem.clear()
        self.start_mark = False
        self.end_mark = False

        # Using readlines()
        file = open(file_name, 'r')
        Lines = file.readlines()
        
        for line in Lines:
            if line == poem_name :
                self.start_mark = True
                continue
            else : 
                if self.start_mark == True:
                    char = line[0]
                    if char.isalpha():
                        self.end_mark = True
                        break

                    if self.end_mark == False:
                        self.poem.append(line)

        return self.poem

    # designed to use poem names which are prepared by human, and then there is some poem name errors.
    # then, it convert the lower case for titles and compare it.
    def getPoemWithRange(self, file_name, start_poem_name, end_poem_name):
        self.poem.clear()
        self.start_mark = False
        self.end_mark = False

        # Using readlines()
        file = open(file_name, 'r')
        Lines = file.readlines()
        
        # there is some mismatching due to lower case & upper case characters, then make all to lower case for the comparison
        # poem names doesn't include the new line character('\n'), added it to make easy comparion.
        # there is an alternative comparing way with elimination of the new line character('\n'), but the treatment is much more complicate,
        # then, simply adding the new line character('\n')
        start_poem_name = start_poem_name.lower()
        start_poem_name = start_poem_name + '\n'

        end_poem_name = end_poem_name.lower()
        end_poem_name = end_poem_name + '\n'

        # Strips the newline character
        for line in Lines:
            if line.lower() == start_poem_name :
                self.start_mark = True
                continue
            else : 
                if self.start_mark == True:
                    if line.lower() == end_poem_name :
                        self.end_mark = True
                        break

                    if self.end_mark == False:
                        self.poem.append(line)

        return self.poem

    # designed to use poem names which are prepared by human, and then there is some poem name errors.
    # then, it convert the lower case for titles and compare it.
    def getLastPoem(self, file_name, poem_name):
        self.poem.clear()
        self.start_mark = False
        self.end_mark = False

        # Using readlines()
        file = open(file_name, 'r')
        Lines = file.readlines()
        
        # there is some mismatching due to lower case & upper case characters, then make all to lower case for the comparison
        # poem names doesn't include the new line character('\n'), added it to make easy comparion.
        # there is an alternative comparing way with elimination of the new line character('\n'), but the treatment is much more complicate,
        # then, simply adding the new line character('\n')
        poem_name = poem_name.lower()
        poem_name = poem_name + '\n'

        # Strips the newline character
        for line in Lines:
            if line.lower() == poem_name :
                self.start_mark = True
                continue
            else :
                if self.start_mark == True:
                    end_value = line.find('THE END')
                    if end_value != -1: # return value -1 doesn't mean the False, then it should use the comparison way
                        break
                    else :
                        self.poem.append(line)

        return self.poem

if __name__ == '__main__':
    file_directory = os.path.dirname(os.path.realpath(__file__))
    file_name = file_directory + '\\A dome of many coloredglass2.txt'
    poemExtractor = PoemExtractor()
    # poem_names = poemExtractor.getPoemNames(file_name)

    # for name in poem_names:
    #     poem = poemExtractor.getPoem(file_name, name)
    #     print('POEM : {}'.format(name))
    #     print('\t{}'.format(poem))

    # poem = poemExtractor.getPoem(file_name, poem_names[0])
    # print('POEM : {}'.format(poem_names[0]))
    # print('\t{}'.format(poem))

    # some of the poem name is different against the actual name in book, then the table is modified
    # i.e. Diya  {original title is Greek, Delta-iota-psi-alpha}, Teatro Bambino.  Dublin, N. H.,J--K. Huysmans
    # On Carpaccio's Picture:  The Dream of St. Ursula

    # In odrder to eliminate the human error, this table should be firstly generated by computer with calling getPoemNames(...)
    # and then it needs to be retouched by human.
    # due to human error, debugging it by junior programmer is not an easy job, then it should be automatically created.
    poem_names =  ['Before the Altar', "Suggested by the Cover of a Volume of Keats's Poems", 'Apples of Hesperides',
              'Azure and Gold', 'Petals', 'Venetian Glass', 'Fatigue', 'A Japanese Wood-Carving', 'A Little Song',
              'Behind a Wall', 'A Winter Ride', 'A Coloured Print by Shokei', 'Song', 'The Fool Errant',
              'The Green Bowl', 'Hora Stellatrix', 'Fragment', 'Loon Point', 'Summer',
              '"To-morrow to Fresh Woods and Pastures New"', 'The Way',
              'Diya  {original title is Greek, Delta-iota-psi-alpha}', 'Roads', 'Teatro Bambino.  Dublin, N. H.',
              'The Road to Avignon', 'New York at Night', 'A Fairy Tale', 'Crowned', 'To Elizabeth Ward Perkins',
              'The Promise of the Morning Star', 'J--K. Huysmans', 'March Evening', 'Leisure',
              "On Carpaccio's Picture:  The Dream of St. Ursula", 'The Matrix', 'Monadnock in Early Spring',
              'The Little Garden', 'To an Early Daffodil', 'Listening', 'The Lamp of Life', 'Hero-Worship',
              'In Darkness', 'Before Dawn', 'The Poet', 'At Night', 'The Fruit Garden Path', 'Mirage', 'To a Friend',
              'A Fixed Idea', 'Dreams', 'Frankincense and Myrrh', 'From One Who Stays', 'Crepuscule du Matin',
              'Aftermath', 'The End', 'The Starling', 'Market Day',
              'Epitaph in a Church-Yard in Charleston, South Carolina', 'Francis II, King of Naples', 'To John Keats',
              'The Boston Athenaeum', 'Sea Shell', 'Fringed Gentians', 'The Painted Ceiling', 'The Crescent Moon',
              'Climbing', 'The Trout', 'Wind', 'The Pleiades']

    count = 0
    number_of_poems = len(poem_names)

    # paired poem titles are required for loop
    for count in range(0,number_of_poems - 1):
        poem = poemExtractor.getPoemWithRange(file_name, poem_names[count], poem_names[count+1])
        print('POEM : {}'.format(poem_names[count]))
        print('\t{}'.format(poem))
        print('--------------------------------------------------------------------------------')

    # the last poem needs a special care because it doesn't have the next poem title.
    poem = poemExtractor.getLastPoem(file_name, poem_names[number_of_poems - 1])
    print('POEM : {}'.format(poem_names[number_of_poems - 1]))
    print('\t{}'.format(poem))
    print('--------------------------------------------------------------------------------')
