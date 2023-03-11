from flask  import Flask,request,url_for,redirect,render_template
from app.utils import Prediction

 

app = Flask(__name__)



@app.route('/')
def start():
    return render_template('car_html.html')

@app.route('/predict_price',methods= ['POST','GET'])
def predict_price():
    if request.method =='POST':
        data = request.form
        proj_obj = Prediction(data)

        predicted_price = proj_obj.predict_price()
        return str(predicted_price[0])
    else:
        return render_template('car_html.html')


if __name__ == '__main__':
    app.run(debug=True)
