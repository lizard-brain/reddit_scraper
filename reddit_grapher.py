import pandas as pd
import plotly.graph_objects as go
import csv



def total_active(file):

    print('Plotting Active Users')
    
    fig = go.Figure(go.Scatter())


    with open(file, mode='r', newline='') as database_csv:
        
            database = csv.reader(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in database:
                sub_red = row[1]
                #print(sub_red)
                index = int(row[0])
                data_path = './data/' + row[0] + '_stats.csv'
                
                df = pd.read_csv(data_path)
                
                fig.add_trace(go.Scatter(x = df['localtime_human'], y = df['active'],
                      name=sub_red))
                
                sub_red = row[1]
                sub_red = sub_red.strip()
    fig.update_layout(title='Total Active', plot_bgcolor='rgb(230, 230,230)',showlegend=True)
    fig.show()


def percent_active(file):

    print('Plotting Percent Active')
    fig = go.Figure(go.Scatter())


    with open(file, mode='r', newline='') as database_csv:
        
            database = csv.reader(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in database:
                sub_red = row[1]
                #print(sub_red)
                index = int(row[0])
                data_path = './data/' + row[0] + '_stats.csv'
                
                df = pd.read_csv(data_path)
                
                fig.add_trace(go.Scatter(x = df['localtime_human'], y = df['percent'],
                      name=sub_red))
                
                sub_red = row[1]
                sub_red = sub_red.strip()
    title = file + 'Percent Active'           
    fig.update_layout(title=title, plot_bgcolor='rgb(230, 230,230)',showlegend=True)

    fig.show()


def plot(file):

    file = './plot_info/' + file
    total_active(file)
    percent_active(file)


plot('politics.csv')
plot('drugs.csv')
plot('Aus.csv')









