# Authors: Shrikanth N C <snaraya7@ncsu.edu>
# Date: 15th December 2019
# License: See LICENSE file

import pandas as pd
from PSPConstants import *



PROGRAMMINGLANGUAGE_COLNAME = 'ProgrammingLanguage'
ACTMINCODE_COLNAME = 'ActMinCode'

def getPSPDF():

    PSP_MAIN_DF = pd.read_csv('C:/Users/ncshr/PycharmProjects/SE_Beliefs/data/filtered_data.csv')
    # # PSP_MAIN_DF[PROGRAMMINGLANGUAGE_COLNAME] = PSP_MAIN_DF[PROGRAMMINGLANGUAGE_COLNAME].map({'POWERBUILDER': 'PB'})
    # PSP_MAIN_DF[PROGRAMMINGLANGUAGE_COLNAME] = PSP_MAIN_DF[PROGRAMMINGLANGUAGE_COLNAME].replace('POWERBUILDER','PB')
    # PSP_MAIN_DF[PROGRAMMINGLANGUAGE_COLNAME] = PSP_MAIN_DF[PROGRAMMINGLANGUAGE_COLNAME].replace('PROGRESS', 'PRGS')
    # PSP_MAIN_DF[ACTMINCODE_COLNAME] = PSP_MAIN_DF[ACTMINCODE_COLNAME].replace(1735, 221)
    return PSP_MAIN_DF

#
# if __name__ == '__main__':
#
#     df = getPSPDF()
#
#     df = df[ df[PROGRAMMINGLANGUAGE_COLNAME].isin(PROGRAMMING_LANGUAGES) ]
#
#     df.to_csv('filtered_data.csv', index=False)




