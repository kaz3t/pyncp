from helpers import *

class CRCError(Exception):
    pass

class CRCLengthError(CRCError):
    pass

class CRCPolynomialError(CRCError):
    pass


def crc(message, polynomial, width):
    try:
        width = int(width)
    except ValueError:
        raise CRCLengthError('CRC length argument does not look like an'
                             + ' integer.')
    
    if (width < 0):
        raise CRCLengthError('CRC length argument should be a positive'
                             + ' integer.')
    
    try:
        polynomial = int(polynomial)
    except ValueError:
        raise CRCPolynomialError('CRC polynomial argument does not look like'
                                 + ' an integer.')
        
    if polynomial < 0:
        raise CRCPolynomialError('CRC polynomial argument should be a positive'
                                 + ' integer.')
    
    polynomial_length = polynomial.bit_length()
    
    if polynomial_length != (width + 1):
        raise CRCPolynomialError('CRC polynomial argument does not match with'
                                 + ' length.')
    
    polynomial_bits = bin(polynomial)[2:]
    additional_bits = ''
        
    for i in range(width):
        additional_bits += '0'
        
    message += additional_bits
    message_length = len(message)
    index = 0

    while index < message_length and message[index] == '0':
            index += 1
            
    if index == message_length:
        output = ''
        for i in range(message_length):
            output += '0'
        return (output, hex(int(output, 2)))

    while True:
        begin = index
        end = index + width + 1
        message_slice = int(message[begin:end], 2)
        message_slice ^= polynomial
        message_slice_bits = bin(message_slice)[2:]
        difference = width + 1 - len(message_slice_bits)
        filler = ''
        for i in range(difference):
            filler += '0'
        message_slice_bits = filler + message_slice_bits
        message = message[:begin] + message_slice_bits + message[end:]
        index += 1
        while message[index] == '0':
            index += 1
        if (message_length - index - 1) < width:
            break
    return (message[-width:], hex(int(message[-width:], 2)))

def ncp8(message):
    message = streamify(message)
    message = reverse_bits(message)
    crc_bit, crc_int = crc(message, 0x181, 8)
    crc_bit = reverse_bits(crc_bit)
    crc_int = int(crc_bit, 2)
    crc_int ^= 0x43
    difference = 8 - len(crc_bit)
    filler = ''
    for i in range(difference):
        filler += '0'
    return (filler + crc_bit, crc_int)

def ncp16(message):
    xors = {
        1 : 0x870F,
        2 : 0xB8F0,
        4 : 0x2103,
        6 : 0x7008,
        9 : 0x184E,
        11 : 0x78EE,
        12 : 0x219F
    }
    length = len(message)
    message = streamify(message)
    message = reverse_bits(message)
    crc_bit, crc_int = crc(message, 0x11021, 16)
    crc_bit = reverse_bits(crc_bit)
    crc_int = int(crc_bit, 2)
    crc_int ^= xors[length]
    crc_bit = bin(crc_int)[2:]
    difference = 16 - len(crc_bit)
    filler = ''
    for i in range(difference):
        filler += '0'
    return (filler + crc_bit, crc_int)