#!/usr/bin/env python3

##############################################################################
# Collection of string altering functions. The functions may appear very     #
# specific as well as inefficient. Some you may consider prototypes.         #
# However, feel free to use them.                                            #
##############################################################################


"""
Passing in a string, the function strips every commonly used sign and replaces 
it wiht a whitespace, to isolate every word. It then splits the string at every
whitespace, creating a list of each word individually. In the last step it
counts the appearances of every word, excluding duplicates to be moved into 
the dictionary ( 'if(e not in counts):' ).
"""
    
def countWords(source_str):
    signs = [',','.',':','!',';','-','#','_','"','+','|','<','>','*']
        
    #seperate every word from any given sign it migth be concatenated with
    for sign in signs:
        source_str = source_str.replace(sign," ")
        
    #count every word and put it into a dict. Attention: Casesensitive.
    l = []
    l = source_str.split(" ")
    l.sort()
    counts = {}
    for e in l:
        if(e not in counts):
            c = source_str.count(e)
            counts[e] = c
    return counts


"""
Passing in a source string in which to insert, the exact substring after which
to insert, and the substring to be inserted as arguments, the function partitions
the source_string at the position of the substring, after which we wish to insert,
inside a tuple. In order to make the partioned string mutable, we format the  
tuple into a list. Using the insert method from the list class, we insert 
the string to be inserted into the list and concatenate the string pieces in a
final step to the resulting string. The function then return the resulting
string.
"""

def insertString(source_str, insertAfter_str, insertion_str):
    tmp_tup = source_str.partition(insertAfter_str)
    li = []
    for e in tmp_tup:
        li.append(e)

    li.insert(-1, insertion_str)
    new_str = ""
    for e in li:
        new_str = new_str + e

    return new_str 
