import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd
from pandas.io.formats.format import return_docstring
from PIL import Image

#------------------------------------------Server------------------------------------------------------------
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
df = pd.DataFrame({
    'Name': ['Смертноть', 'Рождаемость', 'Браки', 'Разводы'],
    'Score': [85, 92, 78, 88]
})
#-------------------------------------------Data-------------------------------------------------------------
header_height, footer_height = "5rem", "8rem"
sidebar_width, adbar_width = "12rem", "12rem"
pil_image = Image.open("images/gerb.png")
pil_image2 = Image.open("images/logo.png")
pil_image3 = Image.open("images/map.png")
pil_image4 = Image.open("images/fon_top.png")
pil_image5 = Image.open("images/bord.jpg")


#-------------------------------------------Styles----------------------------------------------------------
span_style = {
    'display':'block',
    'font-size': '12px',
    'margin-top': '5px',
    'font-weight': '700',
    'color':' #fff',
}

pp={
    'position': 'fixed',
    'top': '600px',
    'font-size': '20px',
    'left': '200px',
}

pp2={
    'position': 'fixed',
    'top': '800px',
    'font-size': '20px',
    'left': '200px',
}

page1_P ={
    'position': 'fixed',
    'right': '700px',
    'left': '1300px',
    'font-size': '32px',
}

page3_P ={
    'position': 'fixed',
    'right': '200px',
    'left': '300px',
    'font-size': '20px',
}

p_style = {
    'font-size': '22px',
    'font-weight': '800',
    'line-height': '1.1',
    'color': '#fff',
    'margin-top': '10px',
}

pos_P = {
    'position': 'fixed',
    'left': '300px',
    'font-size': '12px',
}

pos_P2 = {
    'position': 'fixed',
    'left': '280px',
    'margin': '20px',
    'font-size': '12px',
}

pos_P3 = {
    'position': 'fixed',
    'left': '260px',
    'margin': '40px',
    'font-size': '12px',
}

pos_P4 = {
    'position': 'fixed',
    'left': '240px',
    'margin': '60px',
    'font-size': '12px',
}

imgs = {
    'width': '150px',
    'height': 'auto',
    'border-radius': '15px',
    'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.3)',
}

imgs_2 = {
    'width': '150px',
    'height': 'auto',
    'border-radius': '15px',
    'margin-top': '20px',
}

imgs_3 = {
    'width': '800px',
    "position": "fixed",
    "left": '200px',
    
}

imgs_5 = {
    'width': '680px',
    'height': '710px',
    'border-radius': '10px',
    'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.3)',
    "position": "fixed",
    "left": '1030px',

}

imgs_4 = {
    'width': '1200px',
    "position": "fixed",
    "left": '-450px',
    'bottom': 0,
}

imgs_6 = {
    'position': 'fixed',
    'top': '600px',
    'left': '200px',
    'width': '805px',
    'height': '215px',
    'border-radius': '10px',
    'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.3)',
}

HEADER_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "right": 0,
    "height": header_height,
    "padding": "2rem 1rem",
    "background-color": "#222222",
    'color': 'white',
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": header_height,
    "left": 0,
    "bottom": footer_height,
    "width": sidebar_width,
    "padding": "1rem 1rem",
    "background-color": "#474242",
    'color': 'white',
}

ADBAR_STYLE = {
    "position": "fixed",
    "top": header_height,
    "right": 0,
    "bottom": footer_height,
    "width": adbar_width,
    "padding": "1rem 1rem",
    "background-color": "#1a408c",
}

FOOTER_STYLE = {
    "position": "fixed",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": footer_height,
    "padding": "1rem 1rem",
    "background-color": "#222222",
    'color': 'white',
    'border': 'none',
}

CONTENT_STYLE = {
    "margin-top": header_height,
    "margin-left": sidebar_width,
    "margin-right": adbar_width,
    "margin-bottom": footer_height,
    "padding": "1rem 20rem",
}

graf_position = {
    'width': '600px',
    'position': 'fixed',
    'right': '700px',
    'left': '950px',
    'margin': "150px",
}

H2_position = {
    'position': 'fixed',
    'right': '700px',
    'left': '1000px',
    'margin': "60px",
    'font-size': '26px',
}

H2_position_2 = {
    'position': 'fixed',
    'right': '300px',
    'left': '300px',
    'margin': "60px",
    'font-size': '16px',
}

dropdown_s = {
    'width': '400px',

    'position': 'fixed',

    'left': '1220px',
    'top':'160px',
}

dropdown_s2 = {
    'width': '400px',
    'position': 'fixed',

    'left': '620px',
    'top':'160px',
}
fdivs1 = {
    'font-size': '15px',
    'text-align': 'center',
    'padding': '85px',
}

substyle ={
    'position': 'fixed',
    'left': '200px',
    'top':'170px',
}

sub_bord ={
    'position': 'fixed',
    'top': '170px',
    'left': '200px',
    'width': '1000px',
    'height': '600px',
    'border-radius': '10px',
    'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.3)',
}

