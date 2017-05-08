"""Creating Series to Validate Approval/Disapproval Series"""
import pandas as pd

# data: realclearpolitics is an aggregation of several polls
# http://www.realclearpolitics.com/epolls/other/president_trump_job_approval-6179.html#polls

# approval series
approval_data_dict = {
    "03": .401,
    "04": .398,
    "05": .404,
    "06": .403,
    "07": .401,
    "08": .404,
    "09": .404,
    "10": .416,
    "11": .420,
    "12": .421,
    "13": .418,
    "14": .414,
    "15": .413,
    "16": .418,
    "17": .418,
    "18": .425,
    "19": .422,
    "20": .4255,
    "21": .4255,
    "22": .424,
    "23": .423,
    "24": .425,
    "25": .421,
    "26": .424,
    "27": .426,
    "28": .431,
    "29": .431,
    "30": .430
}


disapproval_data_dict = {
    "03": .533,
    "04": .533,
    "05": .528,
    "06": .529,
    "07": .531,
    "08": .534,
    "09": .534,
    "10": .526,
    "11": .523,
    "12": .523,
    "13": .519,
    "14": .517,
    "15": .517,
    "16": .513,
    "17": .513,
    "18": .505,
    "19": .511,
    "20": .507,
    "21": .508,
    "22": .509,
    "23": .518,
    "24": .516,
    "25": .521,
    "26": .527,
    "27": .524,
    "28": .519,
    "29": .518,
    "30": .520
}

# convert dictionary to series
valid_approval = pd.Series(approval_data_dict)

# convert dictionary to series
valid_disapproval = pd.Series(disapproval_data_dict)
