#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# This file is used to deal with my papers
'''
@Time    :   2020/06/16
@Author  :   HQ ZHU(zhuhanqingmame@sjtu.edu.cn) 
'''

import os
import sys
import pandas as pd
import argparse
from datetime import datetime
import re # Regular expression operations

# add parser
parser = argparse.ArgumentParser()
parser.add_argument('--isCreate', type=bool, 
                    default=False,
                    help='Create the paper database(true) or Update(false)')
parser.add_argument('--data_dir', type=str, 
                    default='E:/Papers/paper_db.csv',
                    help='Directory of the paper database')
parser.add_argument('--git_dir', type=str, 
                    default='E:/WORK/DailyThings/paper_db.csv',
                    help='Directory of the github paper database')
parser.add_argument('-y','--year',type=str, 
                    default='2020',
                    help='Year of this paper')
parser.add_argument('-s','--source',type=str, 
                    default='DAC',
                    help='Source of this paper')
parser.add_argument('-n','--name',type=str, 
                    default='Name of paper',
                    help='Name of this paper')
parser.add_argument('-k','--keywords',type=str, 
                    default='None',
                    help='Keywords of this paper')


def load_data(FLAGS, silence=False):
    '''Summary of function here.
    Loading the paper database.
    '''
    if not silence:print('Load data from: ', FLAGS.data_dir)
    if not os.path.exists(FLAGS.data_dir):
        sys.exit("Data file " + FLAGS.data_dir + " does not exist!")

    with open(FLAGS.data_dir,'r') as f:
        data = pd.read_csv(f,encoding='gb18030')
    return data                                        

if __name__ == "__main__":
    # Load parser
    FLAGS, unparsed = parser.parse_known_args()
    
    print("Start...........")
    
    # obtain the current time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d")

    # Remove all special characters, punctuation and spaces from paper name
    # And substitute with '_'
    re_name = re.sub('\W+', '_',FLAGS.name)

    if FLAGS.isCreate == True:
        # Create csv file
        row_num = 0 # default row_num is 0

        # create paper database: db
        db = pd.DataFrame({'Index': [row_num],
                        'Year': [FLAGS.year],
                        'Source': [FLAGS.source],
                        'Name': [FLAGS.name],
                        'Keywords':[FLAGS.keywords],
                        'Time':[time]})
        # # ?Add index column
        # df['index'] = df.index
        
    else:
        # load database
        db = load_data(FLAGS)
        
        # obtain the row number
        row_num = db.shape[0]

        # new row data
        new_paper_data = [row_num, FLAGS.year, FLAGS.source, FLAGS.name, FLAGS.keywords, time]
        db.loc[row_num] = new_paper_data
        
    # save file to csv    
    db.to_csv(FLAGS.data_dir,index=False)

    # github dir

    db_copy = db.copy()
    db_copy.to_csv(FLAGS.git_dir,index=False)

    # print paper name
    paper_name = "NO"+str(row_num)+'_'+FLAGS.year+'_'+FLAGS.source+'_'+re_name
    print("paper name: ", paper_name)
