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

##txt = "The rain in Spain"
##x = re.findall("Portugal", txt)
##print(x)




##The search() Function
##The search() function searches the string for a match, and returns a Match object if there is a match.
##
##If there is more than one match, only the first occurrence of the match will be returned:

##txt = "The rain in Spain"
##x = re.search("\s", txt)
##
##print("The first white-space character is located in position:", x.start())
##If no matches are found, the value None is returned:
##txt = "The rain in Spain"
##x = re.search("Portugal", txt)
##print(x)

























