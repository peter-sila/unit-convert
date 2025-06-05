from flask import Flask, render_template, request

app = Flask(__name__)

# Length conversion factors to meters
length_units = {
   "millimeter": 0.001, "centimeter": 0.01, "meter": 1,
   "kilometer": 1000, "inch": 0.0254, "foot": 0.3048,
   "yard": 0.9144, "mile": 1609.34
}

# Weight conversion factors to grams
weight_units = {
   "milligram": 0.001, "gram": 1, "kilogram": 1000,
   "ounce": 28.3495, "pound": 453.592
}

@app.route('/')
def home():
   return render_template('base.html')

@app.route('/length', methods=['GET', 'POST']) 
def length():
   result = None
   if request.method == 'POST':
      value = float(request.form['value'])
      from_unit = request.form['from_unit']
      to_unit = request.form['to_unit']
      result = value * length_units[from_unit] / length_units[to_unit]
   return render_template('length.html', units=length_units.keys(), result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
   result = None
   if request.method == 'POST':
      value = float(request.form['value'])
      from_unit = request.form['from_unit']
      to_unit = request.form['to_unit']
      result = value * weight_units[from_unit] / weight_units[to_unit]
   return render_template('weight.html', units=weight_units.keys(), result=result)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
   result = None
   if request.method == 'POST':
      value = float(request.form['value'])
      from_unit = request.form['from_unit']
      to_unit = request.form['to_unit']
      result = convert_temperature(value, from_unit, to_unit)
   return render_template('temperature.html', result=result)

def convert_temperature(value, from_unit, to_unit):
   if from_unit == to_unit:
      return value
   # Convert to Celsius first
   if from_unit == 'Fahrenheit':
      value = (value - 32) * 5/9
   elif from_unit == 'Kelvin':
      value -= 273.15

   # Convert from Celsius to target
   if to_unit == 'Fahrenheit':
      return (value * 9/5) + 32
   elif to_unit == 'Kelvin':
      return value + 273.15
   return value

if __name__ == '__main__':
   app.run(debug=True)
