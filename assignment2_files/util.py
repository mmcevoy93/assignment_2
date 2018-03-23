# The functions in this file are to be implemented by students.
from bitio import BitReader
from bitio import BitWriter
import huffman


def read_tree(bitreader):
    '''Read a description of a Huffman tree from the given bit reader,
    and construct and return the tree. When this function returns, the
    bit reader should be ready to read the next bit immediately
    following the tree description.

    Huffman trees are stored in the following format:
      * TreeLeaf is represented by the two bits 01, followed by 8 bits
          for the symbol at that leaf.
      * TreeLeaf that is None (the special "end of message" character)
          is represented by the two bits 00.
      * TreeBranch is represented by the single bit 1, followed by a
          description of the left subtree and then the right subtree.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.

    Returns:
      A Huffman tree constructed according to the given description.
    '''

    table = huffman.make_freq_table(bitreader)
    tree = huffman.make_tree(table)
    return tree


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    br = BitReader(bitreader)
    encoded_table = huffman.make_encoding_table(tree)
    sample = 0
    bits = 0
    better_table = {}
    b = br.readbit()
    for n in encoded_table:
        for v in encoded_table[n]:
            if v is True:
                sample *= 2
                sample += 1
            else:
                sample *= 2
        better_table[sample] = n
        sample = 0
    print(better_table)




def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.

    '''
    file = open('gtest.txt', 'wb')
    bw = BitWriter(file)
    br = BitReader(compressed)
    bits = br.readbits(0)
    bity = br.readbits(1512)
    bw.writebits(bits, 0)
    bw.flush()
    file.closed
    file = open('test.txt', 'rb')

    tree = read_tree(file)
    file.closed
    file = open('gtest.txt', 'wb')
    bw = BitWriter(file)
    bw.writebits(bity, 1512)
    file.closed
    file = open('test.txt', 'rb')
    br = BitReader(file)


    out = decode_byte(tree, file)
    print(br.readbits(100))


    bw = BitWriter(uncompressed)




def write_tree(tree, bitwriter):
    '''Write the specified Huffman tree to the given bit writer.  The
    tree is written in the format described above for the read_tree
    function.

    DO NOT flush the bit writer after writing the tree.

    Args:
      tree: A Huffman tree.
      bitwriter: An instance of bitio.BitWriter to write the tree to.
    '''
    pass


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''
    pass
