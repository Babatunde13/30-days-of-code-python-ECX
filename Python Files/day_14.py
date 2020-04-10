def checkAnagram(word1,word2):
    """
          Takes two words and returns True if both words are anagrams of each other.

          Parameters:
          word1 (string): The first word to be checked
          word2 (string): The second word to be checked

          Returns:
          Bool: Returns True if both inputs are anagrams of each other and False if they are not anagrams or if an invalid input is entered

    """
    if isinstance(word1,str) and isinstance(word2,str):
      word1= word1.upper().replace(' ','')
      word2 = word2.upper().replace(' ','')
      count = 0
      for letter1 in word1:
          for letter2 in word2:
                  if letter1 == letter2:
                      count+=1
                      break
      if count == len(word1) and count == len(word2):
          return True
      return False
    else:
      return False

def anagram_finder(wordList):
    """
          Takes a list of words and returns another list containing sublists that contain 2 strings from the original list that are anagrams of each other.

          Parameters:
          wordList (list): The list of words from which                    the anagrams would be gotten

          Returns:
          list: Returns a list containing sublists which        contain anagrams and returns an empty           list for invalid input

    """
    if isinstance(wordList,list):
      firstWordCount = 0
      final = []
      for firstWord in wordList:
          secondWordCount = 0
          for secondWord in wordList:
              if firstWordCount != secondWordCount:
                  if checkAnagram(firstWord,secondWord):
                      final.append([firstWord, secondWord])
                      wordList.remove(secondWord)
              secondWordCount+=1
          firstWordCount+=1
      return final
    else:
      print('You entered an invalid input!!!')
      return []



