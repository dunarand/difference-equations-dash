import plotly.graph_objects as go
from dash import Dash, dcc, html, callback_context
from dash.dependencies import Input, Output, State

from difference_model import DifferenceModel

app = Dash(__name__)

sequences = []
SHOW_CURRENT_SEQUENCE = True

app.layout = html.Div(
    children=[
        html.H1(
            children='Difference Models',
            style={
                'color': '#303030',
                'font-family': 'Lato, sans-serif',
                'font-size': '36px',
                'text-align': 'center',
                'margin-bottom': '20px',
                'margin-top': '-3px'
            }
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Markdown(children=r'$a_0$: ', mathjax=True),
                        dcc.Input(
                            id='input-a0',
                            type='number',
                            value=None,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                ),
                html.Div(
                    children=[
                        dcc.Markdown(children=r'$r$: ', mathjax=True),
                        dcc.Input(
                            id='input-r',
                            type='number',
                            value=None,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                ),
                html.Div(
                    children=[
                        dcc.Markdown(children=r'$b$: ', mathjax=True),
                        dcc.Input(
                            id='input-b',
                            type='number',
                            value=None,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                ),
                html.Div(
                    children=[
                        dcc.Markdown(children=r'$n$-Start: ', mathjax=True),
                        dcc.Input(
                            id='input-start',
                            type='number',
                            value=0,
                            min=0,
                            step=1,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                ),
                html.Div(
                    children=[
                        dcc.Markdown(children=r'$n$-Stop: ', mathjax=True),
                        dcc.Input(
                            id='input-stop',
                            type='number',
                            value=24,
                            min=0,
                            step=1,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                ),
            ],
            className='input-container'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Checklist(
                            options=[
                                {'label': 'Fix a0', 'value': 'keep'}
                            ],
                            value=[],
                            id='keep-a0-checkbox',
                            style={'display': 'inline-block', 'margin-right': '20px'}
                        ),
                        dcc.Checklist(
                            options=[
                                {'label': 'Fix r', 'value': 'keep'}
                            ],
                            value=[],
                            id='keep-r-checkbox',
                            style={'display': 'inline-block', 'margin-right': '20px'}
                        ),
                        dcc.Checklist(
                            options=[
                                {'label': 'Fix b', 'value': 'keep'}
                            ],
                            value=[],
                            id='keep-b-checkbox',
                            style={'display': 'inline-block', 'margin-right': '20px'}
                        ),
                    ],
                    style={'display': 'flex', 'align-items': 'center'},
                    className='input-label'
                ),
            ],
            className='input-container'
        ),
        html.Div(
            id='latex-output',
            children=dcc.Markdown(
                id='latex-display',
                mathjax=True
            ),
            className='latex-field'
        ),
        html.Div(
            children=[
                html.Button(
                    'New Sequence',
                    id='new-sequence-button',
                    n_clicks=0,
                    className='new-sequence-button'
                ),
                html.Button(
                    'Reset',
                    id='reset-button',
                    n_clicks=0,
                    className='reset-button'
                ),
                html.Button(
                    'Toggle Equilibrium Lines',
                    id='toggle-equilibrium-button',
                    n_clicks=0,
                    className='toggle-equilibrium-button'
                ),
                html.Button(
                    'Toggle Current Sequence',
                    id='toggle-current-sequence-button',
                    n_clicks=0,
                    className='toggle-current-sequence-button'
                ),
            ],
            style={
                'text-align': 'center'
            }
        ),
        dcc.Graph(id='sequence-graph', mathjax=True, className='graph-container'),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Markdown('Graph Title: '),
                        dcc.Input(
                            id='graph-title',
                            type='text',
                            value=r'$\text{Difference Models Sequences}$',
                            className='string-input-label'
                        )
                    ],
                    className='input-label'
                ),
                html.Div(
                    children=[
                        dcc.Markdown('X-axis Label: '),
                        dcc.Input(
                            id='x-axis-label',
                            type='text',
                            value=r'$\text{Iterations } (n)$',
                            className='string-input-label'
                        )
                    ],
                    className='input-label'
                ),
                html.Div(
                    children=[
                        dcc.Markdown('Y-axis Label: '),
                        dcc.Input(
                            id='y-axis-label',
                            type='text',
                            value=r'$\text{Values } (a_n)$',
                            className='string-input-label'
                        )
                    ],
                    className='input-label'
                )
            ],
            className='input-container'
        ),
        html.Div(children=[dcc.Markdown('X-axis Limits', className='input-label')],
                 className='input-container'),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Markdown('Min: ', style={'margin-left': '8px', 'margin-right': '8px'}),
                        dcc.Input(
                            id='xaxis-min',
                            type='number',
                            value=None,
                            className='numeric-input'
                        ),
                        dcc.Markdown('Max: ', style={'margin-left': '8px', 'margin-right': '8px'}),
                        dcc.Input(
                            id='xaxis-max',
                            type='number',
                            value=None,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                )
            ],
            className='input-container'
        ),
        html.Div(children=[dcc.Markdown('Y-axis Limits', className='input-label')],
                 className='input-container'),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Markdown('Min: ', style={'margin-left': '8px', 'margin-right': '8px'}),
                        dcc.Input(
                            id='yaxis-min',
                            type='number',
                            value=None,
                            className='numeric-input'
                        ),
                        dcc.Markdown('Max: ', style={'margin-left': '8px', 'margin-right': '8px'}),
                        dcc.Input(
                            id='yaxis-max',
                            type='number',
                            value=None,
                            className='numeric-input'
                        )
                    ],
                    className='input-label'
                )
            ],
            className='input-container'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Markdown(
                            children=[
                                r'''
                                <div class='markdown-header'>
                                    <strong>What are Difference Models</strong>
                                </div>

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

                                <div class='markdown-header'>
                                    <strong>How to Use</strong>
                                </div>

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

                                <div class='markdown-header'>
                                    <strong>Author: </strong><a href="https://github.com/dunarand">dunarand</a><br/>
                                    <strong> Source Code: </strong><a href="https://github.com/dunarand/difference-equations-dash">GitHub</a>
                                </div>
                                '''
                            ],
                            dangerously_allow_html=True,
                            mathjax=True,
                            className='markdown-text'
                        )
                    ],
                    className='markdown-container'
                )
            ],
            className='markdown-container-parent'
        )
    ],
    style={
        'max-width': '85%',
        'margin': '0 auto',
        'height': '100vh',
        'padding': '20px',
    }
)

