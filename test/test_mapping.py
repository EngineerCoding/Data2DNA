from unittest import TestCase

from mapping import Mapping
from mapping import Value


class MappingTestCase(TestCase):

	def setUp(self):
		self.mapping =  Mapping(Value.zero, Value.one, Value.two, Value.three)

	def test_distinct_values_correct(self):
		try:
			Mapping(Value.zero, Value.one, Value.two, Value.three)
		except ValueError:
			self.fail()

	def test_distinct_value_incorrect(self):
		self.assertRaises(ValueError, Mapping, Value.zero, Value.one,
						  Value.zero, Value.two)

	def test_get_nucleotide_by_value(self):
		self.assertEqual('A', self.mapping.get_nucleotide_by_value(0))
		self.assertEqual('T', self.mapping.get_nucleotide_by_value(1))
		self.assertEqual('C', self.mapping.get_nucleotide_by_value(2))
		self.assertEqual('G', self.mapping.get_nucleotide_by_value(3))

	def get_value_by_nucleotide_case(self, upper=True):
		dna = 'ATCG'
		if upper:
			dna = dna.upper()
		else:
			dna = dna.lower()
		self.assertEqual(0, self.mapping.get_value_by_nucleotide(dna[0]))
		self.assertEqual(1, self.mapping.get_value_by_nucleotide(dna[1]))
		self.assertEqual(2, self.mapping.get_value_by_nucleotide(dna[2]))
		self.assertEqual(3, self.mapping.get_value_by_nucleotide(dna[3]))

	def test_get_value_by_nucleotide_case_lower(self):
		self.get_value_by_nucleotide_case(False)

	def test_get_value_by_nucleotide_case_upper(self):
		self.get_value_by_nucleotide_case()


class ValueTestCase(TestCase):

	def test_get_instance_not_integer(self):
		self.assertRaises(TypeError, Value.get_instance, '0')

	def test_get_instance_not_within_bounds(self):
		self.assertRaises(ValueError, Value.get_instance, -1)
		self.assertRaises(ValueError, Value.get_instance, 4)

	def test_get_instance(self):
		self.assertEqual(Value.zero, Value.get_instance(0))
		self.assertEqual(Value.one, Value.get_instance(1))
		self.assertEqual(Value.two, Value.get_instance(2))
		self.assertEqual(Value.three, Value.get_instance(3))
