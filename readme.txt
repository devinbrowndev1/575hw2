
Q1
-re-requesting information if the user does not answer appropriately.

-only exact match phrases need be supported. 

-cover the sample dialogs shown in DATA0.txt
-support any combination of the pieces of information you must collect. 



You should implement the NLG component as well; system responses should be natural language sentences. Perform appropriate grounding of the information using the small DB shown above.



TO IMPLEMENT:
-edit distance to catch common typos (haiwaiian vs hawaiian)
	nltk.edit_distance(mistake, word)