def plot_sequence(fig, a0, r, b, start, stop, show_equilibrium):
    model = DifferenceModel(a0, r, b)
    data = model.generate_data(start, stop)

    a0 = a0 if a0 is not None else 0
    r = r if r is not None else 0
    b = b if b is not None else 0

    fig.add_trace(go.Scatter(
        x=data['n'],
        y=data['a_n'],
        mode='lines',
        name=fr'$a_0={a0}, r={r}, b={b}$',
        hovertemplate='n: %{x}<br>a_n: %{y}',
        showlegend=True
    ))

    if 'show' in show_equilibrium:
        eq_value = model.equilibrium()
        if eq_value is not None:
            eq_value = round(eq_value, 3)
        if b >= 0:
            eqn = fr'${r}\cdot a_n + {b} \Rightarrow a={eq_value}$'
        else:
            eqn = fr'${r}\cdot a_n {b} \Rightarrow a={eq_value}$'
        fig.add_trace(go.Scatter(
            x=data['n'],
            y=[eq_value] * len(data),
            opacity=0.75,
            mode='lines',
            line=dict(dash='dash', color='black', width=1),
            name=eqn,
            showlegend=True
        ))
    return fig

@app.callback(
    Output('latex-display', 'children'),
    [Input('input-a0', 'value'),
     Input('input-r', 'value'),
     Input('input-b', 'value')]
)
def update_latex(a0, r, b):
    a0 = a0 if a0 is not None else 0
    r = r if r is not None else 0
    b = b if b is not None else 0

    if b >= 0:
        latex_str = rf'$a_{{n + 1}} = {r} \cdot a_n + {b},\ a_0 = {a0}$'
    else:
        latex_str = rf'$a_{{n + 1}} = {r} \cdot a_n {b},\ a_0 = {a0}$'

    return latex_str