anstyle = {
    'font-size': '22px',
    'position': 'fixed',
    'left': '1300px',
    'top': '190px',
}

ans_bord = {
    'position': 'fixed',
    'top': '270px',
    'left': '1230px',
    'width': '470px',
    'height': '500px',
    'border-radius': '1px',
    'box-shadow': '0px 4px 8px rgba(0, 0, 0, 0.3)',
}

txt ={
    'padding-right': '1000px',

}

txt2 ={
    'padding-right': '200px',
    'position': 'fixed',
    'top': '270px',

}
#------------------------------------main-layout-code----------------------------------------------------
header = html.Div([
    html.H2("Мониторинг")], style=HEADER_STYLE
)

fdivs = [html.Img(src=pil_image4, style= imgs_4),
             html.P('Тел: 8 800 234-77-20', style= pos_P), 
             html.P('Email: priem@uwc-i.ru', style= pos_P2), 
             html.P('Москва, Ленинский проспект, д. 1/2, корп. 1', style= pos_P3), 
             html.P('Москва, 1-й Басманный переулок, д. 3, стр. 1', style= pos_P4),
         html.H2(" Copyright Awesome. All rights Reserved.", 
                 style=fdivs1)]

footer = html.Div(fdivs, style=FOOTER_STYLE)

adbar = html.Div([
    html.H2(""), html.Img(src=pil_image, style=imgs), html.Img(src=pil_image2, style=imgs_2), html.P("Университет Мировых Цивилизаций", style=p_style),
    html.Span("им. В.В. Жириновского", style=span_style)], 
    style=ADBAR_STYLE
)

sidebar = html.Div([
    html.H2("Меню"),
    html.Hr(),
    dbc.Nav([
            dbc.NavLink("Аналитика", href="/page-1", id="page-1-link"),
            dbc.NavLink("Управленческое решение", href="/page-2", id="page-2-link"),
            dbc.NavLink("Статистические данные", href="/page-3", id="page-3-link")
        ], vertical=True, pills=True,
    )],
    style=SIDEBAR_STYLE
)

cdivs = [html.H2(""),
         html.Div(id="page-content")]


content = html.Div(cdivs, style=CONTENT_STYLE)

dropdown = html.Div([
        html.H3('Выберите Регион:', style=H2_position),
        dcc.Dropdown(
            id='demo_drop',
            options=[
                {'label': 'Москва', 'value': '1'},
                {'label': 'Санкт-Петербург', 'value': '2'},
                {'label': 'Краснодарский Край', 'value': '3'}
            ],
            value='1', style=dropdown_s
        ),
    dcc.Graph(id='graf', style=graf_position), html.P('Описание:', style=pp, id='opisan')
])

dropdown2 = html.Div([
        dcc.Dropdown(
                id='drop',
                options=[
                         {'label': 'Москва', 'value': '1'},
                         {'label': 'Санкт-Петербург', 'value': '2'},
                         {'label': 'Краснодар', 'value': '3'}
                ], value='1',
            style={"width": "75%"}
        ), dcc.Graph(id='graph',style=substyle), html.P('', style=pp2, id='answer')
])

dropdown3 = html.Div([
        html.H3('Выберите Регион:', style=H2_position_2),
        dcc.Dropdown(
            id='demo_drop',
            options=[
                {'label': 'Москва', 'value': '1'},
                {'label': 'Санкт-Петербург', 'value': '2'},
                {'label': 'Краснодарский Край', 'value': '3'}
            ],
            value='1', style=dropdown_s2
        )
])

app.layout = html.Div([dcc.Location(id="url"),
                       header, sidebar, adbar, content, footer])

#------------------------------------------Callbacks-and-Funcs------------------------------------------------------
#menu pages
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return (html.Img(src=pil_image3, style=imgs_3), html.Img(src=pil_image5, style=imgs_5), html.Img(src=pil_image5, style=imgs_6),
                html.P("Аналитика", style=page1_P), dropdown)
    elif pathname == "/page-2":
        return (html.Img(src=pil_image5, style=ans_bord),  html.Img(src=pil_image5, style=sub_bord), 
                html.P("", style=anstyle, id='answer2'), dropdown2)
    elif pathname == "/page-3":
        return (html.P("Форма для заргузки данных", style=page3_P), dropdown3)

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

#general info
@app.callback(
    Output(component_id='graf', component_property='figure'),
    [Input(component_id='demo_drop', component_property='value'),
     ]
)
def update_output(value):
    if value == '3':
        labels = ['Эмиграция', 'Браки', 'Разводы', 'Рождаемость', 'Смертность', 'Зарплата', 'Стоимость жилья']
        values = [2500, 1200, 670, 1001, 302, 400, 650]

    elif value == '2':
        labels = ['Эмиграция', 'Браки', 'Разводы', 'Рождаемость', 'Смертность']
        values = [4000, 2100, 589, 1889, 301]

    elif value == '1':
        labels = ['Эмиграция', 'Браки', 'Разводы', 'Рождаемость', 'Смертность']
        values = [5000, 2500, 429, 1890, 213]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=10,
                      marker=dict(line=dict(color='#000000', width=1)))
    return fig

