import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Tanh Activation Function",
    layout="centered"
)

st.title("Hyperbolic Tangent (Tanh)")
st.write("This web application visualises the Tanh activation function.")


st.sidebar.header("Input Settings")

x_min = st.sidebar.slider("Minimum x value", -20.0, -1.0, -10.0)
x_max = st.sidebar.slider("Maximum x value", 1.0, 20.0, 10.0)
num_points = st.sidebar.slider("Number of points", 100, 1000, 400, step=50)


x = np.linspace(x_min, x_max, num_points)

st.write("**Formula:** Tanh(x) = (eˣ − e⁻ˣ) / (eˣ + e⁻ˣ)")
st.write(
    "**X-axis:** Input value to the neuron\n\n"
    "**Y-axis:** Output range between -1 and 1"
)

y = np.tanh(x)


fig, ax = plt.subplots()
ax.plot(x, y, color="red")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Activation Output")
ax.set_title("Tanh Activation Function")
ax.grid(True)

st.pyplot(fig)
