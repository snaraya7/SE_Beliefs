"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Apprentice law (Belief 5)
License: See LICENSE file
"""

from PSPConstants import *
from results_generator import *

import pandas as pd

def percentage(numer, denom):

    if denom > 0:
        return float(numer*100/denom)
    else:
        return 0

def filterNumeric(samples):

    count = 0

    ss = []
    for s in samples:

        if str(s) == 'inf':
            ss.append(1000)
            print("appending ", 1000)
            count += 1
        elif str(s) == 'nan':
            ss.append(-1)
            print("appending ", -1)
            count += 1
        else:
            ss.append(s)

    per = percentage(count,len(samples))
    if  per  > 5:
        assert 1 == 0


    # print("\% replaced ", per, count )

    return ss

def calculateProductivity(pdf, filter=True):
    tempDF = pd.DataFrame()

    tempDF['production-rate'] =  pdf[ACTLOC_COLNAME] / (pdf[ACTMIN_COLNAME]/60)

    samples = tempDF['production-rate'].values.tolist()


    # if filter:
    #     samples = filterNumeric(samples)

    return samples

def generateProductivityExpertNovice():

    df = getPSPDF()

    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_ALL)]

    globalMin = min(pspDF[ACTLOC_COLNAME] / (pspDF[ACTMIN_COLNAME] / 60))
    globalMax = max(pspDF[ACTLOC_COLNAME] / (pspDF[ACTMIN_COLNAME] / 60))

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_ProductivityExpertNovice.txt'
    remove(output_file_name)

    appendTreatment(output_file_name, 'expert', normalize(calculateProductivity(expertDF), globalMin, globalMax))
    appendTreatment(output_file_name, 'novice', normalize(calculateProductivity(noviceDF), globalMin, globalMax))



def calculateDD(pdf, filter=True):

    tempDF = pd.DataFrame()

    tempDF['defect-density'] = pdf[ACTDEFINJCODE_COLNAME] #/ (pdf[ACTLOC_COLNAME] / 1000)

    samples = tempDF['defect-density'].values.tolist()

    # if filter:
    #     samples = filterNumeric(samples)

    return samples

def generateDefectDensityExpertNovice():
    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_ALL)]

    globalMin = min(pspDF[ACTDEFINJCODE_COLNAME])
    globalMax = max(pspDF[ACTDEFINJCODE_COLNAME])


    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_DefectDensityExpertNovice.txt'
    remove(output_file_name)

    appendTreatment(output_file_name, 'expert', normalize(calculateDD(expertDF), globalMin, globalMax))
    appendTreatment(output_file_name, 'novice', normalize(calculateDD(noviceDF), globalMin, globalMax))


def generateProductivityExpertNoviceGroupedByProgrammingLanguage():
    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_ALL)]

    globalMin = min(pspDF[ACTLOC_COLNAME] / (pspDF[ACTMIN_COLNAME] / 60))
    globalMax = max(pspDF[ACTLOC_COLNAME] / (pspDF[ACTMIN_COLNAME] / 60))

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_ProductivityExpertNoviceGroupedByProgrammingLanguage.txt'
    remove(output_file_name)

    for p in PROGRAMMING_LANGUAGES:

        plExpertDF = expertDF[ expertDF[PROGRAMMINGLANGUAGE_COLNAME] == p]
        plNoviceDF = noviceDF[noviceDF[PROGRAMMINGLANGUAGE_COLNAME] == p]

        appendTreatment(output_file_name, p+'_expert', normalize(calculateProductivity(plExpertDF), globalMin, globalMax))
        appendTreatment(output_file_name, p+'_novice', normalize(calculateProductivity(plNoviceDF), globalMin, globalMax))


def generateDefectDensityExpertNoviceGroupedByProgrammingLanguage():
    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_ALL)]

    globalMin = min(pspDF[ACTDEFINJCODE_COLNAME])
    globalMax = max(pspDF[ACTDEFINJCODE_COLNAME])

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_DefectDensityExpertNoviceGroupedByProgrammingLanguage.txt'
    remove(output_file_name)

    for p in PROGRAMMING_LANGUAGES:
        plExpertDF = expertDF[expertDF[PROGRAMMINGLANGUAGE_COLNAME] == p]
        plNoviceDF = noviceDF[noviceDF[PROGRAMMINGLANGUAGE_COLNAME] == p]

        appendTreatment(output_file_name, p + '_expert', normalize(calculateDD(plExpertDF), globalMin, globalMax))
        appendTreatment(output_file_name, p + '_novice', normalize(calculateDD(plNoviceDF), globalMin, globalMax))


if __name__ == '__main__':

    generateProductivityExpertNovice()
    generateDefectDensityExpertNovice()

    generateProductivityExpertNoviceGroupedByProgrammingLanguage()
    generateDefectDensityExpertNoviceGroupedByProgrammingLanguage()



