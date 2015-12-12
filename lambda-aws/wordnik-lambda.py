import json
from wordnik import *


print 'Loading function'

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

	apiUrl = 'http://api.wordnik.com/v4'
	apiKey = '18a5df78c3471888dc34c16b56e34e9d4dab4322fe6f0f325'
	client = swagger.ApiClient(apiKey, apiUrl)
	client = swagger.ApiClient(apiKey, apiUrl)
	wordApi = WordApi.WordsApi(client)

	i=1

	for x in input_word:
		
		# print i
		# print x
		if x == 'x':
			sounds_like = 'xylophone'
		else:
			apiUrl = 'http://api.wordnik.com/v4'
			apiKey = '18a5df78c3471888dc34c16b56e34e9d4dab4322fe6f0f325'
			
			searchResults = wordApi.searchWords('badger',
			                                     minCorpusCount='30000',
			                                     minLength='wiktionary',
			                                     maxLength=9,
			                                     )
			print searchResults[0].text
