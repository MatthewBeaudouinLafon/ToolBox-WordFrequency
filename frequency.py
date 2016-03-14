""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
# coding=utf-8

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name, 'r')
	lines = f.readlines()
	start_line = 0
	end_line = 0

	while lines[start_line].find('LA PARURE') == -1:
		start_line += 1

	while lines[start_line + end_line].find('LE BONHEUR') == -1:
		end_line += 1

	lines = lines[start_line + 1:start_line + end_line]

	words = []

	for a_line in lines:
		line_words = a_line.split()
		for word in line_words:
			treated_word = word.lower()
			treated_word = treated_word.replace('\n', '').replace('\r', '')
			treated_word =  treated_word.strip(string.whitespace+string.punctuation)
			treated_word = treated_word.decode('utf8')
			words.append(treated_word)

	return words


def get_top_n_words(word_list, n, shortest_word_length):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

	freq = {}

	#print words[:20]
	#print words[3]

	# Get frequency of words
	for word in word_list:
		#print word
		freq[word] = freq.get(word, 0) + 1

	# Make into a list of freq-word tuples
	freq_list = []

	for word in freq:
		freq_list.append( (freq[word], word) )

	freq_list.sort(reverse = True)

	sorted_list = []

	for num, word in freq_list:
		if len(word)>shortest_word_length:
			sorted_list.append((word, num))

	return sorted_list[:n]
	
if __name__ == '__main__':
	file_name = 'pg14790.txt'
	words = get_word_list(file_name)
	freq = get_top_n_words(words, 100, 4) # Don't look at words with less than four chars

	for word in freq:
		print "'"+word[0]+"' appears", word[1], 'times.'
