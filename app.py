from flask import Flask,render_template,request
import pandas as pd
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb+'))

@app.route('/',methods=['POST','GET'])
def wine_quality():
    if request.method == 'POST':
        type=request.form['type']
        fixed_acidity=request.form['fixed_acidity']
        volatile_acidity=request.form['volatile_acidity']
        citric_acid=request.form['citric_acidity']
        residual_sugar=request.form['residual_sugar']
        chlorides=request.form['chlorides']
        free_sulfur_dioxide=request.form['free_sulfur_dioxode']
        total_sulfur_dioxide=request.form['total_sulfur_dioxode']
        density=request.form['density']
        ph=request.form['ph']
        sulphates=request.form['sulphates']
        alcohol=request.form['alcohol']
        data=pd.DataFrame({'type':type,"fixed acidity":fixed_acidity,"volatile acidity":volatile_acidity,"citric acid":citric_acid,'residual sugar':residual_sugar,
        "chlorides":chlorides,"free sulfur dioxide":free_sulfur_dioxide,"total sulfur dioxide":total_sulfur_dioxide,"total sulfur dioxide":total_sulfur_dioxide,"density":density,
        "pH":ph,"sulphates":sulphates,"alcohol":alcohol},index=[0])
        pred=model.predict(data)
        val=pred[0]
        if val == '3' or val== 3:
            return render_template('index2.html',val=val)
        elif val == '4' or val== 4:
            return render_template('index2.html',val=val)
        elif val == '5' or val== 5:
            return render_template('index2.html',val=val)
        elif val == '6' or val== 6:
            return render_template('index2.html',val=val)
        elif val == '7' or val== 7:
            return render_template('index2.html',val=val)
        elif val == '8' or val== 8:
            return render_template('index2.html',val=val)
        else:
            return render_template('index2.html',val=val)
        


    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)