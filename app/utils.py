import pickle
import json
import numpy as np
import os

class Prediction():
    def __init__(self,data):
        self.data = data
        print(os.getcwd())
        os.chdir('artifacts')
        print(os.getcwd())
        print(os.listdir())
        with open(r'linear_model.pkl','rb') as file:
            self.model = pickle.load(file)
        with open(r'columns_names.json','r') as col_file:
            self.column_name = json.load(col_file)

        with open(r'encoded_data.json', 'r')as encoded:
            self.encoded_data = json.load(encoded)

    # def load_raw(self):
        # print(os.getcwd())
    #    
    #    
    #    
    #    
        # print(self.column_name)
        # 
        # 
        
    def predict_price(self):

        user_input =np.zeros(len(self.column_name['Column Names']))
        array = np.array(self.column_name['Column Names'])

        symboling = self.data["symb"]
        normalized_losses = self.data['normalized_losses']
        make = self.data['make']
        fuel_type = self.data['fule_type']
        aspiration = self.data['aspiration']
        num_of_doors = self.data['num_of_doors']
        body_style = self.data['body_style']
        drive_wheels = self.data['drive_wheel']
        engine_location = self.data['engine_location']
        wheel_base =self.data['wheel_base']
        length = self.data['length']
        width = self.data['width']
        height = self.data['height']
        curb_weight = self.data['curb_weight']
        engine_type = self.data['engine_type']
        num_of_cylinders = self.data['num_of_cylinders']
        engine_size = self.data['engine_size']
        fuel_system = self.data["fuel_system"]
        bore = self.data['bore']
        stroke = self.data['stroke']
        compression_ratio = self.data['compression_ratio']
        horsepower = self.data['horsepower']
        peak_rpm = self.data['peak_rpm']
        city_mpg = self.data['city_mpg']
        highway_mpg =self.data['highway_mpg']
    
        user_input[0] = symboling
        user_input[1] = normalized_losses

        make_string = 'make_'+make
        make_index = np.where(array == make_string)[0][0]
        user_input[make_index] = 1

        user_input[2] = int(fuel_type)
        user_input[3] = int(aspiration)
        user_input[4]= int(num_of_doors)

        body_style_string = 'body-style_'+body_style
        bs_index = np.where(array == body_style_string)[0][0]
        user_input[bs_index] = 1
        drive_wheels_string = 'drive-wheels_'+drive_wheels
        drive_wheels_string_index = np.where(array == drive_wheels_string)[0][0]
        user_input[drive_wheels_string_index]=1

        user_input[5] = int(engine_location)
        user_input[6]= wheel_base
        user_input[7]= length
        user_input[8] = width
        user_input[9]= height
        user_input[10] =curb_weight

        engine_type_string = 'engine-type_'+engine_type
        et_index = np.where(array == engine_type_string)[0][0]
        user_input[et_index]=1

        user_input[11] = self.encoded_data['num_of_cylinders'][num_of_cylinders]
        user_input[12] = engine_size

        fuel_system_string = 'fuel-system_'+fuel_system
        fs_index = np.where(array== fuel_system_string)[0][0]
        user_input[fs_index] =1

        user_input[13] = float(bore)
        user_input[14] = float(stroke)
        user_input[15] = float(compression_ratio)
        user_input[16] = horsepower
        user_input[17] = peak_rpm
        user_input[18] = city_mpg
        user_input[19] = highway_mpg

        print(f'{user_input=}')
        print(len(user_input))
        print(self.data)
        price = self.model.predict([user_input])
        print(price)
        print('actual price = 22625')
        return price
    

if __name__ == "__main__":
    pred_obj = Prediction()