#find double spaces in a given string

st = "This is a string with double  spaces"

DoubleSpaces = st.find("  ")
print(DoubleSpaces)


#replace doubles spaces with single space

st = "This is a string with double  spaces"

print(st.replace("  "," "))