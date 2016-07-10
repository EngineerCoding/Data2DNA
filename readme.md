# Data2DNA

This is a simple application which converts arbitrary binary data to a DNA sequence. It was quite simple to make, but the real application here has been done by [microsoft](https://www.microsoft.com/en-us/research/project/dna-storage/). The real challenge here is creating the synthetic DNA and assembling it correctly so it can be read out by machines. In the future it is quite possible that data storage is done with DNA, but by then we live in a world where technologies are further ahead then we currently are. To go from DNA to data an expensive conversion must be done. This is the biggest limitation there is, we can already make synthetic DNA, but not yet on the fly like your computer stores it data on your hard drive.

### How to use it

Currently I have not created a pluggable out of this, simply because this is more of a fun project than an actual serious project. The code itself is not documented, but there is not much code to browse through.

The important files where the action happens is in `encoder.py` and `decoder.py`. Note that the mapping parameter has a default, and please refer to `mapping.py` what the mapping actually does.

The following methods are available in `encoder.py`:

* `encode(bytes, mapping)`: This function does the conversion of bytes to a DNA sequence, however this is done in memory. The bytes argument can be any iterable which yields values `0 <= value <= 255` which is like a byte. Als the built-in function `bytes` works as an iterator, while it actually is not an iterator. It works, which is the important thing to me.
* `encode(reader, writer, mapping)`: This function does exactly the same as the original `encode` function but writes it directly to a file to avoid RAM conflicts. The reader should be a byte inputstream (for instance `open('myfile', 'rb')`) and the writer should be a text outputstream (for instance `open('myfile', 'w')`).

The following methods are available in `decoder.py`:

* `decode(sequence, mapping)`: this is the direct opposite of `encode` and takes the generated sequence of that instead.
* `decode_streaming(reader, writer, mapping)`: this is also the direct opposite of `encode_streaming` but takes a text inputstream and byte outputstream as arguments.


### How it works

#### Encoding

The encoding is done by taking the bytes one by one, and converting this in 4 nucleotides. This is because there are 4 different nucleotides in DNA: A, T, G and C. Through the specified mapping the correct nucleotides are retrieved and appended to the sequence. Each nucleotide represents 2 bits.

On another note, DNA is double stranded, but the data is not: the algorithm outputs one strand which is the "data-coding strand."

#### Decoding

The decoding is done by reading the nucleotides one by one, and since we know 4 nucleotides represent one byte (or octet of bits if we speak in strict terms), the algorithm decodes the strand literally by byte. 4 nucleotides are read and converted to the binary data.

### Disclaimer

I am in no way affiliated with Microsoft. This code is al written by me and is inspired by Microsoft's project, not taken from it. Feel free to improve my code, as I am still a student.