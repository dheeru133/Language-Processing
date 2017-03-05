"""
Reading text from books stored in multiple directories and storing data into a Pandas Dataframe.
"""
import os
book_dir = "./Books"

import pandas as pd
stats = pd.DataFrame(columns = ("lnguage", "athor", "ttle", "lngth", "unique"))
title_num = 1

for language in os.listdir(book_dir):
	for author in os.listdir(book_dir + "/" + language):
		for title in os.listdir(book_dir + "/" + language + "/" + author):
			inputfile = book_dir + "/" + language + "/" + author + "/" + title
			print(inputfile)
			(num_unique, counts) = word_stats(count_words(text))
			stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
			title_num += 1
