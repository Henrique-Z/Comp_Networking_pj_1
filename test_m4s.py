
# let's open the file and read its first few bytes to analyze the header
file_path = "app_server/static/DASH_dataset/BigBuckBunny_565835bps/BigBuckBunny_15s1.m4s"

# reading the first 64 bytes of the file for header analysis
with open(file_path, "rb") as file:
	header_data = file.read(64)

hex_string = header_data.hex()

print(header_data)
print(type(header_data))
print(hex_string)

# obs.: OSError exception
