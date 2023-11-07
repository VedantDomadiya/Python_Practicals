# -*- coding: utf-8 -*-
"""Numpy.ipynb
 https://colab.research.google.com/drive/1USkoxduWvPnoKjwgAeWiKPwR-gyE8-V2?usp=sharing
"""

1. Create a 2D Numpy Array of the given values: a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
2. Convert list to Numpy Array
3. Show the numpy array dimensions
4. Show the numpy array shape
5. Show the numpy array size
6. Access the element on the second row and third column
7. Access the element on the first row and first column
8. Access the element on the first row and first and second columns
9. Access the element on the first and second rows and third column
10. Create a numpy array X=[[1 0],[0,1]] and array Y= [[2,1][1,2]]
11. Add X and Y
12. Multiply Y with 2
13. Multiply X with Y
14. Create a matrix A=[[0, 1, 1], [1, 0, 1]] and B = [[1, 1], [1, 1], [-1, 1]]
15. Calculate the dot product
16. Calculate the sine of Z
17. Create a matrix C= [[1,1],[2,2],[3,3]]
18. Get the transposed of C
19. Use arange to create a variable named foo that stores an array of numbers from 0 to 29,
inclusive. Print foo and its shape.
20. Use the reshape function to change foo to a validly-shaped two-dimensional matrix and store
it in a new variable called bar. Print bar and its shape.
21. Create a third variable, baz that reshapes it into a valid three-dimensional shape. Print baz
and its shape.
22. There are several different ways to index into NumPy arrays. Use two-dimensional array
indexing to set the first value in the second row of bar to -1. Now look at foo and baz. Did they
change? Explain what’s going on. (Hint: does reshape return a view or a copy?)
23. Another thing that comes up a lot with array shapes is thinking about how to aggregate over
specific dimensions. Figure out how the NumPy sum function works (and the axis argument in
particular) and do the following:
24. (i) Sum baz over its second dimension and print the result.
25. (ii) Sum baz over its third dimension and print the result.
26. (iii) Sum baz over both its first and third dimensions and print the result.
27. Along with shaping and indexing, we also do a lot of slicing which is where you index with
ranges to get subvectors and sometimes submatrices. Write code to do the following:
28. (i) Slice out the second row of bar and print it.
29. (ii) Slice out the last column of bar using the -1 notation and print it.
30. (iii) Slice out the top right 2 × 2 submatrix of the bar and print it.
