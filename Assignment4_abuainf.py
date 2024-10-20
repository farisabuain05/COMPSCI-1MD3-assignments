'''COMPSCI 1MD3 Assignment 4: Length Count, Word Count, and Word Search
Defines length_count function, which counts number of words of each length (up to the longest one) in a given list.
Defines word_count function, which counts number of words starting with letters from A to Z, again in a given list.
Finally, defined word_search function, which searches for a given string, 'word', in a list of strings, 'board'.
Faris Abuain, McMaster University, June 2024.'''

## Counting Words by Length

def length_count(words):
    ''' Length Count: counts number of words (string in a list) of length 0 to maximum length in list.

    Parameters:
        words: list of strings.
        
    Returns:
        string containing list of the count for each given word length. 
        
    Outputs:
        none'''
    
    word_lengths_count = [] # intialize count list
    max_len = 0
    for word in words: # determines the longest word in the list
        if len(word) > max_len:
            max_len = len(word)
    for i in range(1, max_len+1): # checks for words from length 1 to max_len
        count = 0 # intialize count variable
        for word in words:
            if len(word) == i:
                count+=1
        word_lengths_count.append(count)
    return f'The number of strings of length 1 to {max_len} is {word_lengths_count}'

## Define test-list of words

my_words = ['geek', 'hello', 'breh', 'ok']

print(length_count(my_words))  ## call the function with the above list of words


## Counting Words by First Letter

from string import ascii_lowercase # import ascii_lowercase (lowercase alphabet)

def word_count(words):
    ''' Word Count: counts number of words starting with each letter from A to Z.

    Parameters:
        words: list of strings
        
    Returns:
       string with the number of words starting with each given letter
        
    Outputs:
        none'''
    
    listy_wisty_pisty = [] # intialize list to store word counts
    for c in ascii_lowercase:
        count = 0 # intialize count variable
        for word in words: # checks each word individually
            word = word.lower()
            if word[0] == c: # check word[0] -- the starting letter
                count +=1
        listy_wisty_pisty.append(count)
    return f'From a to z, letters starting with these letters occured in the following frequency: {listy_wisty_pisty}'

print(word_count(my_words))  ## call function using my_words list from above


## WORD SEARCH

def word_search(board, word):
    ''' Word Search: searches for a word in a given 'board'/puzzle (list of strings).

    Parameters:
        board: list of strings (acts as the search puzzle)
        word: the specific string of characters we're searching for
        
    Returns:
        True: if word is in board (diagonally, horizontally, or vertically)
        False: if word is not in board
        
    Outputs:
        none'''
    
    word = word.lower()  # convert word to all lowercase -- avoids case sensitivity issues
    word = word.replace(' ', '') # removes any whitespace (which would not be contained in the puzzle)
    for i in range(len(board)):
        string = board[i]  # defines given row of 'board' list as the string indexed at i
        string = string.lower() # (convert to lowercase)
        if word in string: 
            return True 
        elif word in string[::-1]: # checks reverse of the row for 'word'
            return True 
        diag_string = ''.join(board[c-i][c] for c in range(len(string))) # creating a string of characters on a given diagonal
        diag_string = diag_string.lower() # (convert to lowercase)
        if word in diag_string: 
            return True  
        elif word in diag_string[::-1]: # checks reverse of the diagonal
            return True 
        back_diag_str = ''.join(board[c-i][len(string)-c-1] for c in range(len(string))) # creates a backwards diagonal string
        back_diag_str = back_diag_str.lower() # (convert to lowercase)
        if word in back_diag_str: 
            return True 
        elif word in back_diag_str[::-1]: # checks reverse of backwards diagonal
            return True 
        top_down = ''.join(board[x][i] for x in range(len(board))) # creates a vertical column string (from top to bottom)
        top_down = top_down.lower() # (converts to lowercase)
        if word in top_down: 
            return True 
        elif word in top_down[::-1]: # checks reverse of vertical column
            return True
    return False # returns False if none of the above conditions are met


## Test Cases for Word Search Function

def test_ws():
    ''' Test Word Search: calls word_search function for certain test cases of 'board' and 'word'.

    Parameters:
        none.
        
    Returns:
        none.
        
    Outputs:
        prints out the value returned from calling word_search for a given test case.'''
    
    ## Sample puzzle
    puzzle = [
    "KLIMTSEINWORBCHOC",
    "CGOLYNASEMISWEETT",
    "EHNCSDENETEEWSNUO",
    "RCIIOENIIGFILLING",
    "SIOPKCLADNABFTESE",
    "KFRNSAOFCEIOOMCTV",
    "NRHEFDBAFTRSOEHEI",
    "ICATAERTTUIGDDOGT",
    "RORDSNCECCRONSCNC",
    "DOWEFTRTEUTTUIOII",
    "GKHTASPCIRPOHFLDD",
    "NIIEWMRUEOICOTADD",
    "IETESEPSRCNNAHTUA",
    "CSESAESIIYDEBKIPO",
    "ITIMBERLEUSAROEAM",
    "AWFUDGECEARCAYRSO",
    "SUGARDTESSUOMRSEE"
    ]
    
    ## Sample Set of Words
    words = [
    "ADDICTIVE",
    "BAKING",
    "BARS",
    "BITTERSWEET",
    "BROWNIES",
    "CAKES",
    "CANDY",
    "CHIPS",
    "CHOCOLATIERS",
    "COCOA",
    "CONFECTIONERY",
    "COOKIES",
    "CREAM PIE",
    "CUPCAKE",
    "DARK",
    "DECADENT",
    "DELICIOUS",
    "DESSERT",
    "DRINKS",
    "FILLING",
    "FONDUE",
    "FOOD",
    "FUDGE",
    "ICE CREAM",
    "ICING",
    "INGREDIENT",
    "MILK",
    "MOUSSE",
    "PUDDING",
    "SEMISWEET",
    "SUGAR",
    "SWISS",
    "SYRUP",
    "TREAT",
    "TRUFFLES",
    "UNSWEETENED",
    "WHITE",
    ]
    
    for test_word in words:  # run the test cases for each word -- should all return true (all are in puzzle)
        print(word_search(puzzle, test_word))
        
        
    print('') # putting space between each set of test cases, for readability
    print('')
        
    ## Second Sample Set of Words    
    fake_words = [
    "BRUH",
    "HUH",
    "CHICKYCHUNK",
    "SILLY",
    "HEH??",
    ]

    
    for test_word_2 in fake_words: # these test cases are random words not found in puzzle -- should all return false
        print(word_search(puzzle, test_word_2))
        
    print('')
    print('')
    
    ## Test Case Sensitivity
    case_words = [
    "deCadENT",
    "drINKS",
    "ICE    creaM",
    ]
    
    for case_word in case_words: # words taken from original list --> should return TRUE
        print(word_search(puzzle, case_word))
    
    
test_ws() # call the test function
                 