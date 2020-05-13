"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Apprentice law (Belief 5)
License: Proprietary
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

    tempDF['productivity'] = pdf[ACTLOC_COLNAME] / (
            (pdf[ACTMIN_COLNAME] - (pdf[ACTMINPLAN_COLNAME] + pdf[ACTMINDSGN_COLNAME])) / 60)

    # tempDF['productivity'] = pdf[ACTLOC_COLNAME]/ (pdf[ACTMIN_COLNAME]/ 60)

    samples = tempDF['productivity'].values.tolist()

    if filter:
        samples = filterNumeric(samples)

    return samples

def generateProductivityExpertNovice():

    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2)]

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_ProductivityExpertNovice.txt'
    remove(output_file_name)

    appendTreatment(output_file_name, 'expert', calculateProductivity(expertDF))
    appendTreatment(output_file_name, 'novice', calculateProductivity(noviceDF))



def calculateDD(pdf, filter=True):

    tempDF = pd.DataFrame()

    tempDF['defect-density'] = pdf[ACTDEFINJCODE_COLNAME] / (pdf[ACTLOC_COLNAME] / 1000)
    samples = tempDF['defect-density'].values.tolist()

    if filter:
        samples = filterNumeric(samples)

    return samples

def generateDefectDensityExpertNovice():
    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2)]

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_DefectDensityExpertNovice.txt'
    remove(output_file_name)

    appendTreatment(output_file_name, 'expert', calculateDD(expertDF))
    appendTreatment(output_file_name, 'novice', calculateDD(noviceDF))


def generateProductivityExpertNoviceGroupedByProgrammingLanguage():
    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2)]

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_ProductivityExpertNoviceGroupedByProgrammingLanguage.txt'
    remove(output_file_name)

    for p in PROGRAMMING_LANGUAGES:

        plExpertDF = expertDF[ expertDF[PROGRAMMINGLANGUAGE_COLNAME] == p]
        plNoviceDF = noviceDF[noviceDF[PROGRAMMINGLANGUAGE_COLNAME] == p]

        appendTreatment(output_file_name, p+'_expert', calculateProductivity(plExpertDF))
        appendTreatment(output_file_name, p+'_novice', calculateProductivity(plNoviceDF))


def generateDefectDensityExpertNoviceGroupedByProgrammingLanguage():
    df = getPSPDF()
    pspDF = df[df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2)]

    expertDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] >= 3)]
    noviceDF = pspDF[(pspDF[YEARSPROGRAMMINGEXPERIENCE_COLNAME] < 3)]

    output_file_name = 'belief_5_DefectDensityExpertNoviceGroupedByProgrammingLanguage.txt'
    remove(output_file_name)

    for p in PROGRAMMING_LANGUAGES:
        plExpertDF = expertDF[expertDF[PROGRAMMINGLANGUAGE_COLNAME] == p]
        plNoviceDF = noviceDF[noviceDF[PROGRAMMINGLANGUAGE_COLNAME] == p]

        appendTreatment(output_file_name, p + '_expert', calculateDD(plExpertDF))
        appendTreatment(output_file_name, p + '_novice', calculateDD(plNoviceDF))


if __name__ == '__main__':

    generateProductivityExpertNovice()
    generateDefectDensityExpertNovice()

    generateProductivityExpertNoviceGroupedByProgrammingLanguage()
    generateDefectDensityExpertNoviceGroupedByProgrammingLanguage()
