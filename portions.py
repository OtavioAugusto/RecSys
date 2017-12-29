
from os import listdir
from os.path import isfile, join
import numpy as np
import collections

class BootstrappedSample(object):
	def __init__(self, bootstrapped_sample_dir, num_samples):
		self.bootstrapped_sample_dir = bootstrapped_sample_dir
		self.num_samples             = num_samples
		self.current_stream          = None
		self.current_portion_idx     = 0
		self.current_bootstrap_idx   = 0
		self.current_indexes         = collections.defaultdict()
		self.portion_content         = collections.defaultdict()

		self.num_events_subsampled = None

		self.portion_files = [f for f in listdir(self.bootstrapped_sample_dir) if isfile(join(self.bootstrapped_sample_dir, f))]

	def load_current_portion(self):
		# load to memory and return stream with self.current_bootstrap_idx = 0
		if self.current_bootstrap_idx  != 0:
			return

		self.current_indexes = collections.defaultdict(lambda: None)

		portion_file_name = join(self.bootstrapped_sample_dir, self.portion_files[self.current_portion_idx])
		sample_idx_file_name = join(self.bootstrapped_sample_dir + '/idx/', self.portion_files[self.current_portion_idx] + '.idx')

		fp_sample_idx = open(sample_idx_file_name, 'r')
		print('    openning file [%s]' % (sample_idx_file_name))
		num_samples, self.num_events_subsampled, num_items, num_events = fp_sample_idx.readline().strip().split()
		i = 0
		for line in fp_sample_idx:
			self.current_indexes[i] = np.array([int(j) for j in line.strip().split()])
			i               += 1
		fp_sample_idx.close()
		
		fp_portion = open(portion_file_name, 'r')
		i = 0
		for line in fp_portion:
			self.portion_content[i] = line.strip()
			i                       += 1
		fp_portion.close()

	def assign_current_stream(self):
		tmp_idxs = self.current_indexes[self.current_bootstrap_idx]
		self.current_stream = '\n'.join([self.portion_content[i] for i in tmp_idxs])

	def next(self):
		if self.current_bootstrap_idx == self.num_samples:
			self.current_portion_idx   += 1
			self.current_bootstrap_idx = 0

		if self.current_portion_idx < len(self.portion_files):

			self.load_current_portion()

			self.assign_current_stream()
			self.current_bootstrap_idx += 1

			return [self.current_portion_idx, self.current_bootstrap_idx, self.current_stream, self.num_events_subsampled]

		else:

			return None
