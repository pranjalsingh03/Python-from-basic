import base58
# from bitcoinlib.encoding import base58_decode_check
def is_valid_btc_address(address):
    try:
        decode =  base58.b58decode_check(address)
        return True
    except ValueError:
        return False
address = '1BvBMSEYstWetqTFn5Au4m4GFg723442aNVN2'
if is_valid_btc_address(address):
    print(f"{address} is a valid Bitcoin address.")
else:
    print(f"{address} is not a valid Bitcoin address.")