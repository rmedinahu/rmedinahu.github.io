# software_db.py

import itertools
import random

# quiz schema: (name)
# question schema: (quiz, question, order)
# relation (app, file)
quizzes = ['A', 'B', 'C', 'D']
questions = [('A', 'fav food?', 3), ('A', 'fav hobby?', 1), ('A', 'fav color?', 0), ('A', 'fav movie?', 2)]

print '\n**SELECT** (single table with predicate)'
for i in questions:
	if i[1] == 'fav food?':
		print i

print '\n**PROJECT** (select \'question\': single table select and projection over n attributes with predicate)'
for i in questions:
	if i[0] == 'A':
		print i[1] # selecting specific attribute (question)

print '\n**BINARY PRODUCT** (all columns of a table A with all columns of a table B'
prod = list(itertools.product(quizzes, questions))
for i in prod:
	print (i[0], i[1][0], i[1][1], i[1][2])

print '\n**THETA JOIN** (product of A,B then select)'
for i in prod:
	if i[1][1] == 'fav color?':
		print i

print '\n**EQUIJOIN** (product of A,B where col i of A == col j of B)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i

print '\n**NATURAL JOIN** (EQUIJOIN but drop repeated columns)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i[1][1], i[1][2]

print '\n**LEFT JOIN** (NATURAL JOIN BUT PROJECT ONLY ATTRIBUTES OF A)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i[0]

print '\n**RIGHT JOIN** (NATURAL JOIN BUT PROJECT ONLY ATTRIBUTES OF B)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i[1]

print '\n**LEFT OUTER JOIN** (NATURAL JOIN but add null matches B)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i[1][1], i[1][2]
	else:
		print i[0], None

print '\n**RIGHT OUTER JOIN** (NATURAL JOIN but add null matches for A)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i[1][1], i[1][2]
	else:
		print None, i[1]

print '\n**FULL OUTER JOIN** (NATURAL JOIN but add null matches for A and B)'
for i in prod:
	if i[0] == i[1][0]:  # col 1 of A must match col 1 of B
		print i[1][1], i[1][2]
	else:
		print None, None

