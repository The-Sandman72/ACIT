KB = 1024
MB = 1048576
GB = 1073741824

num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

kb_size = (num_entries * entry_size) / KB
mb_size = (num_entries * entry_size) / MB
gb_size = (num_entries * entry_size) / GB

print('''Storage Estimates
==================================
''')
print(f"Per minute: {kb_size}KB")
print(f"Per minute: {mb_size}MB")
print(f"Per minute: {gb_size}GB")