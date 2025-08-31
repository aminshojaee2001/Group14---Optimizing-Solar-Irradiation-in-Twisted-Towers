from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

app = Flask(__name__)

# Load Excel data
EXCEL_FILE = "data/full data set.xlsx"
df = pd.read_excel(EXCEL_FILE)
df = df[['city', 'L1', 'rotation', 'NoFloor', 'irradiation']]

# List of cities and shapes
available_cities = sorted(df['city'].unique())
shapes = ["pentagon", "square", "hexagon"]

# Shape correction multipliers
shape_factors = {
    "pentagon": 1.00,
    "square": 0.92,
    "hexagon": 1.08
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        selected_city = request.form["city"]
        selected_shape = request.form["shape"]
        l1 = float(request.form["l1"])
        rotation = float(request.form["rotation"])
        floors = int(request.form["floors"])

        # Filter for selected city
        city_data = df[df['city'] == selected_city]

        if city_data.empty:
            result_text = "⚠️ No data available for the selected city."
        else:
            points = city_data[["L1", "rotation", "NoFloor"]].values
            values = city_data["irradiation"].values
            query_point = np.array([[l1, rotation, floors]])

            # Interpolate for pentagon shape
            interpolated_result = griddata(points, values, query_point, method='linear')

            if interpolated_result[0] is not None:
                adjusted_result = interpolated_result[0] * shape_factors[selected_shape]
                result_text = f"🔆 Estimated irradiation: {adjusted_result:.2f} kWh/m²"
            else:
                result_text = "⚠️ Interpolation failed. Input may be out of range."

        return render_template(
            "results.html",
            city=selected_city,
            shape=selected_shape,
            l1=l1,
            rotation=rotation,
            floors=floors,
            result=result_text
        )

    return render_template("index.html", cities=available_cities, shapes=shapes)

if __name__ == "__main__":
    app.run(debug=True)
