# tf-idf
This allows lets you find the weight (or importance) of a word in a document in a series of documents.

I calculated the inverse document frequency part of the algorithm based off of 9 million wikipedia articles.
The Wikipedia XML dump file was first parsed by an open source Python script.
Then, I read in each article into my database and saved it to a new file.

How to use this?

Just change the url variable to the website you want in readDatabase.py file and run it. This scrapes that particular website's text using the Beautiful Soup Python library, and then calculates the term frequency part, and then multiplies it by the inverse document frequency (already calculated). The output is printed to the console as well as to the output.txt from least important to most important term.
