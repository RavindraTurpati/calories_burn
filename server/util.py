import pickle
import json
import numpy as np

__genders = None
__data_columns = None
__model = None

def get_estimated_calories(gender,age,height,weight,duration,heart_rate,body_temp):
    try:
        loc_index = __data_columns.index(gender.lower())
    except:
        loc_index = -1
    p = np.zeros(len(__data_columns))
    p[0]=age
    p[1]=height
    p[2]=weight
    p[3]=duration
    p[4]=heart_rate
    p[5]=body_temp
    if loc_index>=0:
        p[loc_index]=1
    return round(__model.predict([p])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __genders

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __genders = __data_columns[6:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/calories_burn44.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_gender_names():
    return __genders

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_gender_names())
    print(get_estimated_calories('male',42,150,50,30,57,136))
