"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess Sackman’s Second law (Belief 4)
License: See LICENSE file
"""

from PSPConstants import *
from results_generator import *

import pandas as pd


def calculateProductivity(df):

    # return df[ACTLOC_COLNAME] / (df[ACTMIN_COLNAME] / 60)
    #
    return df[ACTLOC_COLNAME] / ((df[ACTMIN_COLNAME] - (df[ACTMINPLAN_COLNAME] + df[ACTMINDSGN_COLNAME])) / 60)

def generateProductivityGroupedByTasks():

    measure = 'productivity'
    output_file_name = 'belief_4_ProductivityGroupedByTasks.txt'
    remove(output_file_name)

    df = getPSPDF()
    print( "after 1 ", len(df))
    df = df[ df[PROGRAMMINGLANGUAGE_COLNAME].isin(PROGRAMMING_LANGUAGES)]
    print( "after  2", len(df))
    df = df[ df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2)]
    print( "after  3", len(df))

    for pa in PROGRAM_ASSIGNMENT_LIST_LEVEL2:

        pspDF = df[ df[PROGRAMASSIGNMENT_COLNAME] == pa]

        tempDF = pd.DataFrame()

        tempDF[measure] = calculateProductivity(pspDF)

        samples = tempDF[measure].values.tolist()

        pp = pa
        appendTreatment(output_file_name, "$" + pp + "$", samples)


def generateProductivityGroupedByProgrammingLanguages():

    measure = 'productivity'
    output_file_name = 'belief_4_ProductivityGroupedByProgrammingLanguages.txt'
    remove(output_file_name)

    df = getPSPDF()
    df = df[ df[PROGRAMASSIGNMENT_COLNAME].isin(PROGRAM_ASSIGNMENT_LIST_LEVEL2) ]

    for pa in PROGRAMMING_LANGUAGES:

        pspDF = df[df[PROGRAMMINGLANGUAGE_COLNAME] == pa]

        tempDF = pd.DataFrame()

        tempDF[measure] = calculateProductivity(pspDF)

        samples = tempDF[measure].values.tolist()

        pp = pa
        appendTreatment(output_file_name, "$" + pp + "$", samples)


def generateProductivityGroupedByTask10CompletedByProgrammingLanguages():
    measure = 'productivity'
    output_file_name = 'belief_4_ProductivityGroupedByTask10CompletedByProgrammingLanguages.txt'
    remove(output_file_name)

    df = getPSPDF()
    df = df[df[PROGRAMASSIGNMENT_COLNAME].isin(['10A'])]

    for pa in PROGRAMMING_LANGUAGES:
        pspDF = df[df[PROGRAMMINGLANGUAGE_COLNAME] == pa]

        tempDF = pd.DataFrame()

        tempDF[measure] = calculateProductivity(pspDF)

        samples = tempDF[measure].values.tolist()

        pp = pa
        appendTreatment(output_file_name, "$10" + pp + "$", samples)


def generateDefectDensityGroupedByTask10CompletedByProgrammingLanguages():
    measure = 'defect-density'
    output_file_name = 'belief_4_DefectDensityGroupedByTask10CompletedByProgrammingLanguages.txt'
    remove(output_file_name)

    df = getPSPDF()
    df = df[df[PROGRAMASSIGNMENT_COLNAME].isin(['10A'])]

    for pa in PROGRAMMING_LANGUAGES:
        pspDF = df[df[PROGRAMMINGLANGUAGE_COLNAME] == pa]

        tempDF = pd.DataFrame()

        tempDF[measure] = pspDF[ACTDEFINJCODE_COLNAME] / (pspDF[ACTLOC_COLNAME] / 1000)

        samples = tempDF[measure].values.tolist()

        pp = pa
        appendTreatment(output_file_name, "$10" + pp + "$", samples)



if __name__ == '__main__':

    generateProductivityGroupedByTasks()
    generateProductivityGroupedByProgrammingLanguages()
    generateProductivityGroupedByTask10CompletedByProgrammingLanguages()
    generateDefectDensityGroupedByTask10CompletedByProgrammingLanguages()








