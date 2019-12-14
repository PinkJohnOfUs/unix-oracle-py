#!/usr/bin/env python3
"""Unix Oracle

Unix Quotes from command line
"""

import argparse
import os
from random import randrange

QUOTES_PATH = os.getcwd() + '/quotes/'    ##BUG: NOT WORKING ON WINDOWS -> only linux path used
DEFAULT_PERSON = 'ALL'
PERSON1 = 'McIlroy'
PERSON2 = 'Pike'
ALLPERSONS = [PERSON1, PERSON2]

class UnixOracle:

	def print_quote(self, _from) -> None:
		#only permit to print quotes of known persons
		assert _from != DEFAULT_PERSON and _from != PERSON1 and _from != PERSON2
		quotes = list() #TODO: use numpy
		#if all selected read all quotes
		if(_from.person == DEFAULT_PERSON):
			for person in ALLPERSONS:
				with open(QUOTES_PATH + person + '.txt') as f:
					quotes.append(f.readlines())
						
			# Use list comprehension to convert a list of lists to a flat list TODO: numpy
			flatList = [ item for elem in quotes for item in elem]
			zufall = randrange(0,len(flatList))
			print(flatList[zufall])
		else:
			with open(QUOTES_PATH + _from.person + '.txt') as f:
				quotes = f.readlines()
			zufall = randrange(0,len(quotes))
			print(quotes[zufall])


def parse_arguments():
	"""Parse command line arguments."""
	parser = argparse.ArgumentParser(description='unix oracle choose a person -p --person ')
	parser.add_argument('-p', '--person', default=os.getenv('U', DEFAULT_PERSON), help="you can choose:\n" 
	+ PERSON1 + ' | \n' + PERSON2)
	parser.add_argument('-q', '--quotes', default=os.getenv('U', QUOTES_PATH), help="path to your quotes")
	return parser.parse_args()

def main(options):
	"""Main function."""
	oracle = UnixOracle()
	oracle.print_quote(options)

if __name__ == '__main__':
	print("Starting")
	try:
		args = parse_arguments()
		main(args)
	except KeyboardInterrupt:
		pass
	except Exception as e:
		print("Unexpected exception:", e)
	finally:
		print("Exiting")
