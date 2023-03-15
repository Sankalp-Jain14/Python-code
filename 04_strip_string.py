def remove_and_split(string , word):
    newStr = string.replace(word , "")
    return newStr.strip()


this = "             This is Sankalp      "

f = remove_and_split(this,"Sankalp")
print(f)
