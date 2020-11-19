# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:39:57 2020

@author: Deepa Kapoor
"""
##NPI num,Name,Gender,Last Updated Certi date,Enumeration Date,NPI Type,Sole Proprietor,Status
##,Mailing Address,Primary Practice Address
## 'number','name', 'basic''gender', 'basic''last_updated', 'basic''enumeration_date',
## 'enumeration_type', 'basic''sole_proprietor', 'basic''status', 'addresses'[0]
from npyi import npi
import csv
import requests
import json
import pandas as pd
import numpy as np
from flatten_json import flatten


list = [1992826994,
1063478204,
1194937805,
1205122512,
1326051400,
1275526022,
1245363530,
1134394323,
1508032533,
1851454268,
1053474866,
1477902252,
1952693228,
1669447439,
1427050392,
1457423170,
1720077506,
1013906791,
1780769786,
1376509364,
1972580215,
1962799858,
1952474504,
1013099126,
1922326727,
1932169711,
1083008932,
1740327790,
1942469622,
1811214026,
1326124256,
1467412684,
1487861761,
1740486786,
1063857662,
1740417617,
1013027036,
1295077758,
1720233927,
1073900940,
1154366763,
1295078087,
1427443233,
1881779247,
1124316799,
1457646358,
1619135787,
1740390855,
1952476053,
1447330204,
1093890444,
1043395429,
1730117144,
1437197324,
1386748465,
1639106297,
1801878921,
1821254913,
1225352123,
1679867022,
1285829978,
1447640032,
1770540403,
1023465424,
1063687812,
1053639765,
1770573727,
1811943475,
1649611302,
1922179936,
1053739748,
1871576926,
1235190133,
1003234964,
1558398305,
1609091909,
1043321003,
1750588109,
1255616694,
1437131323,
1720061120,
1396883997,
1023007622,
1255499661,
1710049622,
1619929502,
1346637188,
1215356761,
1467420224,
1083828032,
1427292879,
1942283098,
1861735292,
1972700318,
1134109754,
1558790220,
1366499469,
1396734067,
1225270986,
1366640286,
1164798112,
1073804571,
1336245422,
1740539931,
1073683272,
1679741722,
1851487920,
1396746087,
1780754986,
1396835047,
1801972641,
1215195896,
1033203070,
1336361021,
1184811580,
1982048690,
1225456650,
1316380603,
1992899215,
1154427490,
1326141698,
1164416418,
1689084816,
1174550651,
1992747075,
1972526283,
1376606814,
1144383696,
1720180524,
1841618808
]
  

#for i in list:
#   response = npi.search(search_params={'number': i})
#    output_row = []
 #   column= response['results'][0]
  #  first_record = flatten(column)
   # df1 = pd.DataFrame.from_dict(first_record,orient='index').T
    ##   df = df1
    #else:
     #   df = pd.concat([df,df1], axis=0, ignore_index=True)
    
#df.to_csv('NPI_Export.csv')



i = 0
#Create loop
while i < len(list):
    response = npi.search(search_params={'number': list[i]})
    column= response['results'][0]
    record = flatten(column)
    data = pd.DataFrame.from_dict(record,orient='index').T
    if i == 0:
        df = data
    else:
        df = pd.concat([df,data], axis=0, ignore_index=True)
    i+=1
    
df.to_csv('NPI_Export.csv')
