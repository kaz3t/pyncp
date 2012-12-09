# Python 2.7 is needed due to some used assertions
import unittest

from crc import ncp8, ncp16
from helpers import byteify


class TestNCP8(unittest.TestCase):
    def setUp(self):
        self.message1 = [0xFF, 0x01, 0x01, 0x00, 0x88, 0x03, 0x80, 0x64, 0x1E,
                         0x00, 0x00]
        self.message2 = [0xFF, 0x01, 0x01, 0x00, 0x88, 0x04, 0x80, 0x64, 0x1E,
                         0x00, 0x00]
        self.message3 = [0x80, 0x01, 0x08, 0x00, 0x88, 0x12, 0x28, 0x77, 0x10,
                         0x84, 0x00]
        self.message4 = [0x80, 0x01, 0x08, 0x00, 0x88, 0x1B, 0x28, 0x66, 0x08,
                         0x30, 0x00]
        self.message5 = [0x80, 0x01, 0x08, 0x00, 0x88, 0x29, 0x28, 0x81, 0x0C,
                         0x20, 0x00]

    def test_message1(self):
        crc_bit, crc_int = ncp8(self.message1)
        self.assertEqual(crc_int, 0xFB)

    def test_message2(self):
        crc_bit, crc_int = ncp8(self.message2)
        self.assertEqual(crc_int, 0x77)
        
    def test_message3(self):
        crc_bit, crc_int = ncp8(self.message3)
        self.assertEqual(crc_int, 0x64)
        
    def test_message4(self):
        crc_bit, crc_int = ncp8(self.message4)
        self.assertEqual(crc_int, 0x81)
        
    def test_message5(self):
        crc_bit, crc_int = ncp8(self.message5)
        self.assertEqual(crc_int, 0xF7)

class TestNCP16OneByte(unittest.TestCase):
    def setUp(self):
        self.message1 = [0x00]
        self.message2 = [0x40]
        self.message3 = [0x2E]
        self.message4 = [0x2F]
        self.message5 = [0x3A]
    
    def test_message1(self):
        crc_bit, crc_int = ncp16(self.message1)
        self.assertListEqual(byteify(crc_bit), [0x87, 0x0F])
        
    def test_message2(self):
        crc_bit, crc_int = ncp16(self.message2)
        self.assertListEqual(byteify(crc_bit), [0x83, 0x4D])
        
    def test_message3(self):
        crc_bit, crc_int = ncp16(self.message3)
        self.assertListEqual(byteify(crc_bit), [0xFB, 0xC7])
        
    def test_message4(self):
        crc_bit, crc_int = ncp16(self.message4)
        self.assertListEqual(byteify(crc_bit), [0x72, 0xD6])
        
    def test_message5(self):
        crc_bit, crc_int = ncp16(self.message5)
        self.assertListEqual(byteify(crc_bit), [0x5E, 0x91])    
        
class TestNCP16TwoBytes(unittest.TestCase):
    def setUp(self):
        self.message1 = [0x00, 0x00]
        self.message2 = [0x01, 0x5D]
        self.message3 = [0x00, 0xF8]
        self.message4 = [0x00, 0xE6]
        self.message5 = [0x03, 0x5F]
        
    def test_message1(self):
        crc_bit, crc_int = ncp16(self.message1)
        self.assertListEqual(byteify(crc_bit), [0xB8, 0xF0])
        
    def test_message2(self):
        crc_bit, crc_int = ncp16(self.message2)
        self.assertListEqual(byteify(crc_bit), [0x00, 0x60])
        
    def test_message3(self):
        crc_bit, crc_int = ncp16(self.message3)
        self.assertListEqual(byteify(crc_bit), [0x7F, 0x8B])
        
    def test_message4(self):
        crc_bit, crc_int = ncp16(self.message4)
        self.assertListEqual(byteify(crc_bit), [0x80, 0x72])
        
    def test_message5(self):
        crc_bit, crc_int = ncp16(self.message5)
        self.assertListEqual(byteify(crc_bit), [0xA2, 0x70])
        
class TestNCP16NineBytes(unittest.TestCase):
    def setUp(self):
        self.message1 = [0x09, 0x20, 0x0e, 0x05, 0x18, 0x26, 0x09, 0x0a, 0x01]
        self.message2 = [0x09, 0x2a, 0x0e, 0x05, 0x18, 0x26, 0x09, 0x0a, 0x01]
        self.message3 = [0x09, 0x34, 0x0e, 0x05, 0x18, 0x26, 0x09, 0x0a, 0x01]

    def test_message1(self):
        crc_bit, crc_int = ncp16(self.message1)
        self.assertListEqual(byteify(crc_bit), [0x37, 0x02])
        
    def test_message2(self):
        crc_bit, crc_int = ncp16(self.message2)
        self.assertListEqual(byteify(crc_bit), [0xE4, 0x24])
        
    def test_message3(self):
        crc_bit, crc_int = ncp16(self.message3)
        self.assertListEqual(byteify(crc_bit), [0x91, 0x4F])
        
        
if __name__ == "__main__":
    unittest.main()