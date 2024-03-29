# -*- coding: utf-8 -*-
"""Promilo_BA_Task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1beVX3CCXSKeYRp3lzMwC2MiXo4LGjFfy

**Data Analysis and Insights for different page Optimization &amp;
How to get more user install &amp; Engagement from the App &amp; Website ****

**Assignment Description**

As an intern in the Business Analytics team, your task is to analyze a provided dataset
and generate actionable insights to optimize page performance for a fictional company
called &quot;XYZ Inc.&quot; The dataset contains user data from various regions, customer
demographics, product information, and marketing campaign details. Your objective is to
identify critical factors influencing Data Analysis and Insights for different page
Optimization and how to get more user installation and engagement from the App and
website&quot; User and propose recommendations for improving performance.
"""

!pip install -U kaleido

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
!pip install plotly
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_excel('/content/drive/MyDrive/Data set for BA.xlsx')

excel_sheets = pd.ExcelFile('/content/drive/MyDrive/Data set for BA.xlsx')
sheets = excel_sheets.sheet_names
sheets

google_Ads_Report =pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Google Ads Report')
user_by_age = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='User By Age')
user_by_language= pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='User by Language')
user_by_interest = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name= 'User By Interest')
gender_report = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Gender Report')
citiwise_report = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Citiwise Report')
demographics_report= pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Demographics Report')
pages_and_screens_report = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Pages & Screens Report')
conversion_report = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Conversion Report')
event_report= pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Event Report')
traffic_aquisition = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='Traffic Aquisition')
user_acquisition = pd.read_excel("/content/drive/MyDrive/Data set for BA.xlsx",sheet_name='User Acquisition')

"""# Google Ads Report"""

google_Ads_Report.head()

#checking datatypes
google_Ads_Report.dtypes

#checking missing values
google_Ads_Report.isnull().sum()

google_Ads_Report.sum()

google_Ads_Report.describe()

user_graph =px.bar(google_Ads_Report,x='Session Google Ads campaign',y='Users',
                    text_auto = True,height=500 )
user_graph.show()

#  App installed for may  Google ads campaign have the highest users count.

#  total number of sessions that the Google Ads campaign produced as well as the number of sessions in which users actively participated

bar1 = go.Bar(x=google_Ads_Report['Session Google Ads campaign'],
              y=google_Ads_Report["Sessions"],
              text=google_Ads_Report["Sessions"],
              textposition="auto",
              name="Sessions",
              marker=dict(color='black'))

bar2 = go.Bar(x=google_Ads_Report['Session Google Ads campaign'],
              y=google_Ads_Report["Engaged sessions"],
              text=google_Ads_Report["Engaged sessions"],
              textposition="auto",
              name="Engaged sessions")

layout = go.Layout(title="Number of session generated and actively engaged google ads campaign", height=800)

fig=go.Figure(data=[bar1,bar2],layout=layout)

fig.show()

# Expense of Google Ads compared to return as an event count
line1 = go.Scatter(x=google_Ads_Report["Session Google Ads campaign"],
                   y=google_Ads_Report["Google Ads cost"],
                   mode="lines+markers",
                   text=google_Ads_Report["Google Ads cost"],
                   marker=dict(color="blue"),
                   name="Google Ads cost")

line2 = go.Scatter(x=google_Ads_Report["Session Google Ads campaign"],
                   y=google_Ads_Report["Conversions"],
                   mode="lines + markers",
                   text=google_Ads_Report["Conversions"],
                   marker=dict(color="orange"),
                   name="Conversions")

layout = go.Layout(title="Cost invested in google add against conversion", height=600,
                   xaxis=dict(title='sessions google ads campaign'),
                   yaxis=dict(title='Amount invested and number of conversion'))
fig=go.Figure(data=[line1,line2],layout=layout)

fig.show()

"""# Users by age"""

user_by_age

user_by_age.dtypes

user_by_age.sum()

user_by_age.describe()

# Age wise users and new users generated

bar1 = go.Bar(x=user_by_age['Age'],
              y=user_by_age["Users"],
              text=user_by_age["Users"],
              textposition="auto",
              name="Users",
              marker=dict(color='cadetblue'))

bar2 = go.Bar(x=user_by_age['Age'],
              y=user_by_age["New users"],
              text=user_by_age["New users"],
              textposition="auto",
              name="New Users",
              marker=dict(color='lightcoral'))


layout = go.Layout(title="Age wise users and new users", height=600,
                   xaxis=dict(title='Age Catergory'),
                   yaxis=dict(title='Number of unsers and new users'))
