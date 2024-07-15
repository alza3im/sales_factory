import hashlib
import base62

def hash_base62(input_string, length=8):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the input string encoded as bytes
    sha256.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hex_hash = sha256.hexdigest()
    
    # Convert the hexadecimal hash to an integer
    int_hash = int(hex_hash, 16)
    
    # Encode the integer to base62
    encoded_url = base62.encodebytes(int_hash.to_bytes((int_hash.bit_length() + 7) // 8, 'big'))

    return  encoded_url[:length]
    
    
