FORMAT = 'utf-8'
HEADER = 5

data = "sdfe44g"
data_length = len(data)
encode_data_length = str(data_length).encode(FORMAT)
encode_data_length += b' ' * (HEADER - len(encode_data_length))
print(encode_data_length)
print(int(encode_data_length.decode()))
