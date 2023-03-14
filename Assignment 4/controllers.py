import pandas as pd
import random
from models import read_classmate_data, write_classmate_data
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def process_data(form):
    df = read_classmate_data()
    new_data = {
        'Name': form.name.data,
        'No Shadow': int(form.no_shadow.data),
        'Pale Complexion': int(form.pale_complexion.data),
        'No Garlic': int(form.no_garlic.data)
    }
    df = df.append(new_data, ignore_index=True)
    write_classmate_data(df)

def threshold_based_vampire(df):
    df['Score'] = df['No Shadow'] * 4 + df['Pale Complexion'] * 3 + df['No Garlic'] * 3
    df['Vampire'] = df['Score'] > 6
    return df

def random_vampire(df):
    df['Vampire'] = df.apply(lambda x: bool(random.getrandbits(1)), axis=1)
    return df

def plot_data(method):
    df = read_classmate_data()
    if method == 'threshold':
        df = threshold_based_vampire(df)
    elif method == 'random':
        df = random_vampire(df)
   
import pandas as pd
import random
from models import read_classmate_data, write_classmate_data
import matplotlib.pyplot as plt

def process_data(form):
    df = read_classmate_data()
    new_data = {
        'Name': form.name.data,
        'No Shadow': int(form.no_shadow.data),
        'Pale Complexion': int(form.pale_complexion.data),
        'No Garlic': int(form.no_garlic.data)
    }
    df = df.append(new_data, ignore_index=True)
    write_classmate_data(df)

def threshold_based_vampire(df):
    df['Score'] = df['No Shadow'] * 4 + df['Pale Complexion'] * 3 + df['No Garlic'] * 3
    df['Vampire'] = df['Score'] > 6
    return df

def random_vampire(df):
    df['Vampire'] = df.apply(lambda x: bool(random.getrandbits(1)), axis=1)
    return df

def plot_data(method):
    df = read_classmate_data()
    if method == 'threshold':
        df = threshold_based_vampire(df)
    elif method == 'random':
        df = random_vampire(df)
    # Plot pie chart
    counts = df['Vampire'].value_counts()
    labels = ['Not Vampire', 'Vampire']
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Vampire Distribution')
    plt.savefig('static/pie_chart.png', bbox_inches='tight')
    plt.clf()
