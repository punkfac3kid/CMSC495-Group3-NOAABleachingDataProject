import chardet as chdet

file_name = input('Input file name to check:')
raw_file = open(file_name, 'rb').read()
result = chdet.detect(raw_file)

char_enc = result['encoding']
print(char_enc)