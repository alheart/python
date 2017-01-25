

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = (data.strip().split(','))
        return ({'Name' : templ.pop(0),
                 'DOB'  : templ.pop(0),
                 'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})

    except IOError as err:
        print('File error: ' + str(err))
        return (None)


sarah=get_coach_data('sarah2.txt')

def print_data(name):
    file_name = name + '2.txt'
    coach_data = get_coach_data(file_name)
    print(coach_data['Name'] + "'s fastest times are: " + coach_data['Times'])


print_data('james')
print_data('julie')
print_data('mikey')
print_data('sarah')
