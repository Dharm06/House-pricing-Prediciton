import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from tkinter import *
from tkinter import messagebox
import numpy as np
import locale

# Set Indian locale for number formatting (this works for many systems)
try:
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')  # fallback

# ----------- Load and train model -----------

# Load dataset
data = pd.read_csv(r"C:\Users\dalak\OneDrive\Documents\ML\House Price Predition\indian_house_prices.csv")

# Encode 'Road_Touch' (Yes=1, No=0)
le = LabelEncoder()
data['Road_Touch'] = le.fit_transform(data['Road_Touch'])

# Features and target
X = data[['BHK', 'Area_sqft', 'Road_Touch']]
y = data['Price_Lakhs']

# Train model
model = LinearRegression()
model.fit(X, y)

# ----------- GUI with Tkinter -----------

def predict_price():
    try:
        bhk = int(entry_bhk.get())
        area = float(entry_area.get())
        road_touch = 1 if road_var.get() == "Yes" else 0

        input_data = np.array([[bhk, area, road_touch]])
        prediction = model.predict(input_data)[0]
        rupees = prediction * 100000  # Convert lakhs to rupees

        formatted_price = locale.format_string("%d", int(rupees), grouping=True)
        result_label.config(text=f"Predicted Price: ₹ {formatted_price}")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create window
root = Tk()
root.title("Indian House Price Predictor")
root.geometry("350x320")

# Title label
Label(root, text="🏠 Indian House Price Predictor", font=("Helvetica", 14, "bold")).pack(pady=10)

# BHK Input
Label(root, text="Enter BHK:").pack()
entry_bhk = Entry(root)
entry_bhk.pack()

# Area Input
Label(root, text="Enter Area (in sqft):").pack()
entry_area = Entry(root)
entry_area.pack()

# Road Touch Option
Label(root, text="Is it Road Touch Property?").pack()
road_var = StringVar(value="Yes")
OptionMenu(root, road_var, "Yes", "No").pack()

# Predict Button
Button(root, text="Predict Price", command=predict_price, bg="green", fg="white", padx=10, pady=5).pack(pady=15)

# Result Label
result_label = Label(root, text="", font=("Helvetica", 12, "bold"))
result_label.pack()

root.mainloop()
