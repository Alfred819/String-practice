def extract_number(s):
    num_str = ""
    for char in s:
        if char.isdigit() or char == '.':
            num_str += char
    num = float(num_str)
    return "{:.2f}".format(num)

print(extract_number("abcd123.456"))
print(extract_number("abcd123"))