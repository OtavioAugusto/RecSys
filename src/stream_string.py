
from collections import defaultdict

class StreamFromString(object):
	def __init__(self, string_content):
		self.string_content = string_content
		self.flag_handler   = 0
		self.line_str       = None
		self.current_line   = 0
		self.clean_dicts()

	def clean_dicts(self):
		self.user_features  = defaultdict()
		self.items_features = defaultdict(lambda: defaultdict())

	def __iter__(self):
		self.handler        = self.string_content.split('\n')
		self.string_content = None
		return self

	def name(self):
		return 'Stream From STRING'

	def next(self):
		if self.flag_handler == 0:
			self.flag_handler = 1
			self.__iter__()

		if self.current_line < len(self.handler):
			self.line_str     = self.handler[self.current_line]
			self.current_line += 1

			tokens = self.line_str.split('|')

			# timestamp, displayed article id, and user click
			part1  = tokens[0].split()

			# clean dicts for next event
			self.clean_dicts()

			# user_features
			part2  = tokens[1]
			for a, b in [(i.split(':')[0], i.split(':')[1]) for i in part2.split()[1:]]:
				self.user_features[a] = b

			# articles features
			part3  = tokens[2:]
			for item in part3:
				tmp_features = [(i.split(':')[0], i.split(':')[1]) for i in item.split()[1:]]
				if len(tmp_features) == 6:
					for a, b in tmp_features:
						self.items_features[item.split()[0]][a] = b

			event = {
	    				'timestamp'         : part1[0],
	            'displayed_item_id' : part1[1],
	            'user_click'        : part1[2],
	            'user_features'			: self.user_features,
	            'items_features'    : self.items_features,
	    }

			return event

		return None

	def get_line(self):
		return self.line_str
