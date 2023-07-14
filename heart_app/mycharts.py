
from plotly.offline import plot
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

def scatter(dflastdate):
    # df.dropna(subset='continent',inplace=True)
    # dflastdate=df[(df['date'].str[-2:]=='07')]

    dflastdate=dflastdate.groupby(['continent','date']).sum().reset_index()
    scatter = px.scatter(dflastdate, x="date", y="total_cases", color="continent",
                  hover_data=['total_deaths','total_vaccinations'], size='total_deaths')
    scatter.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(scatter,output_type='div')
    return plt_div


def histogram1(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[(df['date'].str[-2:]=='07')]

    dflastdate=dflastdate.groupby(['continent','date']).sum().reset_index()
    histogram=px.histogram(df, x="continent",y="new_cases",color='location')
    histogram.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div= plot(histogram, output_type='div')
    return plt_div

def bargraphtop5(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[df['date']=='2023-06-07']
    top5countrydata=pd.DataFrame()
    for cont in dflastdate.continent.unique():
        dftmp=dflastdate[dflastdate['continent']==cont]
        print(cont)
        dftmp=dftmp.sort_values(ascending=False,by=['total_cases']).head(5)
        top5countrydata=top5countrydata.append(dftmp)
    barchart=px.bar(top5countrydata,y="continent",x="total_cases",color="location",orientation='h',hover_data=['total_cases','total_deaths'],barmode='group')
    barchart.update_traces(width=.7)
    barchart.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div= plot(barchart, output_type='div')
    return plt_div

def sunburst1(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[df['date']=='2023-06-07']
    sun = px.sunburst(dflastdate, path=['continent', 'location'], values='total_cases',title="TOTAL CASES",color_discrete_sequence = ['blue'])
    sun.update_traces(textinfo="label+percent parent")
    sun.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(sun,output_type='div')
    return plt_div

def sunburst2(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[df['date']=='2023-06-07']
    sun = px.sunburst(dflastdate, 
                    path=['continent', 'location'], 
                    values='total_deaths',
                    title="TOTAL DEATHS",
                    color_discrete_sequence = ['red'])
    sun.update_traces(textinfo="label+percent parent")
    sun.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(sun,output_type='div')
    return plt_div

def sunburst3(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[df['date']=='2023-06-07']
    sun = px.sunburst(dflastdate, 
                    path=['continent', 'location'], 
                    values='population',
                    title="TOTAL POPULATION",
                    color_discrete_sequence = ['green'])
    sun.update_traces(textinfo="label+percent parent")
    sun.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(sun,output_type='div')
    return plt_div

def line1(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[(df['date'].str[-2:]=='07')]

    dflastdate=dflastdate.groupby(['continent','date']).sum().reset_index()
    line = px.line(dflastdate, x="date", y="new_cases", color='continent')
    line.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        height=250,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(line,output_type='div')
    return plt_div

def line2(df):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[(df['date'].str[-2:]=='07')]

    dflastdate=dflastdate.groupby(['continent','date']).sum().reset_index()
    line = px.line(dflastdate, x="date", y="positive_rate", color='continent')
    line.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        height=250,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(line,output_type='div')
    return plt_div
    



    #country graph
def con_line1(dfind):
    # df.dropna(subset='continent',inplace=True)
    # dfind=df[(df['location'].str.lower()==sel_con.lower()) & (df['date'].str[-2:]=='01')]

    line = px.line(dfind, x="date", y="total_cases")
    line.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
            },
            margin = dict(t=26, l=5, r=5, b=5),
            font_family="Comic Sans MS",
            font_color="white",
            height=250,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False))
    line.update_traces(line_color='pink')
    plt_div=plot(line,output_type='div')
    
    return plt_div

def con_line2(dfind):
    # df.dropna(subset='continent',inplace=True)
    # dfind=df[(df['location'].str.lower()==sel_con.lower()) & (df['date'].str[-2:]=='01')]

    line = px.line(dfind, x="date", y="new_cases")
    line.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
            },
            margin = dict(t=26, l=5, r=5, b=5),
            font_family="Comic Sans MS",
            font_color="white",
            height=250,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False))
    line.update_traces(line_color='yellow')
    plt_div=plot(line,output_type='div')
    
    return plt_div


def con_line3(dfind):
    # df.dropna(subset='continent',inplace=True)
    # dfind=df[(df['location'].str.lower()==sel_con.lower()) & (df['date'].str[-2:]=='07')]

    line = px.line(dfind, x="date", y="total_vaccinations")
    line.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
            },
            margin = dict(t=26, l=5, r=5, b=5),
            font_family="Comic Sans MS",
            font_color="white",
            height=250,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False))
    line.update_traces(line_color='green')
    plt_div=plot(line,output_type='div')
    
    return plt_div

def con_line4(dfind):
    # df.dropna(subset='continent',inplace=True)
    # dfind=df[(df['location'].str.lower()==sel_con.lower()) & (df['date'].str[-2:]=='01')]

    line = px.line(dfind, x="date", y="total_deaths")
    line.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
            },
            
            margin = dict(t=26, l=5, r=5, b=5),
            font_family="Comic Sans MS",
            font_color="white",
            height=250,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False))
    line.update_traces(line_color='red')
    plt_div=plot(line,output_type='div')
    return plt_div


def sunburst_con(df,sel_con):
    df.dropna(subset='continent',inplace=True)
    selected_continent=df[df['location'].str.lower()==sel_con.lower()]['continent'].iloc[0]
    dflastdate=df[(df['continent']==selected_continent) & (df['date']=='2023-06-07')]
    sun = px.sunburst(dflastdate, 
                    path=['continent', 'location'], 
                    values='population',
                    title="TOTAL POPULATION",
                    color_discrete_sequence = ['blue'])
    sun.update_traces(textinfo="label+percent parent")
    sun.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        margin = dict(t=26, l=5, r=5, b=5),
        font_family="Comic Sans MS",
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div=plot(sun,output_type='div')
    return plt_div



def bargraphtop(df,sel_con):
    df.dropna(subset='continent',inplace=True)
    dflastdate=df[df['date'].str[-5:]=='12-31']
    dflastdate2=df[df['date']=='2023-03-01']
    my_current_country=sel_con
    top5_countries_list=['United States','China','India','France','Germany']
    top_5_country_data=dflastdate[dflastdate['location'].isin(top5_countries_list)]
    top_5_country_data=top_5_country_data.append(dflastdate2[dflastdate2['location'].isin(top5_countries_list)])
    top_5_country_data['year']=top_5_country_data['date'].str[:4]
    my_country_data=dflastdate2[dflastdate2['location']==my_current_country]
    my_country_data=my_country_data.append(dflastdate[dflastdate['location']==my_current_country])
    my_country_data['year']=my_country_data['date'].str[:4]
    my_country_data=my_country_data.sort_values(by=['total_cases'])
    fig=px.bar(top_5_country_data[['location','total_cases','year']], x="year", y="total_cases",
                color="location", hover_data=['total_cases'],
                barmode = 'group')
    fig.add_scatter(x=my_country_data["year"],y=my_country_data["total_cases"],name=my_current_country)
   


    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0.300)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0.300)',
        },
        font_family="Comic Sans MS",
        title='COMPARISON',
        title_x=0.5,
        font_color="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False))
    plt_div= plot(fig, output_type='div')
    return plt_div