
import pickle
from athletelist import AthleteList
from athletelist import get_coach_data

def put_to_store(files_list):
    all_athletes = {}

    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))

    return (all_athletes)

def get_from_store():
    all_athletes = {}

    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)

    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))

    return (all_athletes)
