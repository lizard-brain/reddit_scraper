import time
import datetime
import csv
import requests

'''
Make sure the database file is closed and restart the script

'''


#------------------------------------------------------------------------------------------------------


subreddit_lst = []

with open('database.csv', mode='r', newline='') as database_csv:
    database = csv.reader(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in database:
        subreddit_lst.append(1)

    
def process():

    
    with open('database.csv', mode='r', newline='') as database_csv:
    
        database = csv.reader(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in database:
            index = int(row[0])
            data_path = './data/' + row[0] + '_stats.csv'
            data_path_new = './data/' + row[0] + '_stats.csv'
            sub_red = row[1]
            sub_red = sub_red.strip()
            print(sub_red)
            with open(data_path_new, mode='a', newline='') as video_csv_new: #a for append
                csv_file_new = csv.writer(video_csv_new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_file_new.writerow(['time_e', 'localtime_human', 'active', 'subscribers', 'percent', sub_red])
                    

            

            with open(data_path, mode='r', newline='') as video_csv: #a for append
                csv_file = csv.reader(video_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row_i in csv_file:
                    time_e = row_i[1]
                    time_e = float(time_e)
                    time_human = time.strftime('%Y-%m-%d %H:%M', time.localtime(time_e)) 
                    active = row_i[2]
                    subs = row_i[3]
                    pct = row_i[4]
                    #print(time_e, time_human, active, subs, pct)
                    
                    with open(data_path_new, mode='a', newline='') as video_csv_new: #a for append
                        csv_file_new = csv.writer(video_csv_new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        #print('Writing CSV...', '\n')
                        csv_file_new.writerow([time_e, time_human, active, subs, pct])


process()



