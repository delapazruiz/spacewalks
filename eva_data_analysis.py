import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = './eva_data.json'
output_file = './eva_data.csv'
graph_file = './cumulative_eva_graph.png'
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
eva_df['eva'] = eva_df['eva'].astype(float)
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
eva_df.to_csv(output_file, index=False, encoding='utf-8')
eva_df.sort_values('date', inplace=True)
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()

# import datetime as dt
# import csv
# import json
# import matplotlib.pyplot as plt

# import pandas as pd


# # https://data.nasa.gov/resource/eva.json (with modifications)
# data_f = open('eva_data.json', 'r', encoding= "ascii")
# data_t = open('eva_data.csv','w', encoding="utf-8")
# g_file = 'cumulative_eva_graph.png'

# fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

# data=[]


# for i in range(375):
#     line=data_f.readline()
#     print(line)
#     data.append(json.loads(line[1:-1]))
# #data.pop(0)
# ## Comment out this bit if you don't want the spreadsheet

# w=csv.writer(data_t)

# time = []
# date =[]

# j=0
# for i in data:
#     print(data[j])
#     # and this bit
#     w.writerow(data[j].values())
#     if 'duration' in data[j].keys():
#         tt=data[j]['duration']
#         if tt == '':
#             pass
#         else:
#             t=dt.datetime.strptime(tt,'%H:%M')
#             ttt = dt.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()/(60*60)
#             print(t,ttt)
#             time.append(ttt)
#             if 'date' in data[j].keys():
#                 date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
#                 #date.append(data[j]['date'][0:10])

#             else:
#                 time.pop(0)
#     j+=1

# t=[0]
# for i in time:
#     t.append(t[-1]+i)

# date,time = zip(*sorted(zip(date, time)))

# plt.plot(date,t[1:], 'ko-')
# plt.xlabel('Year')
# plt.ylabel('Total time spent in space to date (hours)')
# plt.tight_layout()
# plt.savefig(g_file)
# plt.show()