#generl info description
@app.callback(
    Output(component_id='opisan', component_property='children'),
    [Input(component_id='demo_drop', component_property='value'),
     ]
)
def update_output_text(value):
    if value=='1':
        return html.P('Описание региона: Москва продолжает привлекать мигрантов из других регионов России и стран СНГ, что способствует увеличению численности населения. Однако, начиная с 2024 года, ожидается ежегодная естественная убыль населения на уровне от 20 до 37 тыс. человек, что связано с низким уровнем рождаемости и старением населения', 
                      style=txt)
    elif value=='2':
        return html.P('Описание региона: Санкт-Петербург также сталкивается с проблемой естественной убыли населения. В 2017 году уровень рождаемости в городе снизился на 10%, а естественный прирост уменьшился на 48%. Миграционный прирост населения в Санкт-Петербурге составляет около 63 тыс. человек в год, что частично компенсирует естественную убыль. ',
                      style=txt)
    elif value =='3':
        return html.P('Описание региона: Краснодар демонстрирует устойчивый рост населения, в том числе за счет миграции. Численность города увеличилась на 200 тыс. человек за год, что свидетельствует о высокой привлекательности города для переселенцев. Однако, по данным переписи 2021 года, население Краснодара составляет около 1,24 млн человек, что ниже оценок местных властей, предполагающих более высокие цифры.',
                      style=txt)
    
#data for page 2
@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='drop', component_property='value')]
)
def update_f(value):
    if value == '1':
        dfA = pd.DataFrame({
            "1": [250, 530, 300, 850, 400, 670, 750], "Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020]
        })

        dfB = pd.DataFrame({
            "Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "2": [430, 350, 518, 405, 320, 650, 700]
        })

        dfC = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "3": [600, 350, 450, 700, 550, 270, 410]
             })

        dfD = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "4": [250, 350, 450, 550, 350, 650, 250]
             })

        dfF = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "5": [250, 350, 450, 550, 350, 650, 250]
             })

        dfG = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "6": [250, 350, 450, 550, 350, 650, 250]
             })
    elif value == '2':
        dfA = pd.DataFrame({
            "1": [200, 500, 200, 800, 200, 570, 450], "Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020]
        })

        dfB = pd.DataFrame({
            "Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "2": [330, 250, 418, 305, 320, 650, 750]
        })

        dfC = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "3": [400, 250, 250, 600, 450, 170, 410]
             })

        dfD = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "4": [150, 250, 350, 550, 350, 350, 250]
             })

        dfF = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "5": [350, 350, 450, 750, 150, 650, 250]
             })

        dfG = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "6": [255, 359, 400, 150, 250, 650, 250]
             })
    elif value == '3':
        dfA = pd.DataFrame({
            "1": [50, 230, 100, 450, 400, 670, 750], "Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020]
        })

        dfB = pd.DataFrame({
            "Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "2": [230, 550, 518, 505, 420, 350, 700]
        })

        dfC = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "3": [100, 350, 450, 700, 550, 270, 410]
             })

        dfD = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "4": [250, 350, 450, 400, 350, 250, 250]
             })

        dfF = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "5": [50, 300, 450, 550, 350, 250, 120]
             })

        dfG = pd.DataFrame(
            {"Years": [2014, 2015, 2016, 2017, 2018, 2019, 2020], "6": [200, 300, 450, 550, 350, 600, 100]
             })
    fig = make_subplots(rows=3, cols=2, shared_yaxes=False,
                        subplot_titles=(
                            "Эмиграция", "Рождаемость", "Смертность", "Браки", 'Зарплата', 'Стоимость жилья'))
    fig.add_trace(go.Scatter(x=dfA["Years"], y=dfA["1"]), row=1, col=1)
    fig.add_trace(go.Scatter(x=dfB["Years"], y=dfB["2"]), row=1, col=2)
    fig.add_trace(go.Scatter(x=dfC["Years"], y=dfC["3"]), row=2, col=1)
    fig.add_trace(go.Scatter(x=dfD["Years"], y=dfD["4"]), row=2, col=2)
    fig.add_trace(go.Scatter(x=dfF["Years"], y=dfF["5"]), row=3, col=1)
    fig.add_trace(go.Scatter(x=dfG["Years"], y=dfG["6"]), row=3, col=2)
    fig.update_layout(height=600, width=1000, title_text="Показатели по годам и решения",showlegend=False)
    return fig

#answer
@app.callback(
    Output(component_id='answer2', component_property='children'),
    [Input(component_id='drop', component_property='value'),
     ]
)
def update_output_text2(value):
    if value == '1':
        return html.P('Решение для региона: ')
    elif value == '2':
        return html.P('Решение для региона: ')
    elif value == '3':
        return (html.P('Решение для региона: '), 
                html.P('Развитие инфраструктуры: Усовершенствование транспортной сети, улучшение жилищных условий, обеспечение доступности социальных услуг для всех категорий граждан.',
                       style=txt2))


if __name__ == "__main__":
    app.run_server(port=8888)