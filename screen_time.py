import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates




#Dataset importing and pre processing

screentime = pd.read_csv('screentime_analysis.csv')
screentime['Date'] = pd.to_datetime(screentime['Date'])

# print(screentime.info())
# print(screentime.head())


grpapp = screentime.groupby(['App'])['Usage (minutes)'].sum().reset_index().sort_values(by='Usage (minutes)',ascending=False)

#<--------------App vs usage----------------->
plt.figure(figsize=(12,6))
plt.bar(grpapp['App'],grpapp['Usage (minutes)'],color = 'orange')
plt.title('Most used apps')
plt.xlabel('Apps')
plt.ylabel('Usage (minutes)')
plt.savefig('App vs Usage.png',dpi = 300)
plt.show()

#<--------------App vs date wise usage----------------->

apps = screentime['App'].unique()

plt.figure(figsize=(12,6))
for app in apps:
    app_usage = screentime.loc[screentime['App']==app].sort_values(by = 'Date') 
    plt.plot(app_usage['Date'],app_usage['Usage (minutes)'],label = app, marker = '.',markersize ='10')


plt.legend()
locator = mdates.DayLocator(interval=4)
plt.gca().xaxis.set_major_locator(locator)
plt.title("Screen Time trends for different Apps")
plt.xlabel('Date')
plt.xticks(rotation = 45)
plt.ylabel('Usage (minutes)')
plt.savefig('App vs Datewise usage.png',dpi = 300)

plt.show()


#<--------------App vs day wise usage----------------->


screentime['Day'] = screentime['Date'].dt.day_name()

day_wise_usage = screentime.groupby(['Day'])['Usage (minutes)'].mean().reset_index()

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day_wise_usage['Day'] = pd.Categorical(day_wise_usage['Day'], categories=day_order, ordered=True)

day_wise_usage = day_wise_usage.sort_values(by='Day')

plt.figure(figsize=(12,6))
plt.bar(day_wise_usage['Day'],day_wise_usage['Usage (minutes)'],color = '#A1C349')
plt.title('Average screen time usage per day of the week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Usage (minutes)')   
plt.savefig('App vs Daywise Usage.png',dpi = 300)

plt.show()



#<--------------App vs day wise usage----------------->

insta_usage = screentime.loc[screentime['App']=='Instagram']
insta_group = insta_usage.groupby(['Day'])['Usage (minutes)'].mean().reset_index()
insta_group['Day'] = pd.Categorical(insta_group['Day'],categories=day_order,ordered=True)
insta_group =insta_group.sort_values(by ='Day')

Netflix_usage = screentime.loc[screentime['App']=='Netflix']
Netflix_group = Netflix_usage.groupby(['Day'])['Usage (minutes)'].mean().reset_index()
Netflix_group['Day'] = pd.Categorical(Netflix_group['Day'],categories=day_order,ordered=True)
Netflix_group =Netflix_group.sort_values(by ='Day')

Whatsapp_usage = screentime.loc[screentime['App']=='WhatsApp']
Whatsapp_group = Whatsapp_usage.groupby(['Day'])['Usage (minutes)'].mean().reset_index()
Whatsapp_group['Day'] = pd.Categorical(Whatsapp_group['Day'],categories=day_order,ordered=True)
Whatsapp_group =Whatsapp_group.sort_values(by ='Day')


bar_width = 0.25

x = np.arange(len(insta_group['Day']))


plt.figure(figsize=(12,6))
plt.bar(x, insta_group['Usage (minutes)'], width=bar_width, label='Instagram', align='center',color = '#E1306C')
plt.bar(x + bar_width, Netflix_group['Usage (minutes)'], width=bar_width, label='Netflix', align='center',color = '#E50914')
plt.bar(x + 2*bar_width, Whatsapp_group['Usage (minutes)'], width=bar_width, label='WhatsApp', align='center',color = '#25D366')

plt.title('Average Daily usage for Instagram, Netflix and WhatsApp')
plt.xlabel('Day of the Week')
plt.ylabel('Usage (minutes)')
plt.xticks(x + bar_width, insta_group['Day']) 
plt.legend()
plt.savefig('TopApps vs Usage.png',dpi = 300)

plt.show()