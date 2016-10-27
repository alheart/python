#import nester
import pickle

man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if (role == 'Man'):
                man.append(line_spoken)
            elif (role == 'Other Man'):
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()

except IOError:
    print('The datafile is missing!')


try:
    with open('man_data.txt', 'wb') as manfile:
        pickle.dump(man, manfile)
        #nester.print_lol(man, outfile=manfile)
    with open('other_data.txt', 'wb') as otherfile:
        #nester.print_lol(other, outfile=otherfile)
        pickle.dump(other, otherfile)
except IOError:
    print('write file error!')
except pickle.PickleError as perr:
    print('Pickle Error ' + str(perr))
    
