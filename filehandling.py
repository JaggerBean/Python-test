# this is a demo cript to show how filehandling works in py
with open('/usr/share/dict/words', 'r') as f:
    for x in range(5):
        print(f.readline())
