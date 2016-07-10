from enum import Enum


class Value(Enum):
	zero = 0
	one = 1
	two = 2
	three = 3

	@staticmethod
	def get_instance(integer):
		if not isinstance(integer, int):
			raise TypeError("Expected an integer!")
		if not (0 <= integer <= 3):
			raise ValueError("Values have to be between 0 and 3!")
		# We can return an appropriate object
		if integer == 0:
			return Value.zero
		elif integer == 1:
			return Value.one
		elif integer == 2:
			return Value.two
		elif integer == 3:
			return Value.three


def value_enum_or_error(value):
	if isinstance(value, Value):
		return value
	else:
		return Value.get_instance(value)


class Mapping(object):

	def __init__(self, a_val, t_val, c_val, g_val):
		self.a = value_enum_or_error(a_val)
		self.t = value_enum_or_error(t_val)
		self.c = value_enum_or_error(c_val)
		self.g = value_enum_or_error(g_val)
		self._mapping = ((self.a, 'A'), (self.t, 'T'), (self.c, 'C'),
						(self.g, 'G'))
		self._check_distinct()

	def _check_distinct(self):
		for current_value in self._mapping:
			counter = 0
			for next_value in self._mapping:
				if next_value[0] == current_value[0]:
					counter += 1
			if counter > 1:
				raise ValueError("Values must be distinct!")

	def get_nucleotide_by_value(self, value):
		for ValueEntry, nucleotide in self._mapping:
			if ValueEntry.value == value:
				return nucleotide

	def get_value_by_nucleotide(self, nucleotide):
		current_nucleotide = nucleotide[0].upper()
		for ValueEntry, nucleotide in self._mapping:
			if nucleotide == current_nucleotide:
				return ValueEntry.value



DEFAULT_MAPPING = Mapping(Value.zero, Value.three, Value.one, Value.two)
