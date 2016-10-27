import sys 

def print_lol(the_list, indent=False, level=0, outfile=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, outfile)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end="", file=outfile)
            print(each_item, file=outfile)


movies=[
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
        ["Graham Chapman",
             ["Michael Palin", "John cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print_lol(movies, True, 1)
