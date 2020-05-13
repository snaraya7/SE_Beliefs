"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Corbat́o’s law (Belief 1)
License: Proprietary
"""

from PSPConstants import *
from results_generator import *

import pandas as pd


def getProgrammingLanguages(df):

    return list(set(df[PROGRAMMINGLANGUAGE_COLNAME].values.tolist()))

def generate(measure, assignments, programminglanguages):

    output_file_name = "belief_1_"+measure+ '.txt'

    remove(output_file_name)

    df = getPSPDF()

    for pa in assignments:

            pspDF = df[df[PROGRAMASSIGNMENT_COLNAME] == pa]

            pLanguageS = programminglanguages

            for pl in pLanguageS:

                pl_paDF = pspDF[pspDF[PROGRAMMINGLANGUAGE_COLNAME] == pl]
                tempDF = pd.DataFrame()

                tempDF['productivity'] = pl_paDF[ACTLOC_COLNAME]/( (pl_paDF[ACTMIN_COLNAME] - ( pl_paDF[ACTMINPLAN_COLNAME] + pl_paDF[ACTMINDSGN_COLNAME]) )/60 )
                tempDF['LOC'] = pl_paDF[ACTLOC_COLNAME]
                tempDF['defect-density'] = pl_paDF[ACTDEFINJCODE_COLNAME]/ ( pl_paDF[ACTLOC_COLNAME] /1000)

                samples = tempDF[measure].values.tolist()

                ppl = pl

                if pl == 'C#':
                    ppl  = 'C\#'

                pp = pa
                appendTreatment(output_file_name, "$"+pp+"_{"+ppl+"}$", samples)


if __name__ == '__main__':

    generate('LOC', PROGRAM_ASSIGNMENT_LIST_LEVEL2, ['C', 'C#'])
    generate('productivity', ['10A'], ['C', 'C#'])
    generate('defect-density', ['10A'], ['C', 'C#'])





