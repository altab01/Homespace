import json
import pickle
import numpy as np
__bengLocation=None
__delhiLocation=None

__bengColumns=None
__delhiColumns=None

__delhiModel=None
__bengModel=None

def get_location_names(city):
    if city=='benglore':
        return __bengLocation
    else:
        return __delhiLocation
    

def predict_price(city,location,sqft,bath,bhk):
     if city=='benglore':
        try:
            loc_idx=__bengColumns.index(location.lower())
        except:
         loc_idx=-1

        x=np.zeros(len(__bengColumns))
        x[0]=sqft
        x[1]=bath
        x[2]=bhk
        if loc_idx>=0:
            x[loc_idx]=1

        return round(__bengModel.predict([x])[0],2)
     else:
        try:
            loc_idx=__delhiColumns.index(location.lower())
        except:
            loc_idx=-1

        x=np.zeros(len(__delhiColumns))
        x[0]=sqft
        x[1]=bath
        x[2]=bhk
        if loc_idx>=0:
            x[loc_idx]=1
        
        result = round(__delhiModel.predict([x])[0] / 100000, 2)
        return result





def load_saved_data():
    global __bengLocation
    global __bengColumns 
    global __bengModel

    global __delhiLocation
    global __delhiColumns
    global __delhiModel

    with open("./model/banglore_columns.json",'r') as f:
        __bengColumns=json.load(f)['df_columns']
        __bengLocation=__bengColumns[3:]
            
    with open("./model/banglore_price_prediction_model.pickle",'rb') as f:
         __bengModel=pickle.load(f)

        
    with open("./model/delhi_columns.json",'r') as f:
         __delhiColumns=json.load(f)['df_columns']
         __delhiLocation=__delhiColumns[3:]

    with open("./model/delhi_price_prediction_model.pickle",'rb') as f:
            __delhiModel=pickle.load(f)
    
    

      
    


if __name__=='__main__':
    load_saved_data()
    print(get_location_names("Benglore"))
    # print(predict_price("1st phase jp nagar",1000,3,3))
    # print(predict_price("1st phase jp nagar",1000,2,2))
    # print(predict_price("ABC",1000,2,2))
