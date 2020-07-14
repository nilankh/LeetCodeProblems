import re
##txt = "The rain in Spain"
##x = re.search("^The.*Spain$", txt)
####print(x)
##if x:
##    print("YES! We have a match!")
##else:
##    print("No Match")


##The findall() Function
##The findall() function returns a list containing all matches.
##txt = "The rain in Spain"
##x = re.findall("ai", txt)
##print(x)
##The list contains the matches in the order they are found.
##
##If no matches are found, an empty list is returned:

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
