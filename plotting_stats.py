"""
Plots book length vs unique words for books in 4 different languages.
"""
import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo")

plt.figure(figsize = (10, 10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plt.pdf")
