from mapping import DEFAULT_MAPPING


BYTE_LENGTH = 8
FIRST_TWO_BITS_MASK = 3
TWO_BITS = 2


def _encode_byte(byte, mapping):
	coding_strand = ''
	byte = int(byte)
	for _ in range(int(BYTE_LENGTH / 2)):
		coding_strand += mapping.get_nucleotide_by_value(
			byte & FIRST_TWO_BITS_MASK)
		byte >>= TWO_BITS
	return coding_strand


def encode(bytes_obj, mapping=DEFAULT_MAPPING):
	coding_strand = ''
	for byte in bytes_obj:
		coding_strand += _encode_byte(byte, mapping)
	return coding_strand


def encode_streaming(byte_stream, text_output, mapping=DEFAULT_MAPPING):
	bytes_obj = byte_stream.read(1)
	while bytes_obj:
		text_output.write(encode(bytes_obj, mapping))
		bytes_obj = byte_stream.read(1)
