def read_book(title_path):
	""" 
	Read a book and return it as a string.
	"""

	with open(title_path, "r", encoding = "utf8") as current_file:
		text = current_file.read()
		text.replace("\n", ""), replace("\r", "")
	return text

ind = text.find("What's in a name?")

sample_text = text[ind : ind + 1000]

def word_stats(word_counts):
	"""
	Return number of uniqye words and word frequencies.
	"""

	num_unique = len(word_counts)
	counts = word_counts.values()
	return (num_unique, counts)

"""Word Frequency statistics: Romeo and Juliet English vs German"""

text = read_book("./Books/English/shakespeare/Romeo and Juliet")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print (num_unique, sum(counts))

text = read_book("./Books/German/shakespeare/Romeo und Julia")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print (num_unique, sum(counts))
