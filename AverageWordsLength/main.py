'''
Task:
Takes in a string, figure out the average length of all the words and return a number representing the average length. 
Remove all punctuation. Round up to the nearest whole number.

Input Format:
A string containing multiple words.

Output Format:
A number representing the average length of each word, rounded up to the nearest whole number.

Sample Input:
this phrase has multiple words
Sample Output:
6

'''

def AverageWordsLenght(sentence):
    words = sentence.split(' ')
    lenghts = []
    avgWordLength = 0
    
    i = 0
    for i in range(len(words)):
        lenghts.append(len(words[i]))  #all lenghts of all words

    suma = 0
    a = 0
    for a in range(len(lenghts)):
        suma += lenghts[a]    
    
    avgn = (suma/len(lenghts)) #avg lenght of all words
    avgn = int(avgn)
    print(avgn)



#output = 6
Sentence1 = 'this phrase has multiple words'
Sentence2 = "Hi all, my name is Tom...I am originally from Australia."
AverageWordsLenght(Sentence2)