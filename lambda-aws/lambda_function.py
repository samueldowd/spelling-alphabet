import json
import random
import requests
from json import JSONEncoder

print 'Loading function' 

# def test(event):
# 	print event
# 	input_word = list(event)
# 	print input_word
# 	print len(input_word)

# 	for x in input_word:
# 		if x == 'x':
# 			sounds_like = 'xylophone'
# 		else:
# 			req_url = "http://api.wordnik.com:80/v4/words.json/search/" + x
# 			print req_url
# 			payload = {'minCorpusCount': '30000', 'minLength': 4, 'maxLength': 9, 'limit': 10, 'api_key': '18a5df78c3471888dc34c16b56e34e9d4dab4322fe6f0f325'}
# 			r = requests.get(req_url, params=payload)
# 			print r.status_code
# 			print r.url
# 			print r.text
# 			response_json = r.json()
# 			print response_json
# 			response_dict = dict(response_json)
# 			result_count = response_dict['totalResults']
# 			print result_count
# 			rand_max = len(response_dict['searchResults']) - 1
# 			rand_int = random.randint(2, rand_max)
# 			print rand_int
# 			print x
# 			sounds_like = response_dict['searchResults'][rand_int]['word']
			
# 			print sounds_like

# 		result = [x, sounds_like]
# 		radiotelephony_result.append(result)
# 		print radiotelephony_result
# 	radiotelephony_dict = dict(radiotelephony_result)
# 	ui_return = json.dumps(radiotelephony_dict, indent=4, separators=(',', ': '))
# 	print ui_return
# 	for i in radiotelephony_result:
# 		print i[0] + " as in " + i[1]
# 	return ui_return




def lambda_handler(event, context):
	print type(event)
	print event
	event_str = str(event)
	print str(event)
	print type(event_str)

	input_word = list(event_str)
	# print input_word
	# print len(input_word)
	radiotelephony_result = []
	i=1

	for x in input_word:
		
		# print i
		# print x
		if x == 'x':
			sounds_like = 'xylophone'
		else:
			req_url = "http://api.wordnik.com:80/v4/words.json/search/" + x
			# print req_url
			payload = {'minCorpusCount': '30000', 'minLength': 4, 'maxLength': 9, 'limit': 10, 'api_key': '18a5df78c3471888dc34c16b56e34e9d4dab4322fe6f0f325'}
			r = requests.get(req_url, params=payload)
			# print r.status_code
			# print r.url
			# print r.text
			response_json = r.json()
			# print response_json
			response_dict = dict(response_json)
			result_count = response_dict['totalResults']
			# print result_count
			rand_max = len(response_dict['searchResults']) - 1
			rand_int = random.randint(2, rand_max)
			# print rand_int
			# print x
			sounds_like = response_dict['searchResults'][rand_int]['word']
			
			# print sounds_like

		result = [str(x), str(sounds_like)]
		radiotelephony_result.append([i, result])
		# print radiotelephony_result
		i+=1
	radiotelephony_dict = dict(radiotelephony_result)
	print radiotelephony_dict
	rdt_json = JSONEncoder().encode(radiotelephony_dict)
	print rdt_json
	ui_return = json.dumps(radiotelephony_dict, sort_keys=True, indent=4, separators=(',', ': '))
	# for i in radiotelephony_result:
		# print i[0] + " as in " + i[1]
	# print ui_return
	return rdt_json
	