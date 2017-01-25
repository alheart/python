

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)

class AthleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = (data.strip().split(','))
        return (AthleteList(templ.pop(0), templ.pop(0), templ))

    except IOError as err:
        print('File error: ' + str(err))
        return (None)


sarah=get_coach_data('sarah2.txt')

def print_data(name):
    file_name = name + '2.txt'
    athlete = get_coach_data(file_name)
    print(athlete.name + "'s fastest times are: " + str(athlete.top3()))


print_data('james')
print_data('julie')
print_data('mikey')
print_data('sarah')
