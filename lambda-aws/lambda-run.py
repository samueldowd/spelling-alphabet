from wordnik_lambda import lambda_handler

# print test(sys.argv[1])

input = "ttttt"
context = {'env': 'local'}
print lambda_handler(input, context)