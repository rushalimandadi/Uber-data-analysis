#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("C:\\Users\\rusha\\Downloads\\uber_data.csv")


# In[4]:


df.head()


# In[5]:


df.info()


# In[7]:


df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])


# In[8]:


df.info()


# In[9]:


df=df.drop_duplicates().reset_index(drop=True)
df['trip_id']=df.index


# In[10]:


df


# In[11]:


datetime_dim=df[['tpep_pickup_datetime','tpep_dropoff_datetime']].reset_index(drop=True)


# In[12]:


datetime_dim


# In[13]:


datetime_dim['tpep_pickup_datetime']=datetime_dim['tpep_pickup_datetime']


# In[15]:


datetime_dim['pick_hour']=datetime_dim['tpep_pickup_datetime'].dt.hour
datetime_dim['pick_day']=datetime_dim['tpep_pickup_datetime'].dt.day
datetime_dim['pick_month']=datetime_dim['tpep_pickup_datetime'].dt.month
datetime_dim['pick_year']=datetime_dim['tpep_pickup_datetime'].dt.year
datetime_dim['pick_weekday']=datetime_dim['tpep_pickup_datetime'].dt.weekday


# In[16]:


datetime_dim['tpep_dropoff_datetime']=datetime_dim['tpep_dropoff_datetime']


# In[17]:


datetime_dim['drop_hour']=datetime_dim['tpep_dropoff_datetime'].dt.hour
datetime_dim['drop_day']=datetime_dim['tpep_dropoff_datetime'].dt.day
datetime_dim['drop_month']=datetime_dim['tpep_dropoff_datetime'].dt.month
datetime_dim['drop_year']=datetime_dim['tpep_dropoff_datetime'].dt.year
datetime_dim['drop_weekday']=datetime_dim['tpep_dropoff_datetime'].dt.weekday


# In[18]:


datetime_dim['datetime_id']=datetime_dim.index


# In[19]:


datetime_dim


# In[20]:


datetime_dim=datetime_dim[['datetime_id','tpep_pickup_datetime','tpep_dropoff_datetime','pick_hour','pick_day','pick_month','pick_year','pick_weekday','drop_hour','drop_day','drop_month','drop_year','drop_weekday']]


# In[21]:


datetime_dim


# In[28]:


passenger_count_dim=df[['passenger_count']].reset_index(drop=True)
passenger_count_dim['passenger_count_id']=passenger_count_dim.index
passenger_count_dim=passenger_count_dim[['passenger_count_id','passenger_count']]


# In[29]:


passenger_count_dim


# In[30]:


trip_distance_dim=df[['trip_distance']].reset_index(drop=True)
trip_distance_dim['trip_distance_id']=trip_distance_dim.index
trip_distance_dim=trip_distance_dim[['trip_distance_id','trip_distance']]


# In[31]:


trip_distance_dim


# In[32]:


payment_type_name = {
    1:"Credit card",
    2:"Cash",
    3:"No charge",
    4:"Dispute",
    5:"Unknown",
    6:"Voided trip"
}
payment_type_dim=df[['payment_type']].reset_index(drop=True)
payment_type_dim['payment_type_id']=payment_type_dim.index
payment_type_dim['payment_type_name']=payment_type_dim['payment_type'].map(payment_type_name)
payment_type_dim=payment_type_dim[['payment_type_id','payment_type','payment_type_name']]


# In[33]:


payment_type_dim


# In[34]:


rate_code_type = {
    1:"Standard rate",
    2:"JFK",
    3:"Newark",
    4:"Nassau or Westchester",
    5:"Negotiated fare",
    6:"Group ride"
}
rate_code_dim=df[['RatecodeID']].reset_index(drop=True)
rate_code_dim['rate_code_id']=rate_code_dim.index
rate_code_dim['rate_code_name']=rate_code_dim['RatecodeID'].map(rate_code_type)
rate_code_dim=rate_code_dim[['rate_code_id','RatecodeID','rate_code_name']]


# In[36]:


rate_code_dim.head()


# In[37]:


pickup_location_dim=df[['pickup_latitude','pickup_longitude']].reset_index(drop=True)
pickup_location_dim['pickup_location_id']=pickup_location_dim.index
pickup_location_dim=pickup_location_dim[['pickup_location_id','pickup_latitude','pickup_longitude']]


# In[38]:


pickup_location_dim


# In[42]:


dropoff_location_dim=df[['dropoff_latitude','dropoff_longitude']].reset_index(drop=True)
dropoff_location_dim['dropoff_location_id']=dropoff_location_dim.index
dropoff_location_dim=dropoff_location_dim[['dropoff_location_id','dropoff_latitude','dropoff_longitude']]


# In[43]:


dropoff_location_dim


# In[44]:


fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id')              .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id')              .merge(rate_code_dim, left_on='trip_id', right_on='rate_code_id')              .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id')              .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')             .merge(datetime_dim, left_on='trip_id', right_on='datetime_id')              .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id')              [['trip_id','VendorID', 'datetime_id', 'passenger_count_id',
               'trip_distance_id', 'rate_code_id', 'store_and_fwd_flag', 'pickup_location_id', 'dropoff_location_id',
               'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
               'improvement_surcharge', 'total_amount']]


# In[45]:


fact_table


# In[ ]:




