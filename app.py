from flask import Flask, render_template, request
import pickle
#from sklearn.ensemble import RandomForestClassifier
## loding pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':

        f1 =  float(request.form.get('feature1'))
        f2 =  float(request.form.get('feature2'))
        f3 =  float(request.form.get('feature3'))
        f4 =  float(request.form.get('feature4'))
        f5 =  float(request.form.get('feature5'))
        f6 =  float(request.form.get('feature6'))
        f7 =  float(request.form.get('feature7'))
        f8 =  float(request.form.get('feature8'))
        f9 =  float(request.form.get('feature9'))
        f10 = float(request.form.get('feature10'))
        f11 = float(request.form.get('feature11'))
        f12 = float(request.form.get('feature12'))
        f13 = float(request.form.get('feature13'))
        f14 = float(request.form.get('feature14'))
        f15 = float(request.form.get('feature15'))
        f16 = float(request.form.get('feature16'))
        f17 = float(request.form.get('feature17'))
        #features = [request.form[f'feature{i}'] for i in range(1, 18)]

        result=model.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17]])
    
    res=''
    if int(result[0])==0:
        res='This data is belongs to CLUSTER 0'
    elif int(result[0])==1:
        res= 'This data is belongs to CLUSTER 1 '
        
    elif int(result[0])==2:
        res= 'This data is belongs to CLUSTER 2'
    else:
        res = 'This data is belongs to CLUSTER 3'
    
    return render_template('result.html',result=res)


if __name__ == '__main__':
    app.run(debug=True)
