#A computer-readable English Dictionary, from scratch

We're going to us a Predictable Information Elimination (PIE) algorithm to create a perfectly computer readable document from the raw text of the Webster's Unabridged Dictionary.

##PIE Aligorthms

###Source
The Websters dictionary can be found on [Project Gutenberg](http://www.gutenberg.org/files/29765/29765-8.txt), and is included in this repo in the texts/ directory.

Project Gutenberg requests that one [http://www.gutenberg.org/error403.php](not crawl) the site, so please be respectful and download it manually if you want it directly from the source.

###Concept


###Step 1: Define information


PIE algorithms work by iteratively identifying 

begins by defining "predictable information," data in predictable formats that can
be blocked off to narrow the search for unpredictable information. In this case, this involved notations for 
the word, the definition, etymology, parts of speech, etc.

For text documents, regular expressions are an obvious way to create these definitions. But PIE algorithms
are not limited to text, and theoretically work for any set of information for with is it possible to 
define patterns and search for matches: An image, a piece of music, and so forth.

This is accomplished iteratively. 