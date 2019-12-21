## Iris dataset
#with Jason edits
import plotly.express as px
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()

## Car dataset
car_df = pd.read_csv('cardataset.csv')
car_df.head()
car_df_new = car_df[car_df['MSRP']<50000]
car_df_new['price bucket']=pd.cut(car_df_new.MSRP,5)

attribute_list = ['Engine HP','Engine Cylinders','Transmission Type','highway MPG','Vehicle Size']
comb_att_list = list(itertools.combinations(attribute_list,3))
comb_att_list
len(comb_att_list)

for i in range(0,len(comb_att_list)):
    sublist=comb_att_list[i]
    x=sublist[0]
    y=sublist[1]
    z=sublist[2]
    fig = px.scatter_3d(car_df_new, x=x,y=y,z=z,
              color='price bucket')
    fig.show()
