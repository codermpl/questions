# Questions

Serve a webpage to display questions.

Features:
1. Reads questions from a csv file
2. Endpoint for getting questions at /rest/question
3. Pagination that gets each page from the server.
4. Server side sorting of the question and answer columns.  Sorting of distractors is not enabled.

Bugs: 
1. Server can only sort one column at a time even though UI allows selecting multiple columns for sorting using control or shift.  The first column selected will be used to sort.
