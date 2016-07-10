from unittest import TestCase
from io import BytesIO, StringIO

from mapping import Mapping, Value
from encoder import _encode_byte, encode, encode_streaming


class EncodingTestCase(TestCase):

	def setUp(self):
		self.bytes_obj = bytes([57, 65, 101])
		self.correct_bytes_obj = 'TCGATAATTTCT'
		self.mapping = Mapping(Value.zero, Value.one, Value.two, Value.three)

	def test_encode_byte(self):
		self.assertEqual('TCGA', _encode_byte(57, self.mapping))

	def test_encode_bytes(self):
		self.assertEqual(self.correct_bytes_obj, encode(self.bytes_obj,
														self.mapping))

	def test_encode_streaming_bytes(self):
		byte_stream = BytesIO(self.bytes_obj)
		text_output = StringIO()
		encode_streaming(byte_stream, text_output, self.mapping)
		self.assertEqual(self.correct_bytes_obj, text_output.getvalue())