fig=go.Figure(data=[bar1,bar2],layout=layout)

fig.show()
fig.write_image("User_age(1).png")

"""* The "unknown" category seems to have the most users (14,303) and new users (13,636) according to the data that is currently available. More research and data analysis are required to fully comprehend and categorise this area.
A noticeable influx of new users and users outside of the "unknown" category are those in the 18–20 age range. A sizeable portion of the platform's prospective user base falls within this category.

* The following ideas should be taken into consideration in order to take advantage of this chance and enhance user acquisition from this age group:
User onboarding, target marketing, social sharing, and user surveys.
"""

# Sessions and events counts
engaged_sessions=go.Bar(x=user_by_age["Age"],
             y=user_by_age["Engaged sessions"],
              text=user_by_age["Engaged sessions"],
             textposition="auto",
             name="Engaged Sessions",
             marker=dict(color='purple'))

event_count=go.Bar(x=user_by_age["Age"],
             y=user_by_age["Event count"],
                   text=user_by_age["Event count"],
                   textposition="auto",
             name="Event counts",
             marker=dict(color='salmon'))


layout = go.Layout(title="Age group by sessions organished and event happens ", height=600,
                   xaxis=dict(title='Age Catergory'),
                   yaxis=dict(title='Number of sessions and event happens'))
fig=go.Figure(data=[engaged_sessions,event_count],layout=layout)

fig.show()
fig.write_image("User_age(2).png")

"""# Users by language"""

user_by_language

user_by_language.dtypes

user_by_language.isnull().sum()

user_by_language.sum()

user_by_language.describe()

# Top 10 Language prefrence
user_by_language_10 = user_by_language.sort_values(by=["Users","New users"],ascending =False)

top_10_language=user_by_language_10.head(10)

bar1=go.Bar(x=top_10_language["Language"],
             y=top_10_language["Users"],
              text=top_10_language["Users"],
             textposition="auto",
             name="Users",
             marker=dict(color='olive'))
bar2=go.Bar(x=top_10_language["Language"],
             y=top_10_language["New users"],
                   text=top_10_language["New users"],
                   textposition="auto",
             name="New Users",
             marker=dict(color='cadetblue'))


layout = go.Layout(title="Top 10 language prefrences by users and new users ", height=600,
                   xaxis=dict(title='Languages'),
                   yaxis=dict(title='Number of users / new users'))
fig=go.Figure(data=[bar1,bar2],layout=layout)

fig.show()
fig.write_image("User_lang(1).png")

# Top preferred language was english

user_by_language_10.head(10)

"""# User By Interest"""

user_by_interest.head(10)

user_by_interest.dtypes

user_by_interest.isnull().sum()

user_by_interest.sum()

# Top 10 User interest
user_by_interest_sort=user_by_interest.sort_values(by=["Users","New users"],ascending=False)
top10_userby_interest=user_by_interest_sort.head(10)
top10_userby_interest

bar1=go.Bar(x=top10_userby_interest["Interests"],
            y=top10_userby_interest["Users"],
            text=top10_userby_interest["Users"],
            textposition="auto",
            name="Users",
            marker=dict(color="darkslateblue"))


bar2=go.Bar(x=top10_userby_interest["Interests"],
            y=top10_userby_interest["New users"],
            text=top10_userby_interest["New users"],
            textposition="auto",
            name="New users",
            marker=dict(color="moccasin"))

layout = go.Layout(title="Top 10 Inetrest users and user users attract ", height=600,
                   xaxis=dict(title='Intrest'),
                   yaxis=dict(title='Number of users / new users'))
fig=go.Figure(data=[bar1,bar2],layout=layout)

fig.show()
fig.write_image("User_Interest(1).png")

# Top 10 interest with highest engaged sessions

line1 = go.Scatter(x=top10_userby_interest["Interests"],
                   y=top10_userby_interest["Engaged sessions"],
                   mode="lines+markers",  # Show both lines and markers
                   text=top10_userby_interest["Engaged sessions"],
                   textposition="top center",  # Position of the data labels
                   name="Engaged sessions",
                   marker=dict(color="steelblue"))

layout = go.Layout(title="Top 10 Interests with Highest Engaged Sessions", height=600,
                   xaxis=dict(title='Interest', showline=True, showticklabels=True),
                   yaxis=dict(title='Number of Engaged Sessions', showline=True, showticklabels=True))

fig = go.Figure(data=[line1], layout=layout)

