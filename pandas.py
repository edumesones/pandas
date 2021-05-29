# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:22:20 2021

@author: egzlz
"""

df=pd.DataFrame('col one':[100,200],'col two':[300,400])
df2=pd.DataFrame(np.random.rand(4,8),columns=list('abcdefghi'))
df.columns=df.columns.str.replace(' ','_')
df.columns=["nuevo_nombre_1","nuevo_nombre_2"]

#al reves
df.loc[::-1].head()
#invertir orden de la tabla las filas
df.loc[::-1].reset_index(drop=True)
#cambiar orden de las columnas:invertir
df.loc[:,::-1].head()
#columnas por tipo de date
df.dtypes
df.select_dtypes(include='')
df.select_dtypes(exclude='')
#cadena a numero
pd.to_numeric(df.columna,errors='coerce') #coerce si NADA Nan
#cadena a numero + vacio=0
df.apply(pd.to_numeric,errors='coerce').fillna(0)

#reducir tamaño a traves de cambiar lso tipos de datos
dtypes={"continent":"category"} #antes era un objeto
nuevo_df=pd.rad_cvs("",usecols=cols,dtype=dtypes)
df.info(memory_usage='deep') #saber cuanta memoria te esta ocupando


#concatenar varios archivos,por filas
from glob import glob
stock_files=sorted(glob('/data/stocks*.csv')) #esta mirando todos los archivos
#que empiezan por stock
pd.concat(pd.read_csv(file)for file in stock_files,ignore_index=True)
#concatenar varios archivos,por columnas
pd.concat((pd.read_csv(file)for file in stock_files),axis='column')
#desde clipboard,es decir seleccionar parte de un excel y copiarlo
df=pd.read_clipboard()
df
#dividir dataset
movies_1=movies.sample(frac=0.75,random_state=)
movies_!.index.sort_values() #reordenar indices

#filtrar por valores de columnas
movies.column.unique
movies[(movies.genero=="accion") |(movies.column=="comedia")]
movies[movies.genero.isin(["accion","comedia"])]
#los que no son ese genero
movies[~movies.genero.isin(["accion","comedia"])]
#filtrar por cateogrias mas frcuentes
movies.genero.count_values()
movies.nlargest(3)
movies[movies.genero.isin.nlargest(3).index)] #te coje solo los generos con mas casos
#manejar missing
df.isna().sum()
df.isna().mean()
#borrar columnas con missing
df.dropna(axis='columns')
#borrar columnas con + 10% de missing
df.dropna(thresh=len(df)*0.9,axis='columns')
#dividir string en muchas columnas, caso nombre+apellidos
df["nombre","primer apellido","segundo apellido"]=df.columna.str.split(' ',expand=True)
#obtener columnas por valores de lista, en columna2 tenemos valores lista
nuevo_df=df.columna2.apply(pd.Series)
pd.concat([df,df_new],axis='columns') #quedaria borrar la columna de listas
#agregar muchas funciones
#calcular suma en funcion del valor de una columna
#si el item_id es 1 que me sume el valor delos items
orders[order.order_id==1].item_price.sum()
#todos los precios de los items dependiendo de su item_id
order.groupby('order_id').item_price.sum().head()
#suma de los precios de los items y numero de items por su id
order.groupby('order_id').item_price.agg(['sum','count'].head()
#combinar output de agregacion con dataframe (se tranforma el length)                                     
total_price=orders.groupby('order_id'.item_price.transform('sum')
orders["total_price"]=total_price
orders["percent_total"]=orders.item_price/orders.total_price
#otro caso de agrupar información añadiendo el unstack(),te hace tabla
#media supervivientes por y sexo
titanic.groupby(['sexo','clase_cabina']).survived.mean().unstack()
#tablas pivotantes (lo mismo que group by,sexo,Pclass y Survived son columnas
#margins igual a true te da la info de la columna total 
titanic.pivot_table(index='sexo',columns='Pclass',values='Suvived',addfunc='mean',margins=True) 
#cambiar data continua en categorica
#ejemplo edad en joven,adulto,viejo
pd.cut(titanic.age,bins=[0,18,25,99],labels=["child"",young adult",'adult'])
#cambiar formato a dos decimales
pd.set_option('diplay.float_format','{:.2f}'.format)
pd.reset_option('diplay.float_format')
#cambiar formato por ejemplo de fechas,precios etc Date,Close,Volume son columnas
format_dict={'Date':'{:%m/%d%y}','Close':'${:.2f}','Volume':'{:,}'}
stocks.style.format(format_dict)
(sotcks.style.format(fomat_dict).hide_index().
 highlight_min('Close',color='red')
 .highlight_max('Close',color='green'))
#intensidad de azul en funcion del volumnen
(sotcks.style.format(fomat_dict).hide_index().
 background_gradient('Volume',cmap='Blues')
 )

import pandas_profiling

pandas_profiling.ProfileReprot(titanic)

#solo ciertas filas
data[:4]
#ciertas filas ciertas columnas
df.loc[2] #nos da toda la info sobre la segunda fila,es decir valores asociados a las columnas
df.loc[:,["columna1","columna2"]] #toda la info columnas 1 y 2
df.loc[(df["year"]=='1967') & (segunda_condicion),['year','pop']] #seleccionar columnas bajo condicion
data.loc[:4,['columna1']]
df.loc[[2,0]] #nos da info de filas 0 y 2 por index
#seleccion por posicion
df.iloc[1] #primera columna
df.iloc[[1]] #primera fila
df.iloc[:4,:4]#primeras cuatro filas,primeras cuatro columnas
#si haces
data=data['input2']<50 #devuelve true o false en la columna
data=data[data['input2']<50] #te devuelve la condicion
data["columna1"].fillna(0)
data["column1"].fillna('mean')
#definir una funcion a columna
def funcion(x):
    if x<10:
        return 'hola'
    if x>10:
        return adios
    else:
        return 'no funciona'
df["columna"].apply(lambda x:funcion(x))
df["columna"].apply(funcion)
import datetime
a=datetime.datetime.now()

#merge unir tablas
pd.merge(df1,df2,left_on=["columna"],right_on=["columna3"],how='left')
df_new=df[(df["age"]<25) & (df['id']==condicion)]
#one_hot_econding
df=pd.get_dummies(df,prefix="mo",prefix_sep='_',columns=['month'],drop_first=True)
#graficas por columna,imaginemos año
df.mean().plot(subplots=True,figsize=(10,5))
#cambiar formato de datos
"""
tenemos columnas religion y sueldos de la gente y cuantas personas hay
entonces los sueldos nos gustaria tener en una unica columna respetando la religion
"""
#var_name sera el nuevo nombre de la columna,pasará de muchas columnas de diferentes rangos de sueldo a una sola que la englobe
#var value te dará el valor de cada una de las filas en cada columna
#id_vars es para saber las columnas que se mantienen fijas

df_nuevo=pd.melt(df,id_vars='religion',var_name="por sueldo",var_value='cuantas personas hay') #var_name te va a dar una columna con los diferentes valores de la columnas
#caso de uso de temperatura mejorado
url='https://raw.githubusercontent.com/chendaniely/2016-pydata-carolinas-pandas/master/data/tidy-data/data/weather-raw.csv'
df=pd.read_csv(url,sep=',')
df_nuevo=pd.melt(df,id_vars=["id","year","month","element"],var_name='day',value_name='temp')
#element tiene temp_max y temp_min y values es el valor de la temperatura ,table index es lo que aparece 
df_perfe=df_nuevo.pivot_table(index=["id","year","month","day"],columns='element',values='temp')
df_perfe.reset_index()

































