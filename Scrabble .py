
# coding: utf-8

# In[1]:


import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = r'C:\Users\tejasv09\Downloads\words.txt'



# In[2]:


def loadWords():
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList



# In[3]:


def getFrequencyDict(sequence):
   
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# In[4]:


def getWordScore(word, n):
   
    if word == '':
        return 0
    score = 0
    for w in word:
        score += SCRABBLE_LETTER_VALUES[w]
    score *= len(word)
    if len(word) == n:
        score += 50
    return score
    
    


# In[5]:


def displayHand(hand):
    
   
    for letter in hand.keys():
        for j in range(hand[letter]):
             print (letter),              # print all on the same line
    print                               # print an empty line


# In[6]:


def dealHand(n):

   
   hand={}
   numVowels = int(n / 3)
   
   for i in range(numVowels):
       x = VOWELS[random.randrange(0,len(VOWELS))]
       hand[x] = hand.get(x, 0) + 1
       
   for i in range(numVowels, n):    
       x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
       hand[x] = hand.get(x, 0) + 1
       
   return hand


# In[7]:


def updateHand(hand, word):
  
    hand_copy=dict(hand)
    for ch in word:
        hand_copy[ch]=hand_copy.get(ch,0)-1
        if(hand_copy.get(ch,0)==0):
            del hand_copy[ch]
    return hand_copy


# In[8]:


def isValidWord(word, hand, wordList):
   
    if word not in wordList:
        return False
    hand = hand.copy()
    for letter in word:
        if not hand.get(letter, 0):
            return False
        else:
            hand[letter] = hand.get(letter, 0) - 1
    return True

#
# Problem #4: Playing a hand
#



# In[9]:


def calculateHandlen(hand):
   
    count=0
    for ch in hand:
        if(hand.get(ch,0)>0):
            count+=1
    return count
    


# In[10]:


def playHand(hand, wordList, n):
        totalScore = 0
        output = "Run out of letters."
        while calculateHandlen(hand) > 0:
            displayHand(hand)
            word = raw_input('Enter word, or a "." to indicate that you are finished: ').lower()
            if word == '.':
                output = "Goodbye!"
                break
            else:
                if not isValidWord(word, hand, wordList):
                    print("Invalid word, please try again.")
                else:
                    score = getWordScore(word, n)
                    totalScore += score
                    print('"{0:s}" earned {1:d} points. Total: {2:d} points.'.format(word, score, totalScore))
                    hand = updateHand(hand, word)
        print('{0:s} Total score: {1:d} points.'.format(output, totalScore))
    
 



# In[11]:


def compChooseWord(hand, wordList, n):

    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word

    # return the best word you found.
    return best_word


# In[12]:


def compPlayHand(hand, wordList, n):
   
    total_score = 0
    score = 0
    while(calculateHandlen(hand) != 0):
        print 'Current Hand: ',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if(word != None):
            score = getWordScore(word, n)
            total_score += score
            print('"'+word+'"'+' earned '+str(score)+' points. Total: '+str(total_score)+' points')
            print
            hand = updateHand(hand, word)      
        else:
            break
    print('Total score: '+str(total_score))


# In[ ]:


def playGame(wordList):

    hand_choice = ''
    hand = ''
    while True:
        hand_choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if hand_choice == 'e':
            break
        elif hand_choice != 'n' and hand_choice != 'r':
            print "Invalid command."
            continue
        if hand_choice == 'n':
            hand = dealHand(HAND_SIZE)
        elif hand_choice == 'r':
            if hand == '': 
                print "You have not played a hand yet. Please play a new hand first!"+'\n'
                continue
        while True:
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')
            if player != 'u' and player != 'c':
                print "Invalid command."
                continue
            if player == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif player == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
            break
        

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    

