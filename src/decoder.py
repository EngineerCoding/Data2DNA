from mapping import DEFAULT_MAPPING
from encoder import TWO_BITS


NUCLEOTIDES_FOR_BYTE = 4


def _decode_to_byte(nucleotides, mapping):
	if len(nucleotides) > NUCLEOTIDES_FOR_BYTE:
		raise ValueError("Maximum of 4 nucleotides are accepted!")
	value = 0
	iteration = 0
	for nucleotide in nucleotides:
		current_value = mapping.get_value_by_nucleotide(nucleotide)
		if current_value is None:
			raise ValueError("Unknown nucleotide: " + nucleotide)
		current_value <<= iteration * TWO_BITS
		iteration += 1
		value += current_value
	return value


def decode(sequence, mapping=DEFAULT_MAPPING):
	bytes_array = []
	for index in range(0, len(sequence), NUCLEOTIDES_FOR_BYTE):
		combination = sequence[index:index+4]
		bytes_array.append(_decode_to_byte(combination, mapping))
	return bytes(bytes_array)


def decode_streaming(reader, writer, mapping=DEFAULT_MAPPING):
	combination = reader.read(NUCLEOTIDES_FOR_BYTE)
	while combination:
		writer.write(decode(combination, mapping))
		combination = reader.read(NUCLEOTIDES_FOR_BYTE)
