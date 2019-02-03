'''
This module contains the a crawler that extracts the leetcode problem info.
'''

# standard library
import collections
import json
import re
import string
import time
import requests

client = requests.session()

difficulties = {1 : 'Easy', 2 : 'Medium', 3 : 'Hard'}

def crawl_problems():
	'''Crawl leetcode algorithm problems information and stores them inside s dictionary'''
	algo_urls = "https://leetcode.com/api/problems/algorithms/"
	response = client.get(algo_urls)
	algo_data = response.json()
	algo_data = algo_data['stat_status_pairs']
	
	gen_link = lambda title : "https://leetcode.com/problems/"+"-".join(title.split()).lower()

	# maintains index to problem hash mapping
	problems = collections.defaultdict(dict)
	for prob in algo_data:
		stat = prob['stat']
		index = int(stat['frontend_question_id'])
		problems[index]['title'] = stat['question__title']
		problems[index]['total_acs'] = stat['total_acs']
		problems[index]['total_submitted'] = stat['total_submitted']
		problems[index]['accept_rate'] = float(problems[index]['total_acs'])/float(problems[index]['total_submitted'])
		problems[index]['difficulty'] = difficulties[int(prob['difficulty']['level'])]
		problems[index]['url'] = gen_link(problems[index]['title'])
	return problems

def dump_json(data, json_file):
	'''Dump data to a json file'''
	with open(json_file, 'w') as f:
		json.dump(data, f)

if __name__ == "__main__":
	prob_json = crawl_problems()
	dump_json(prob_json, 'lc.json')

