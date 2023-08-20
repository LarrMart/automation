#!/usr/bin/env python

import random as r, csv

def create_vector(dimension, max_value):
	ret = []
	allowed_values = max_value
	for i in range(dimension):
		ret.append(r.randint(0, allowed_values))

	return ret

def create_n_vectors(n, dim, max_value):
	ret = [["x", "y", "z"]]
	for i in range(n):
		ret.append(create_vector(dim, max_value))

	return ret

def create_csv_file_for_vectors(n, dim, max_value):
	vectors = create_n_vectors(n, dim, max_value)
	with open("./s2/vectors.csv", "w", newline = "") as file :
		writer = csv.writer(file, delimiter = ",")
		writer.writerows(vectors)

create_csv_file_for_vectors(30, 3, 3)
