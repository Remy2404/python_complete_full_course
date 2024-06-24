try:
    f = open("file.txt")
except:
    print('Could not open file')
finally:
    f.close()
    print('Program continue')