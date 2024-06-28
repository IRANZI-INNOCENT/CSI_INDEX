import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Function to calculate weighted score
def calculate_weighted_score(location, household_number, num_people, raw_scores):
    severity_weights = {
        'a': 1, 'b': 2, 'c': 2, 'd': 4, 'e': 3, 'f': 2,
        'g': 4, 'h': 1, 'i': 2, 'j': 2, 'k': 2, 'l': 4
    }
    total_score = sum(raw_scores[key] * severity_weights[key] for key in raw_scores)
    return {
        'Location': location,
        'Household Number': household_number,
        'Total Weighted Score': total_score
    }

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Expose the server variable for deployment

# Define the layout of the web app
app.layout = html.Div(style={'padding': '20px', 'background': '#ffeeff', 'maxWidth': '1200px', 'margin': '0 auto'}, children=[
    html.H1("Hunger Coping Strategies Index (CSI)", style={'textAlign': 'center', 'paddingBottom': '9px', 'fontWeight': 'bold', 'backgroundColor': 'hsl(0, 0%, 77%)', 'padding': '10px', 'color': 'hsl(235, 45%, 29%)', 'fontSize': 32}),
    html.Hr(style={'borderWidth': '8px', 'borderColor': 'hsl(240, 100%, 50%)'}),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Location", style={'fontWeight': 'bold'}),
                    dcc.Input(id='input-location', type='text', style={'width': '100%'})
                ]),
                style={'marginBottom': '10px', 'padding': '10px', 'background': 'hsl(159, 100%, 95%)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Household Number", style={'fontWeight': 'bold'}),
                    dcc.Input(id='input-household-number', type='text', style={'width': '100%'})
                ]),
                style={'marginBottom': '10px', 'padding': '10px', 'background': 'hsl(159, 100%, 95%)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Number of People in Family", style={'fontWeight': 'bold'}),
                    dcc.Input(id='input-num-people', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '10px', 'padding': '10px', 'background': 'hsl(159, 100%, 95%)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
    ], align='center'),
    html.H1("How many times did any of the following happen in your household (0-7)", style={'textAlign': 'center', 'fontWeight': 'bold', 'paddingBottom': '5px', 'backgroundColor': 'hsl(0, 0%, 77%)', 'padding': '5px', 'color': 'hsl(235, 45%, 29%)', 'fontSize': 22}),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Rely on less preferred and less expensive foods", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-a', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Borrow food, or rely on help from a friend or relative", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-b', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Purchase food on credit", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-c', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
    ], align='center'),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Gather wild food, hunt, or harvest immature crops", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-d', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Consume seed stock held for next season", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-e', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Send household members to eat elsewhere", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-f', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
    ], align='center'),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Send household members to beg", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-g', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Limit portion size at mealtime", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-h', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Restrict consumption by adults for small children to eat", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-i', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '5px', 'padding': '5px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
    ], align='center'),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Feed working members at the expense of non-working", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-j', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '0px', 'padding': '0px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Ration the money you have and buy prepared food", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-k', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '0px', 'padding': '0px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.Label("Skip entire days without eating", style={'fontWeight': 'bold', 'font-size': '12px'}),
                    dcc.Input(id='input-strategy-l', type='number', style={'width': '100%'})
                ]),
                style={'marginBottom': '0px', 'padding': '0px', 'background': 'hsla(0, 100%, 15%, 0.1)', 'width': '100%', 'height': '87px'}
            ),
            md=4
        ),
    ], align='center'),

    html.Br(),

    html.Div(id='output-container', style={'fontSize': '30px', 'fontWeight': 'bold', 'padding': '0px', 'textAlign': 'center'}),
])

# Define callback to calculate CSI score and update output
@app.callback(
    Output('output-container', 'children'),
    [
        Input('input-location', 'value'),
        Input('input-household-number', 'value'),
        Input('input-num-people', 'value'),
        Input('input-strategy-a', 'value'),
        Input('input-strategy-b', 'value'),
        Input('input-strategy-c', 'value'),
        Input('input-strategy-d', 'value'),
        Input('input-strategy-e', 'value'),
        Input('input-strategy-f', 'value'),
        Input('input-strategy-g', 'value'),
        Input('input-strategy-h', 'value'),
        Input('input-strategy-i', 'value'),
        Input('input-strategy-j', 'value'),
        Input('input-strategy-k', 'value'),
        Input('input-strategy-l', 'value'),
    ]
)
def update_output(location, household_number, num_people, score_a, score_b, score_c, score_d, score_e,
                 score_f, score_g, score_h, score_i, score_j, score_k, score_l):
    
    raw_scores = {
        'a': int(score_a) if score_a else 0,
        'b': int(score_b) if score_b else 0,
        'c': int(score_c) if score_c else 0,
        'd': int(score_d) if score_d else 0,
        'e': int(score_e) if score_e else 0,
        'f': int(score_f) if score_f else 0,
        'g': int(score_g) if score_g else 0,
        'h': int(score_h) if score_h else 0,
        'i': int(score_i) if score_i else 0,
        'j': int(score_j) if score_j else 0,
        'k': int(score_k) if score_k else 0,
        'l': int(score_l) if score_l else 0,
    }
    
    result = calculate_weighted_score(location, household_number, num_people, raw_scores)
    
    output_str = f"Location: {result['Location']}, Household Number: {result['Household Number']}, Total Weighted Score: {result['Total Weighted Score']}"
    html.Hr(style={'borderWidth': '0px', 'borderColor': 'hsl(240, 100%, 50%)'})
    
    return html.Div(output_str, style={'fontSize': '30px', 'fontWeight': 'bold', 'padding': '0px'}),


if __name__ == '__main__':
    app.run_server(debug=True)
