def streamify(bytes=[]):
    zeros = {
        1 : '0',
        2 : '00',
        3 : '000',
        4 : '0000',
        5 : '00000',
        6 : '000000',
        7 : '0000000'
    }
    bits = ''
    if len(bytes) < 1:
        return bits
    for byte in bytes:
        byte_bits = bin(byte)[2:]
        length = len(byte_bits)
        element = ''
        if length < 8:
            element = zeros[8 - length]
        element = element + byte_bits
        bits += element
    return bits

def reverse_bits(message):
    length = len(message)
    reversed = ''
    index = 0
    while length > 0:
        slice = message[index:(index + 8)]
        slice = slice[::-1]
        index += 8
        length -= 8
        reversed += slice
    return reversed
    
def byteify(message):
    length = len(message)
    index = 0
    bytes = []
    while length > 0:
        slice = message[index:(index + 8)]
        bytes.append(int(slice, 2))
        index += 8
        length -= 8
    return bytes