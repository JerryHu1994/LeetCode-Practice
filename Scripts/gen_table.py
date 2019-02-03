'''
This module generates the README file contains the problem url landing
on Leetcode and my solutions.
'''

import collections
import os
import re
import json
import sys
import time

lang = {}

blacklist = [".DS_Store", "-DS_Store"]

def write_to_file(lines, filename):
	"Output the README content"
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line+'\n')
	print "Write {} lines to {}"

def get_finished_problems(base_path):
	"Returns a list of finished problems"
	finished_problems = []
	for f in os.listdir(base_path):
		if f in blacklist:	continue
		processed = f.replace(".", "").lstrip(" ").rstrip(" ")
		if not processed.isdigit():
			finished_problems.append((f, int(f.split("-")[0])))
	sorted_pairs = sorted(finished_problems, key = lambda x:[x[1]])
	return [p[0]	for p in sorted_pairs]

def read_json(filename):
	"Read the json data structure from file"
	with open(filename, "r") as f:
		data = json.load(f)
	return data

def write_file(lines, filename):
	"Write lines to file"
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")

def gen_table(sol_dir, lc_name, abs_path):
	"generate the table for display on RAEDME"
	finished_problems = get_finished_problems(sol_dir)
	lc_json = read_json(lc_name)
	outputs = ['| # | Problem | Accept Rate | Difficulty | Solutions |', '| --- | --- | --- | --- | --- |']
	easy_cnt, medium_cnt, hard_cnt = 0, 0, 0
	for problem in finished_problems:
		if problem in blacklist:	continue
		problem_idx = problem.split("-")[0].lstrip(" ").rstrip(" ")
		problem_title = lc_json[problem_idx]['title']
		problem_url = lc_json[problem_idx]['url']
		problem_difficulty = lc_json[problem_idx]['difficulty']
		problem_ac_rate = '{:.0f}%'.format(lc_json[problem_idx]['accept_rate'] * 100)
		problem_name = "[{}]({})".format(problem_title, problem_url)
		pre_path = sol_dir+problem
		solutions = os.listdir(pre_path)
		solution_with_link = []
		for sol_name in solutions:
			if os.stat(pre_path+"/"+sol_name).st_size == 0:	continue
			solution_with_link.append("[{}]({})".format(sol_name, abs_path+problem+"/"+sol_name))
		problem_sol_link = ' <br> '.join(solution_with_link)
		content = [problem_idx, problem_name, problem_ac_rate, problem_difficulty, problem_sol_link]
		outputs.append("|"+"|".join(content)+"|")
	return outputs

if __name__ == "__main__":
	# print get_finished_problems("../Solutions")
	contents = gen_table("../Solutions/", "lc.json", "Solutions/")
	write_file(contents, "README.md")