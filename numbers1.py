def format_number(num, rep):
    formatted = format(num, rep)
    return f"The number {num} in {rep}-format is: {formatted}"


result = format_number(145, 'o')
print(result)
  


# output

# The number 145 in o-format is: 221