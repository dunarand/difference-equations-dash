# Difference Equations Dashboard

## Overview

The aim of this project was creating interactive visuals of difference models
with ease.

![](https://github.com/user-attachments/assets/23e06cb2-60b7-48c0-906f-9828c6bf78b7)

## Getting Started

Ensure you have the following:

- Python 3.7+
- pip

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dunarand/difference-equations-dash.git
    cd difference-equations-dash
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Navigate to the project directory:
    ```sh
    cd difference-equations-dash
    ```
2. Run the application:
    ```sh
    python dash_app.py
    ```
3. Open a web browser and go to `http://127.0.0.1:8050/`.

### What are Difference Models

A difference equation is a relation that describes the change in a variable over time.
We use difference equations when the time variable is discrete as opposed to continuous
in the case of differential equations. A difference equation is used to model a problem
that features a discrete time change. For example, to model the remaining debt of a loan
which has a certain percentage of interest per month, we use difference equations.

A difference equation can be stated as follows:

$$
\begin{aligned}
    a_{n+1} &= r a_n + b \\
    a_0 &= c
\end{aligned}
$$

where $c \in \mathbb{R}$ is a constant, $r \in \mathbb{R}$ is a nonzero constant for
rate of change, and $b \in \mathbb{R}$ is a constant. Then,

$$
\Delta a_n = a_{n+1} - a_n
$$

For example, a loan of $10,000 with a monthly interest of 1% and a payment of $110 can
be modeled as follows:

$$
\begin{aligned}
    a_{n+1} &= 1.01 \cdot a_n - 110,\ a_0 = 10000 \\
    \Delta a_n &= (1.01 \cdot a_n - 110) - a_n \\
    &= 0.01 \cdot a_n - 110
\end{aligned}
$$

## How to Use

1. **Adding a sequence:** Simply set the following parameters
    - $a_0$: Initial value
    - $r$: Rate of change
    - $b$: Additive constant
    - $n$-Start: Starting index of the sequence
    - $n$-Stop: Ending index of the sequence
    All of the fields are optional and can be left blank or set to 0.
2. **Adding multiple sequences:** To add multiple sequences to the graph, first set the
    parameters of the first sequence. Then, click the "New Sequence" button. Repeat this
    process for all the sequences you want to add.
3. **Fixing parameters:** Fix $a_0$, Fix $r$, and Fix $b$ checkboxes are used to fix
    these values so that when adding multiple sequences, fixed parameters will not be
    reset after clicking new sequences button.
4. **Equilibrium Lines**: "Toggle Equilibrium Lines" button is used to toggle the
    visibility of the equilibrium lines on the graph.
5. **Current Sequence**: "Toggle Current Sequence" button is used to toggle the
    visibility of the current sequence on the graph.
6. **Graph Customization**: The graph can be customized using the following fields:
    - Graph Title (accepts LaTeX)
    - X-axis Label (accepts LaTeX)
    - Y-axis Label (accepts LaTeX)
    - X-axis Limits: Starting and ending values for the x-axis
    - Y-axis Limits: Starting and ending values for the y-axis
7. **Interactive Graph**: The plot is interactive. The following features are supported:
    - Zooming
    - Panning
    - Hovering over points to display their values
    - Selecting a region to highlight the values in that region
    - Hiding selected plots
    - Resetting the graph to its initial state
    - Saving the graph as an image
8. **Reset Button**: Reset button defaults all input fields and clears the graph.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
