"""string and string methords in python

what is strings?
 A string is a sequence of characters enclosed in single quotes('')
and double quotes("")

Multiline strings we can use triple quotes('''or""

STRING INDEXING AND SLICING 
What is a String?

A string is a collection (sequence) of characters enclosed inside single quotes (' ') or double quotes (" ").

A string can contain:

Letters
Numbers
Symbols
Spaces
Example
name = "Python"

Here,

Python is a string.
It contains 6 characters.

Characters are:

P  y  t  h  o  n
What is an Index?

Imagine every character in a string has its own house number.

That house number is called an index.

Python uses these numbers to find characters.

Important Rule:

 Python starts counting from 0, not from 1.

For the string:

text = "Python"

The indexes are:

Character :   P   y   t   h   o   n
Index     :   0   1   2   3   4   5

Think of it like this:

      0   1   2   3   4   5
      ↓   ↓   ↓   ↓   ↓   ↓
      P   y   t   h   o   n
Why Does Python Start from 0?

Most programming languages use 0-based indexing because it makes memory calculations easier and faster.

As a beginner, simply remember:

First character = Index 0

String Indexing
Definition

String indexing means accessing one character from a string using its index number.

Syntax
string_name[index]

General form:

text[index]
Example
text = "Python"
Access the first character
print(text[0])

Output

P

Python looks at index 0 and returns P.

Access the second character
print(text[1])

Output

y
Access the third character
print(text[2])

Output

t
Access the fourth character
print(text[3])

Output

h
Access the fifth character
print(text[4])

Output

o
Access the sixth character
print(text[5])

Output

n
Complete Example
text = "Python"

print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

Output

P
y
t
h
o
n
What Happens if the Index Does Not Exist?

Example

text = "Python"

print(text[6])

Output

IndexError: string index out of range
Why?

The string has only 6 characters.

Valid indexes are:

0 1 2 3 4 5

There is no index 6.

String Slicing

Sometimes we don't want only one character.

We want multiple characters together.

This is called String Slicing.

Definition

String slicing means extracting a portion (part) of a string.

Syntax
string[start:stop]

or

text[start:stop]
Meaning
start → Where to begin.
stop → Where to stop.

Important Rule

The start index is included.

The stop index is excluded (not included).

Example
text = "Python"

Indexes

Character :   P   y   t   h   o   n
Index     :   0   1   2   3   4   5
Example 1
print(text[0:3])

Python starts from index 0.

Stops before index 3.

0 → P ✔
1 → y ✔
2 → t ✔
3 → h ✘

Output

Pyt
Example 2
print(text[2:6])
2 → t ✔
3 → h ✔
4 → o ✔
5 → n ✔

Output

thon
Example 3
print(text[1:4])
1 → y ✔
2 → t ✔
3 → h ✔

Output

yth
Omitting the Start Index

If the start is not written,

Python automatically starts from 0.

Example

print(text[:4])

Equivalent to

print(text[0:4])

Output

Pyth
Omitting the Stop Index

If the stop is not written,

Python continues until the end of the string.

Example

print(text[2:])

Output

thon
Copying the Entire String
print(text[:])

Output

Python

This copies the complete string.

Visual Explanation
text = "Python"

Index

0   1   2   3   4   5
↓   ↓   ↓   ↓   ↓   ↓
P   y   t   h   o   n

Example:

text[1:5]
0   1   2   3   4   5
    |-----------|
    y   t   h   o

Output

ytho
Important Rules
Rule 1

Indexing starts from 0.

Rule 2

Indexing returns only one character.

Example

text[4]

Output

o
Rule 3

Slicing returns multiple characters.

Example

text[2:5]

Output

tho
Rule 4

The start index is included.

Rule 5

The stop index is excluded.

Rule 6

Leaving the start empty means start from the beginning.

text[:3]

Output

Pyt
Rule 7

Leaving the stop empty means go until the end.

text[3:]

Output

hon
Difference Between Indexing and Slicing
String Indexing	String Slicing
Returns one character	Returns multiple characters
Uses one index	Uses start and stop indexes
Syntax: text[index]	Syntax: text[start:stop]
Example: text[0] → P	Example: text[0:3] → Pyt
Practice Questions

Assume:

text = "Programming"

Find the output of the following:

text[0]
text[5]
text[3:7]
text[:6]
text[4:]
text[:]

"""

