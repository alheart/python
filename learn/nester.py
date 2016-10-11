
def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end="")
            print(each_item)


movies=[
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
        ["Graham Chapman",
             ["Michael Palin", "John cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print_lol(movies, 1)
