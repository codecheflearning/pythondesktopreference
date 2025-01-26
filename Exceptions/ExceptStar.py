#Example of except* to filter exception groups

try:
    x = [1, 2, 3]
    noVal = x[3]
    badVal = int("string")
except* ValueError:
    print("A ValueError occurred.")
except* IndexError:
    print("A IndexError occurred.")