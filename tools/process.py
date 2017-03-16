#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataIO import textfile
from pathlib_mate import Path
from sfm import lines_count
import pandas as pd

def process_rare_prefix():
	nlines = lines_count.count_lines("rare-prefix.txt") * 1.0
	prefix_list = list(textfile.readlines("rare-prefix.txt"))

	df = list()
	for i, prefix in enumerate(prefix_list):
		i += 1
		percentage = "%.2f%%" % (i / nlines * 100,)
		row = [prefix, i, percentage]
		df.append(row)
	df = pd.DataFrame(df, columns=["prefix", "index", "percentage"])
	df.to_csv("rare-prefix-table.txt", index=False)

process_rare_prefix()

def process_rare_surfix():
	nlines = lines_count.count_lines("rare-surfix.txt") * 1.0
	surfix_list = list(textfile.readlines("rare-surfix.txt"))

	df = list()
	for i, surfix in enumerate(surfix_list):
		i += 1
		percentage = "%.2f%%" % (i / nlines * 100,)
		row = [surfix, i, percentage]
		df.append(row)
	df = pd.DataFrame(df, columns=["surfix", "index", "percentage"])
	df.to_csv("rare-surfix-table.txt", index=False)

process_rare_surfix()