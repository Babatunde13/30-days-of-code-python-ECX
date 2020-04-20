def find_edit_dist(str1: str, str2: str) -> int:
  '''
  A function that returns the edit distance between two words
  
  Parameters: ---------------
    str1: string
    		The first word
    str2: string
    		The second string
	
  Returns : -------------------
     edit_distance: integer. 
     		The distance between str1 and str2

  @author: Babatunde Koiki
  Created on: 18-04-2020
  '''
  if str1 == "":
      return len(str2)
  if str2 == "":
      return len(str1)
  if str1[-1] == str2[-1]:
      dist = 0
  else:
      dist = 1
  edit_distance = min([find_edit_dist(str1[:-1], str2)+1,
             find_edit_dist(str1, str2[:-1])+1, 
             find_edit_dist(str1[:-1], str2[:-1]) + dist])

  return edit_distance

print(find_edit_dist('goat', 'float'))
