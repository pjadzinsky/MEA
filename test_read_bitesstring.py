from nose.tools import *
import numpy as np
import pdb

def test_sign_unsigned():
    """
    In the recording computer (a PC) I made a wave of bytes like this
        make /o/n=256/B test=p
    and wrote it in binary format either with signed or unsigned bytes
    (Big endian)
        FBinWrite /b=2/f=1/U refnum as "signed_bytes"
        or 
        FBinWrite /B=2/f=1 refnum as "unsigned_bytes" 

    read the byte string and make sure those are the same
    """

    #pdb.set_trace()
    bytes_to_read=-1#120
    with open('Data/unsigned_bytes', 'rb') as f:
        unsigned = f.read(bytes_to_read)

    with open('Data/signed_bytes', 'rb') as f:
        signed = f.read(bytes_to_read)
    
    print(signed)
    assert_equal(unsigned, signed)

def test_fromfile():
    """ 
    """
    unsigned = np.fromfile('Data/unsigned_bytes', dtype='int8')
    signed = np.fromfile('Data/signed_bytes', dtype='int8')
    bytes_string = signed.astype('U')

    print(bytes_string)
    print(signed)
    print(unsigned==signed)
    print(len(unsigned))