fig.show()
fig.write_image("Top_users(1).png")

# Top 10 intrest with highest conversions

line1 = go.Scatter(x=top10_userby_interest["Interests"],
                   y=top10_userby_interest["Conversions"],
                   mode="lines+markers",  # Show both lines and markers
                   text=top10_userby_interest["Conversions"],
                   textposition="top center",  # Position of the data labels
                   name="Conversions",
                   marker=dict(color="tomato"))

layout = go.Layout(title="Top 10 Interests with Highest conversions ", height=600,
                   xaxis=dict(title='Interest', showline=True, showticklabels=True),
                   yaxis=dict(title='Number of conversions', showline=True, showticklabels=True))

fig = go.Figure(data=[line1], layout=layout)

fig.show()
fig.write_image("Top_users(2).png")

"""# Gender Report"""

gender_report

gender_report.dtypes

gender_report.isnull().sum()

#Gender wise user percentage


pie_chart = go.Pie(labels=gender_report["Gender"],
                   values=gender_report["Users"],
                   marker=dict(colors=["teal","salmon","Olive"]),
                   textinfo='label+percent',
                   textposition='inside',
                   hoverinfo='label+percent',
                   hole=0.4)
layout = go.Layout(title='User gender wise percentage ')

fig = go.Figure(data=[pie_chart], layout=layout)
fig.show()
fig.write_image("Usersg(1).png")

# New users gender wise percentage


pie_chart = go.Pie(labels=gender_report["Gender"],
                   values=gender_report["New users"],
                   marker=dict(colors=["teal","salmon","Olive"]),
                   textinfo='label+percent',
                   textposition='outside',
                   hoverinfo='label+percent',
                   hole=0.4)
layout = go.Layout(title='New user gender')

fig = go.Figure(data=[pie_chart], layout=layout)
fig.show()
fig.write_image("Usersg(2).png")

# average time spend by gender
bar1=go.Bar(x=gender_report["Gender"],
            y=gender_report["Average engagement time"]/60,
            text=gender_report["Average engagement time"]/60,
            textposition="auto",
            name="Avergae engament time in mins",
            marker=dict(color="darksalmon")
            )

layout = go.Layout(title="Average time watched in mins ", height=600,
                   xaxis=dict(title='Gender'),
                   yaxis=dict(title='Average time in min'))
fig=go.Figure(data=[bar1],layout=layout)

fig.show()
fig.write_image("Avgtm(1).png")

"""# Citiwise Report"""

citiwise_report

citiwise_report.dtypes

citiwise_report.isnull().sum()

citiwise_report.describe()

#Top 10 cities attract users

citiwise_report_sort=citiwise_report.sort_values(by=["Users","New users"],ascending =False)
top10_citi = citiwise_report_sort.head(10)
top10_citi

bar1=go.Bar(x=top10_citi["Town/City"],
            y=top10_citi["Users"],
            text=top10_citi["Users"],
            textposition="auto",
            name="Users",
            marker=dict(color="cadetblue"))

bar2=go.Bar(x=top10_citi["Town/City"],
            y=top10_citi["New users"],
            text=top10_citi["New users"],
            textposition="auto",
            name="New users",
            marker=dict(color="Olive"))

layout = go.Layout(title="Top 10 cities attarct users", height=600,
                   xaxis=dict(title='Town/city'),
                   yaxis=dict(title='Number of users / new users'))
fig=go.Figure(data=[bar1,bar2],layout=layout)

fig.show()
fig.write_image("Citiw_img(1).png")

#Top 10 cities by engaged session impact of Event count and conversion

citiwise_report_sort=citiwise_report.sort_values(by=["Engaged sessions"],ascending =False)
top10_citi = citiwise_report_sort.head(10)
top10_citi

bar1=go.Bar(x=top10_citi["Town/City"],
            y=top10_citi["Engaged sessions"],
            text=top10_citi["Engaged sessions"],
            textposition="auto",
            name="Engaged sessions",
            marker=dict(color="cadetblue"))

bar2=go.Bar(x=top10_citi["Town/City"],
            y=top10_citi["Event count"],
            text=top10_citi["Event count"],
            textposition="auto",
            name="Event count",
            marker=dict(color="palevioletred"))

bar3=go.Bar(x=top10_citi["Town/City"],
            y=top10_citi["Conversions"],
            text=top10_citi["Conversions"],
            textposition="auto",
            name="Conversions",
            marker=dict(color="salmon"))
