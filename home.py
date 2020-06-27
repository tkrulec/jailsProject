from flask import Flask, render_template, request      
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/second", methods=['POST'])
def second():
	option = request.form['factor']
	df=pd.read_pickle('stats.pkl')
	df['got bail']= df['% awarded bail']
	df['got bail']=df['got bail'].round(2)
	df['average bail']=df['average bail'].round(2)
	df.at[4,'variable']= "Citizen"
	df.at[5,'variable']= "Non-citizen"
	if option==('skintone'):
		var1 = 0
		var2 = 1
		source = 1086978
	elif option==('gender'):
	 	var1 = 2
	 	var2 = 3
	 	source = 1086895
	elif option==('citizenship'):
	 	var1 = 4
	 	var2 = 5
	 	source = 1086955

	var_name1 = df.at[var1,'variable']
	var_name2 = df.at[var2,'variable']

	bail_pct1 = df.at[var1,'got bail']
	bail_pct2 = df.at[var2,'got bail']

	bail_avg1 = df.at[var1,'average bail']
	bail_avg2 = df.at[var2,'average bail']

	top_charges1 = df.at[var1,'top 5 charges']
	top_charges2 = df.at[var2,'top 5 charges']
	return render_template("simulation.html",source=source,top_charges1=top_charges1, top_charges2=top_charges2, option=option, var_name1=var_name1, var_name2=var_name2, bail_pct1=bail_pct1, bail_pct2=bail_pct2, bail_avg1=bail_avg1, bail_avg2=bail_avg2)

@app.route("/third")
def third():
	return render_template("third.html")


@app.route("/fourth", methods=['POST'])
def fourth():
	if request.method == 'POST': 
		charge_input = request.form['charge'].upper()
		skin_input = request.form['skintone']
		sex_input = request.form['gender']
		cit_input = request.form['citizenship']

		df3 = pd.read_pickle('frame.pkl')
		df3['Charge']=df3['Charge'].str.rstrip()
		row = df3.loc[(df3['Charge'] == charge_input) & (df3['Skin_Tone']==skin_input) & (df3['Sex'] == sex_input) & (df3['Citizenship_Status']==cit_input)]
		prediction = row['Prediction'].values[0]
	return render_template("third.html",prediction=prediction)

















