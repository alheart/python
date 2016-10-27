

with open('james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(',')
with open('julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)


clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []


clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]

    
print(sorted(set(clean_james))[0:3])
print(sorted(set(clean_julie))[0:3])
print(sorted(set(clean_mikey))[0:3])
print(sorted(set(clean_sarah))[0:3])
