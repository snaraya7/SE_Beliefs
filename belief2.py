"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Dahl-Goldberg Hypothesis (Belief 2)
License: See LICENSE file
"""

from PSPConstants import *
from results_generator import *

import pandas as pd

def generate(assignments):

    if len(assignments) == 1:
        output_file_name = 'belief_2_Task10.txt'
    else:
        output_file_name = 'belief_2.txt'

    remove(output_file_name)

    df = getPSPDF()

    df = df  [ df[PROGRAMASSIGNMENT_COLNAME].isin(assignments) ]

    globalMin = min(df[ACTDEFINJCODE_COLNAME]  + df[ACTDEFINJDSGN_COLNAME])
    globalMax = max(df[ACTDEFINJCODE_COLNAME]  + df[ACTDEFINJDSGN_COLNAME])

    for pl in PROGRAMMING_LANGUAGES:

        plDF = df[df[PROGRAMMINGLANGUAGE_COLNAME] == pl]

        tempDF = pd.DataFrame()

        tempDF['defects'] = plDF[ACTDEFINJCODE_COLNAME]  + plDF[ACTDEFINJDSGN_COLNAME]

        samples = tempDF['defects'].values.tolist()

        samples = normalize(samples, globalMin, globalMax)

        ppl = pl

        if pl == 'C#':
            ppl = 'C\#'

        if len(assignments) == 1:
            appendTreatment(output_file_name, ppl + "_10", samples)
        else:
            appendTreatment(output_file_name, ppl, samples)



if __name__ == '__main__':

    generate(PROGRAM_ASSIGNMENT_LIST_LEVEL0)
    generate(['10A'])