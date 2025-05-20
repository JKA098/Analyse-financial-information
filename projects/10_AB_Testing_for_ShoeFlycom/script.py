import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# task 1

# print(ad_clicks.head())
print(ad_clicks.head())
# task 2
utm_source = ad_clicks.groupby('utm_source')\
          .user_id.count()\
          .reset_index()

# print(utm_source)

# task 3

ad_clicks['is_click'] = ~ad_clicks\
      .ad_click_timestamp.isnull()



# task 4

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])\
    .user_id.count()\
    .reset_index()

print(clicks_by_source)
# task 5

clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()
print(clicks_pivot)

# task 6

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])

# task 7

experimental_group_count = ad_clicks.groupby('experimental_group').count().reset_index()
# print(experimental_group_count)

# task 8
is_click_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()


# task 9
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks)
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(b_clicks)


# task 10
a_clicks_day = ad_clicks.groupby(['is_click','day']).user_id.count().reset_index()
# print(a_clicks_day)

b_clicks_day = ad_clicks.groupby(['is_click','day']).user_id.count().reset_index()
# print(b_clicks_day)



# task 11
print(a_clicks_day)
print(b_clicks_day)






