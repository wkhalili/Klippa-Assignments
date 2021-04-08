import pandas
import pickle


'''
invoice_lines.pkl is a pickled Pandas dataframe containing over 150k lines that have been annotated from invoices.
Every row in the dataframe has two attributes: text (the full text of the line) and labels (1 indicates a line-item and 0 is used for everything else.)
The task is to create a Bag of Words algorithm using sklearn that is able to classify these lines.
The first step will be splitting the dataframe in two sets: one for training and one for testing.
Your classification algorithm should print out the metrics (precision/recall/accuracy) on how it performs on the test set.
'''

with open('invoice_lines.pkl', 'rb') as f:
	file = open('important', 'wb')
	df = pickle.load(f)
	for index, row in df.iterrows():
		# You now have access to row['text'] and row['labels']
		pass
