# The functions in this file are to be implemented by students.
import bitio  # changed this cause i dont know why they didnt in the first place
import huffman
import time


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

    def re_tree(bitreader):
        bit = bitreader.readbit()
        if bit == 1:
            tree = huffman.TreeBranch(None, None)
            tree.left = re_tree(bitreader)
            tree.right = re_tree(bitreader)
            return tree
        elif bit == 0:
            anotherbit = bitreader.readbit()
            if anotherbit == 0:
                return huffman.TreeLeaf(None)
            else:
                leafval = bitreader.readbits(8)
                return huffman.TreeLeaf(leafval)

    tree = huffman.TreeBranch(None, None)
    bitreader.readbit()
    tree.left = re_tree(bitreader)
    tree.right = re_tree(bitreader)

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
    # if instance is built into python, and is used to check
    # when we reach our leaf with the value inside it
    if isinstance(tree, huffman.TreeBranch):
        bit = bitreader.readbit()
        if bit == 0:
            tree = tree.left
            return decode_byte(tree, bitreader)
        elif bit == 1:
            tree = tree.right
            return decode_byte(tree, bitreader)
    elif isinstance(tree, huffman.TreeLeaf):
        return tree.value


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

    '''br = BitReader(compressed)
    tree = read_tree(br)
    print(tree.left.left.left.left.left)
    # encoded_table = huffman.make_encoding_table(tree)
    # print(encoded_table)
    # print(bin(br.readbits(100)))
    bw = BitWriter(uncompressed)
    while True:
        try:
            bit = br.readbit()
            byte = decode_byte(tree, br)
            bw.writebits(byte, 8)
        except EOFError:
            break

    bw.writebit(0b0)
    bw.writebit(0b1)
    bw.writebit(0b0)
    bw.writebit(0b1)

    bw.writebit(0b0)
    bw.writebit(0b0)
    bw.writebit(0b1)
    bw.writebit(0b0)'''
    # initialize the reading and writing
    reader = bitio.BitReader(compressed)
    writer = bitio.BitWriter(uncompressed)
    tree = read_tree(reader)

    while 1:
        byte = decode_byte(tree, reader)
        if byte == None:  # means ending
            break
        else:
            writer.writebits(byte, 8)


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
