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



##The split() Function
##The split() function returns a list where the string has been split at each match:

##txt = "The rain in Spain"
##x = re.split("\s", txt)
##print(x)

##You can control the number of occurrences by specifying the maxsplit parameter:
##Example
##Split the string only at the first occurrence:
##txt = "The rain in Spain"
##x = re.split("\s", txt, 1)
##print(x)


##The sub() Function
##The sub() function replaces the matches with the text of your choice
##Example
##Replace every white-space character with the number 9:

##txt = "The rain in Spain"
##x = re.sub("\s", "9", txt)
##print(x)
##You can control the number of replacements by specifying the count parameter:
##Example
##Replace the first 2 occurrences:
##txt = "The rain in Spain"
##x = re.sub("\s", "9", txt, 2)
##print(x)




##Match Object
##A Match Object is an object containing information about the search and the result.
##
##Note: If there is no match, the value None will be returned, instead of the Match Object.
##
##Example
##Do a search that will return a Match Object:


##txt = "The rain in Spain"
##x = re.search("ai", txt)
##print(x) #this will print an object


##The Match object has properties and methods used to retrieve information about the search, and the result:
##
##.span() returns a tuple containing the start-, and end positions of the match.
##.string returns the string passed into the function
##.group() returns the part of the string where there was a match


##Example
##Print the position (start- and end-position) of the first match occurrence.
##
##The regular expression looks for any words that starts with an upper case "S":


##txt = "The rain in Spain"
##x = re.search(r"\bS\w+", txt)
##print(x.span())
##span() returns both start and end indexes in a single tuple. Since the match() method only checks if the RE matches at the start of a string,
##start() will always be zero.






























