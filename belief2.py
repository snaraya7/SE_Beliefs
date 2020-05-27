"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Dahl-Goldberg Hypothesis (Belief 2)
License: See LICENSE file
"""

from PSPConstants import *
from results_generator import *

import pandas as pd


def getProgrammingLanguages(df):

    return list(set(df[PROGRAMMINGLANGUAGE_COLNAME].values.tolist()))

def generate(measure, assignments, programminglanguages, prefix):

    output_file_name = "belief_2_"+measure + ""+prefix+ '.txt'

    remove(output_file_name)

    df = getPSPDF()

    df = df  [ df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2) ]
    for pa in assignments:

        if pa is not None:
            pspDF = df[ df[PROGRAMASSIGNMENT_COLNAME] == pa ]
        else:
            pspDF = df



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

            if pa is not None:
                pp = pa
                appendTreatment(output_file_name, "$"+pp+"_{"+ppl+"}$", samples)
            else:
                appendTreatment(output_file_name, "$" +  "{" + ppl + "}$", samples)


if __name__ == '__main__':

    generate('defect-density', [None], PROGRAMMING_LANGUAGES, '_all_assignments')
    generate('defect-density', PROGRAM_ASSIGNMENT_LIST_LEVEL2, ['C', 'C++'], "")