layout = go.Layout(title="Top 10 cities by engaged session impact of Event count and conversion", height=600,
                   xaxis=dict(title='Town/city'),
                   yaxis=dict(title='Numbers count'))
fig=go.Figure(data=[bar1,bar2,bar3],layout=layout)

fig.show()

"""# Demographic Report"""

demographics_report.head()

demographics_report.dtypes

demographics_report.isnull().sum()

demographics_report.describe()

demographic_sort=demographics_report.sort_values(by=["Users","New users"],ascending=False)
top10_demographic=demographics_report.head(10)
top10_demographic

bar1=go.Bar(x=top10_demographic["Country"],
            y=top10_demographic["Users"],
            text=top10_demographic["Users"],
            textposition="auto",
            name="Users",
            marker=dict(color="teal"))


bar2=go.Bar(x=top10_demographic["Country"],
            y=top10_demographic["New users"],
            text=top10_demographic["New users"],
            textposition="auto",
            name="New users",
            marker=dict(color="salmon"))

layout = go.Layout(title="Top 10 country who install application ", height=600,
                   xaxis=dict(title='Country'),
                   yaxis=dict(title='Number of users / new users'))
fig=go.Figure(data=[bar1,bar2],layout=layout)

fig.show()
fig.write_image("Demogr_img(1).png")

"""# Traffic Aquisition"""

traffic_aquisition

traffic_aquisition.dtypes

traffic_aquisition.isnull().sum()

# Traffic source percentage

traffic_pie = go.Pie(labels=traffic_aquisition["Session default channel group"],
                     values=traffic_aquisition["Users"],
                     marker=dict(colors=["palevioletred","salmon","cadetblue","DarkSeaGreen","maroon","lightseagreen"]),
                     textinfo='label+percent',
                     textposition='outside',
                     hoverinfo='label+percent',
                     hole=0.4)
layout = go.Layout(title='Traffic percentile')

fig = go.Figure(data=[traffic_pie], layout=layout)
fig.show()
fig.write_image("Traffic_img(1).png")

"""# User Acquisition"""

user_acquisition

user_acquisition.dtypes

user_acquisition.isnull().sum()

user_acquisition.describe()

# New User Acquisition
new_user_acq = go.Pie(labels=user_acquisition["First user default channel group"],
                     values=user_acquisition["New users"],
                     marker=dict(colors=["palevioletred","salmon","cadetblue","RosyBrown","olive","lightseagreen"]),
                     textinfo='label+percent',
                     textposition='outside',
                     hoverinfo='label+percent',
                     hole=0.4)
layout = go.Layout(title='New User Acquisition')

fig = go.Figure(data=[new_user_acq], layout=layout)
fig.show()
fig.write_image("Traffic_img(2).png")

"""# Pages And Screens Report"""

pages_and_screens_report.head()

pages_and_screens_report.dtypes

pages_and_screens_report.isnull().sum()

pages_and_screens_report.describe()

# Top 10 pages and screens report
pages_and_screens_report_sort = pages_and_screens_report.sort_values(by="Views",ascending=False)
top10_pages_and_screens=pages_and_screens_report_sort.head(10)
top10_pages_and_screens

bar1=go.Bar(x=top10_pages_and_screens["Page path and screen class"],
            y=top10_pages_and_screens["Views"],
            text=top10_pages_and_screens["Views"],
            textposition="auto",
            name="Views",
            marker=dict(color="lightcoral"))

layout = go.Layout(title="Top 10 pages and screens by views", height=600,
                   xaxis=dict(title='pages path and screen'),
                   yaxis=dict(title='Number of views'))
fig=go.Figure(data=[bar1],layout=layout)

fig.show()
fig.write_image("PagesandScreenimage.png")

#Below 10 pages and screens

pages_and_screens_report_sort = pages_and_screens_report.sort_values(by="Views",ascending=True)
below10_pages_and_screens=pages_and_screens_report_sort.head(10)
below10_pages_and_screens

bar1=go.Bar(x=below10_pages_and_screens["Page path and screen class"],
            y=below10_pages_and_screens["Views"],
            text=below10_pages_and_screens["Views"],
            textposition="auto",
            name="Views",
            marker=dict(color="lightcoral"))

layout = go.Layout(title="below 10 pages and screens by views", height=600,
                   xaxis=dict(title='pages path and screen'),
                   yaxis=dict(title='Number of views'))
fig=go.Figure(data=[bar1],layout=layout)

fig.show()
fig.write_image("Pages_and_screen(2).png")