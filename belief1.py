"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Corbat́o’s law (Belief 1)
License: See LICENSE file
"""

from PSPConstants import *
from results_generator import *

import pandas as pd


def getGlobal(df, measure):

    globalDF = pd.DataFrame()

    globalDF['production-rate'] = df[ACTLOC_COLNAME] / (df[ACTMIN_COLNAME] / 60)
    globalDF['LOC'] = df[ACTLOC_COLNAME]
    globalDF['defects'] = df[ACTDEFINJCODE_COLNAME]

    if measure == 'production-rate':
        return globalDF['production-rate'].min(), globalDF['production-rate'].max()
    elif measure == 'LOC':
        return globalDF['LOC'].min(), globalDF['LOC'].max()
    elif measure == 'defects':
        return globalDF['defects'].min(), globalDF['defects'].max()
    else:
        float('error')


def generate(measure, assignments, programminglanguages):

    output_file_name = "belief_1_"+measure+ '.txt'

    remove(output_file_name)

    df = getPSPDF()

    gDF = df[ (df[PROGRAMASSIGNMENT_COLNAME].isin(assignments)) & (df[PROGRAMMINGLANGUAGE_COLNAME].isin(programminglanguages))]
    globalMin , globalMax  = getGlobal(gDF, measure)

    # print(globalMin, globalMax, measure)


    for pa in assignments:

            pspDF = df[df[PROGRAMASSIGNMENT_COLNAME] == pa]

            pLanguageS = programminglanguages

            for pl in pLanguageS:

                pl_paDF = pspDF[pspDF[PROGRAMMINGLANGUAGE_COLNAME] == pl]
                tempDF = pd.DataFrame()

                tempDF['production-rate'] =   pl_paDF[ACTLOC_COLNAME] / (pl_paDF[ACTMIN_COLNAME]/60)
                tempDF['LOC'] = pl_paDF[ACTLOC_COLNAME]
                tempDF['defects'] = pl_paDF[ACTDEFINJCODE_COLNAME]



                ppl = pl

                if pl == 'C#':
                    ppl  = 'C\#'

                pp = pa


                samples = tempDF[measure].values.tolist()

                samples = normalize(samples, globalMin, globalMax)

                appendTreatment(output_file_name, pp+"_"+ppl, samples)


if __name__ == '__main__':

    generate('LOC', PROGRAM_ASSIGNMENT_LIST_LEVEL2, ['C', 'C#'] )
    generate('production-rate', ['10A'], ['C', 'C#'])
    generate('defects', ['10A'], ['C', 'C#'])





