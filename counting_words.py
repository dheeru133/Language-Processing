
text = "This is my string of test text. Let us keep this text short for simplicity. "

def count_words(text):
	'''Counts the number of times each word occurs in a text (str). Returns a dictionary where keys are unique words and values are word counts. Skips punctuation.'''
	word_counts = {}
	text = text.lower()
	skips = [".", ",", ":", ";", "'", '"']
	for ch in skips:
		text = text.replace(ch, "")
	for word in text.split(" "):
		if word in word_counts:
			word_couts[word] += 1
		else:
			word_counts[word] = 1
	return word_counts

	from collections import Counter
	def count_words_fast(text):
	'''Counts the number of times each word occurs in a text (str). Returns a dictionary where keys are unique words and values are word counts. Skips punctuation.'''
	word_counts = {}
	text = text.lower()
	skips = [".", ",", ":", ";", "'", '"']
	for ch in skips:
		text = text.replace(ch, "")
	wourd_counts = Counter(text.split(" "))
	return word_counts