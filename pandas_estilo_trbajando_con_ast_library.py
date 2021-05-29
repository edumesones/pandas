# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:09:36 2021

@author: egzlz
"""

import pandas as pd

url='https://raw.githubusercontent.com/dataprofessor/data/master/nba-player-stats-2019.csv'
df=pd.read_csv(url)
selection = ['Player','Pos','Age','Tm','G','3P%','2P%','FT%','AST','STL','BLK','PTS']
df=df[selection]
df.head(20).style.set_table_styles(
[{'selector': 'th',
  'props': [('background', '#7CAE00'), 
            ('color', 'white'),
            ('font-family', 'verdana')]},
 
 {'selector': 'td',
  'props': [('font-family', 'verdana')]},

 {'selector': 'tr:nth-of-type(odd)',
  'props': [('background', '#DCDCDC')]}, 
 
 {'selector': 'tr:nth-of-type(even)',
  'props': [('background', 'white')]},
 
]
).hide_index()
df.to_csv('formato.csv')
def color_red(val):
  if val > 20:
    color = 'green'
  elif val > 5:
    color = 'red'
  else:
    color = 'black'
  return 'color: %s' % color

df.head(20).style.set_table_styles(
[{'selector': 'th',
  'props': [('background', '#7CAE00'), 
            ('color', 'white'),
            ('font-family', 'verdana')]},
 
 {'selector': 'td',
  'props': [('font-family', 'verdana')]},

 {'selector': 'tr:nth-of-type(odd)',
  'props': [('background', '#DCDCDC')]}, 
 
 {'selector': 'tr:nth-of-type(even)',
  'props': [('background', 'white')]},
 
 {'selector': 'tr:hover',
  'props': [('background-color', 'yellow')]}

]
).hide_index()

df[['PTS']].head(20).style.applymap(color_red)

#en columna rating tenemos un string en formato lista de diccionarios
import ast
url='https://raw.githubusercontent.com/justmarkham/pycon-2019-tutorial/1ef2e795d02ad0ae2e9dc8bfaaf77f61370118d8/ted.csv'
df=pd.read_csv(url)
a=ast.literal_eval(df.ratings[0])

def str_to_list(ratings_str):
    return ast.literal_eval(ratings_str)

str_to_list(df.ratings[0])

#ahora es una lista
df['ratings_list']=df.ratings.apply(str_to_list)

def get_num_ratings(list_of_dicts):
    num=0
    for d in list_of_dicts:
        num+=d['count']
    return num

#nueva columna con los numeros

df['num_ratings']=df.ratings_list.apply(get_num_ratings)
#buscamos datos sobre funny
df.ratings.str.contains('Funny').value_counts()
def get_funny_ratings(list_of_dicts):
    for d in list_of_dicts:
        if d['name']=='Funny':
            return d['count']
#le aplicamos la funcion
df['funny_ratings']=df.ratings_list.apply(get_funny_ratings)

df['funny_rate']=df.funny_ratings/df.num_ratings
df.sort_values('funny_rate').speaker_occupation.tail(20)

df.groupby('speaker_occupation').funny_rate.mean().sort_values().tail()




