import time
import csv
import requests



#------------------------------------------------------------------------------------------------------


subreddit_lst = []

with open('database.csv', mode='r', newline='') as database_csv:
    database = csv.reader(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in database:
        subreddit_lst.append(1)

    
def reddit_log():

    
    with open('database.csv', mode='r', newline='') as database_csv:
    
        database = csv.reader(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in database:
            index = int(row[0])
            data_path = './data/' + row[0] + '_stats' 
            sub_red = row[1]
            sub_red = sub_red.strip()
            #print('Subreddit',sub_red)
            usrs_online = get_active_users(sub_red)
            sub_count = get_sub_count(sub_red)
            pct = (usrs_online / sub_count)*100
            pct = round(pct,3)
            print(sub_red, '| Sub Count:', sub_count, '| Online Users:', usrs_online, ' | % Online:', pct )
            
            active_change = usrs_online - subreddit_lst[index]
            print('User Change:',active_change)


            with open(data_path, mode='a', newline='') as video_csv: #a for append
                csv_file = csv.writer(video_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                print('Writing CSV...', '\n')
                csv_file.writerow([time.strftime('%H:%M', time.localtime()), time.time(), usrs_online, sub_count, pct ])
                subreddit_lst[index] = usrs_online
                    
       
#------------------------------------------------------------------------------------------------------


#Reddit API interface to sub nuber of active users

headers = {
    "User-Agent": "don't rate limit me"
}

def get_active_users(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        # handle request error, return -1?
        return -1
    content = resp.json()
    return content["data"]["accounts_active"]

#------------------------------------------------------------------------------------------------------

#Reddit API interface to sub count

headers = {
    "User-Agent": "don't rate limit me"
}

def get_sub_count(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        # handle request error, return -1?
        return -1
    content = resp.json()
    return content["data"]["subscribers"]
#------------------------------------------------------------------------------------------------------

def run():
    wait = 300
    cycle_start = time.time()
    reddit_log()
    cycle_end = time.time()
    cycle_time = cycle_end - cycle_start
    print('Cycle Time(s):', cycle_time)
    print('cycle complete', time.strftime('%H:%M', time.localtime()), '\n')
    print('Waiting', wait/60, 'mins', '\n')
    time.sleep(wait) #5 mins wait before  refresh

#------------------------------------------------------------------------------------------------------

while True:
    try:
        run()
    except:
        print("Error")
        time.sleep(15)



