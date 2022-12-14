import csv
import view


def download_data(a):
    with open('log.csv', 'r') as f:
        for i in f:
            if a in i:
                print(i)






