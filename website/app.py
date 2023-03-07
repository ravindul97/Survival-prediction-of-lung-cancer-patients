from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def prediction(list):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred = model.predict([list])
    return pred

@app.route('/', methods =['POST', 'GET']) #define address
def index():
    pred_value = 0 
    if request.method ==  'POST':
        age = request.form['age']
        in_vol = request.form['in_vol']
        out_vol = request.form['out_vol']
        diagnose = request.form['diagnose']
        tumour_size = request.form['tumour_size']
        pain = request.form.getlist('pain')
        Haemoptysis = request.form.getlist('Haemoptysis')
        short_breath = request.form.getlist('short_breath')
        cough = request.form.getlist('cough')
        weekness = request.form.getlist('weekness')
        diabetes = request.form.getlist('diabetes')
        breathing_difficulty = request.form.getlist('breathing_difficulty')
        other_disease = request.form.getlist('other_disease')
        smoking = request.form.getlist('smoking')
        asthma = request.form.getlist('asthma')

        feature_list = []
        feature_list.append(float(in_vol))
        feature_list.append(float(out_vol))
        feature_list.append(len(pain))
        feature_list.append(len(Haemoptysis))
        feature_list.append(len(short_breath))
        feature_list.append(len(cough))
        feature_list.append(len(weekness))
        feature_list.append(len(diabetes))
        feature_list.append(len(breathing_difficulty))
        feature_list.append(len(other_disease))
        feature_list.append(len(smoking))
        feature_list.append(len(asthma))
        feature_list.append(int(age))

        diagnose_list =['dgn1', 'dgn2', 'dgn3', 'dgn4', 'dgn5', 'dgn6', 'dgn8']
        tumour_size_list =['oc11', 'oc12', 'oc13', 'oc14']

        # for x in diagnose_list:
        #     if x == diagnose:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def loop(list, value):
            for item in list:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        loop(diagnose_list, diagnose)
        loop(tumour_size_list, tumour_size)

        pred_value = prediction(feature_list)


    return render_template("index.html", pred_value = pred_value)

if __name__ == '__main__':
    app.run(debug=True)