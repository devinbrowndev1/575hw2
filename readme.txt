
Q1
-re-requesting information if the user does not answer appropriately.
-support any combination of the pieces of information you must collect. 


TO IMPLEMENT:
Q1-Q4
-options for whitespace before text
-add more grounding
-cancel --> I implemented a basic cancel option but we could get better
-repeat
-start-over --> I implemented the base of this but needs work--> I added a misunderstood_pizza state which is diff than misunderstood_order, so we can implement startover on pizza_x and also on order_x
-ordering a single specialty pizza (need to make this dynamic/add all possible specialty pizzas to FST),
-reordering the preferred order --> need to somehow store a preffered order, maybe make a db with key being name+phone
-querying for order status --> need to implement an orderid thing that returns order status given an orderid
-provide information out-of-turn or out-of-order
-revise previous information --> this should interact with the misunderstood_pizza and misunderstood_order
-reject previously-provided information --> this should interact with the misunderstood_pizza and misunderstood_order

Q5-
edit topings, order multiple pizzas
-edit distance to catch common typos (haiwaiian vs hawaiian)
	nltk.edit_distance(mistake, word)