@app.callback(
     Output('sequence-graph', 'figure'),
    [Input('input-a0', 'value'),
     Input('input-r', 'value'),
     Input('input-b', 'value'),
     Input('input-start', 'value'),
     Input('input-stop', 'value'),
     Input('new-sequence-button', 'n_clicks'),
     Input('reset-button', 'n_clicks'),
     Input('toggle-equilibrium-button', 'n_clicks'),
     Input('toggle-current-sequence-button', 'n_clicks'),
     Input('graph-title', 'value'),
     Input('x-axis-label', 'value'),
     Input('y-axis-label', 'value'),
     Input('xaxis-min', 'value'),
     Input('xaxis-max', 'value'),
     Input('yaxis-min', 'value'),
     Input('yaxis-max', 'value')]
)
def update_graph(a0, r, b, start, stop, new_seq_clicks, reset_clicks, toggle_equilibrium_clicks,
                           toggle_current_seq_clicks, graph_title, x_axis_label, y_axis_label,
                           xaxis_min, xaxis_max, yaxis_min, yaxis_max):
    ctx = callback_context

    button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    fig = go.Figure()

    if toggle_equilibrium_clicks % 2 == 0:
        equilibrium_checkbox = ['show']
    else:
        equilibrium_checkbox = []

    global SHOW_CURRENT_SEQUENCE
    if button_id == 'toggle-current-sequence-button':
        SHOW_CURRENT_SEQUENCE = not SHOW_CURRENT_SEQUENCE

    a0 = a0 if a0 is not None else 0
    r = r if r is not None else 0
    b = b if b is not None else 0
    start = start if start is not None else 0
    stop = stop if stop is not None else 0

    for seq in sequences:
        seq_a0, seq_r, seq_b, seq_start, seq_stop = seq
        fig = plot_sequence(fig, seq_a0, seq_r, seq_b, start, stop, equilibrium_checkbox)

    if SHOW_CURRENT_SEQUENCE:
        fig = plot_sequence(fig, a0, r, b, start, stop, equilibrium_checkbox)

    xaxis_range = [xaxis_min, xaxis_max] if xaxis_min is not None or xaxis_max is not None else None
    yaxis_range = [yaxis_min, yaxis_max] if yaxis_min is not None or yaxis_max is not None else None

    fig.update_layout(
        paper_bgcolor='#f7f7f7',
        title={
            'text': graph_title,
            'font': {
                'family': 'Open Sans, sans-serif',
                'color': '#333333',
                'size': 24
            },
            'x': 0.5
        },
        xaxis_title={
            'text': r'{}'.format(x_axis_label),
            'font': {
                'family': 'Open Sans, sans-serif',
                'color': '#333333',
                'size': 18
            },
        },
        yaxis_title={
            'text': r'{}'.format(y_axis_label),
            'font': {
                'family': 'Open Sans, sans-serif',
                'color': '#333333',
                'size': 18
            },
        },
        legend={
            'font': {
                'size': 16
            }
        },
        showlegend=True,
        xaxis=dict(range=xaxis_range),
        yaxis=dict(range=yaxis_range)
    )
    return fig

@app.callback(
    [Output('input-a0', 'value'),
     Output('input-r', 'value'),
     Output('input-b', 'value'),
     Output('input-start', 'value'),
     Output('input-stop', 'value'),
     Output('keep-a0-checkbox', 'value'),
     Output('keep-r-checkbox', 'value'),
     Output('keep-b-checkbox', 'value'),
     Output('graph-title', 'value'),
     Output('x-axis-label', 'value'),
     Output('y-axis-label', 'value'),
     Output('xaxis-min', 'value'),
     Output('xaxis-max', 'value'),
     Output('yaxis-min', 'value'),
     Output('yaxis-max', 'value')],
    [Input('new-sequence-button', 'n_clicks'),
     Input('reset-button', 'n_clicks')],
    [State('input-a0', 'value'),
     State('input-r', 'value'),
     State('input-b', 'value'),
     State('input-start', 'value'),
     State('input-stop', 'value'),
     State('keep-a0-checkbox', 'value'),
     State('keep-r-checkbox', 'value'),
     State('keep-b-checkbox', 'value'),
     State('graph-title', 'value'),
     State('x-axis-label', 'value'),
     State('y-axis-label', 'value'),
     State('xaxis-min', 'value'),
     State('xaxis-max', 'value'),
     State('yaxis-min', 'value'),
     State('yaxis-max', 'value')]
)
def reset_inputs(new_seq_clicks, reset_clicks, a0, r, b, start, stop, keep_a0, keep_r, keep_b, graph_title,
                 x_axis_label, y_axis_label, xaxis_min, xaxis_max, yaxis_min, yaxis_max):
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

    global sequences

    new_a0 = None if 'keep' not in keep_a0 else a0
    new_r = None if 'keep' not in keep_r else r
    new_b = None if 'keep' not in keep_b else b
    new_start = start
    new_stop = stop

    if button_id == 'new-sequence-button':
        if a0 is not None and r is not None and start is not None and stop is not None:
            sequences.append((a0, r, b, start, stop))
    if button_id == 'reset-button':
        sequences = []
        new_a0, new_r, new_b, new_start, new_stop = None, None, None, 0, 24
        keep_a0, keep_r, keep_b = [], [], []
        graph_title = r'$\text{Difference Models Sequences}$'
        x_axis_label = r'$\text{Iterations } (n)$'
        y_axis_label = r'$\text{Values } (a_n)$'
        xaxis_min, xaxis_max, yaxis_min, yaxis_max = None, None, None, None

    return (new_a0, new_r, new_b, new_start, new_stop, keep_a0, keep_r, keep_b, graph_title,
            x_axis_label, y_axis_label, xaxis_min, xaxis_max, yaxis_min, yaxis_max)

if __name__ == '__main__':
    app.run_server(debug=True)
