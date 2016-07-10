from unittest import TestCase
from io import BytesIO, StringIO

from decoder import _decode_to_byte, decode, decode_streaming
from encoder import _encode_byte
from mapping import Value, Mapping


class DecodingTestCase(TestCase):

	def setUp(self):
		self.mapping = Mapping(Value.zero, Value.one, Value.two, Value.three)
		self.decoded_bytes = [247, 65, 89]
		self.encoded_bytes = 'GTGGTAATTCTT'

	def test_decode_nucleotide(self):
		self.assertEqual(0, _decode_to_byte('A', self.mapping))
		self.assertEqual(1, _decode_to_byte('T', self.mapping))
		self.assertEqual(2, _decode_to_byte('C', self.mapping))
		self.assertEqual(3, _decode_to_byte('G', self.mapping))

	def test_decode_byte_unknown(self):
		self.assertRaises(ValueError, _decode_to_byte, 'Ä', self.mapping)

	def test_decode_byte_too_many_nucleotides(self):
		self.assertRaises(ValueError, _decode_to_byte, 'AAAAA', self.mapping)

	def test_decode_byte_permutations_nucleotides(self):
		# Assume encoding works
		for byte_value in range(255):
			dna = _encode_byte(byte_value, self.mapping)
			self.assertEqual(byte_value, _decode_to_byte(dna, self.mapping),
							 "Encoding might no be working")

	def collect_bytes(self, bytes):
		collected_bytes = []
		for byte in bytes:
			collected_bytes.append(byte)
		self.assertEqual(self.decoded_bytes, collected_bytes)

	def test_decode_multiple_bytes(self):
		self.collect_bytes(decode(self.encoded_bytes, self.mapping))

	def test_decode_multiple_bytes_streaming(self):
		text_input = StringIO(self.encoded_bytes)
		bytes_stream = BytesIO()
		decode_streaming(text_input, bytes_stream, self.mapping)
		self.collect_bytes(bytes(bytes_stream.getvalue()))
