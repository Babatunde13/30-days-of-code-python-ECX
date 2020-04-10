def anagram_finder(list_words):
	'''This function recieves a liat of words and returns a list of sublists of all anagrams'''
	ans_list = []
	dict = {}
	for i in list_words:
		f = ''.join(sorted(i))
		if f in dict:
			dict[f].append(i)
		else:
			dict[f] = [i]
	for v in dict.values():
		ans_list.append(v)
	return ans_list
list_words = ['cat','act','get','etg','tac','egt','dat','tad']	
print(anagram_finder(list_words))
