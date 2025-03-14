import base64
import codecs

def decode_script(encoded_script):
    try:
        # Try base64 decoding
        decoded_bytes = base64.b64decode(encoded_script, validate=True)
        decoded_str = decoded_bytes.decode('utf-8', errors='ignore')
        print("Base64 Decoded:", decoded_str)

        # Try ROT13 decoding (if applicable)
        rot13_decoded = codecs.decode(decoded_str, 'rot_13')
        print("ROT13 Decoded:", rot13_decoded)

        return decoded_str
    except Exception as e:
        print("Decoding Error:", str(e))
        return None

# Read input from file in binary mode
with open("HostOnion", "rb") as file:
    encoded_bytes = file.read()

# Try decoding as UTF-8 first
try:
    encoded_script = encoded_bytes.decode('utf-8').strip()
except UnicodeDecodeError:
    # Fallback to Latin-1 or other encoding
    encoded_script = encoded_bytes.decode('latin-1').strip()

decoded_script = decode_script(encoded_script)

if decoded_script:
    print("Final Decoded Script:")
    print(decoded_script)

    # Save output to file
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write(decoded_script)
