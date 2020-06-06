"""
@author : Shrikanth N C (nc.shrikanth@gmail.com)
Date: 15 Dec 2019
Script to assess  Mills-Jones Hypothesis (Belief 3)
License: See LICENSE file
"""

from plotly.graph_objs._deprecations import Annotation
from scipy.stats import *



from Constants import *

import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from PSPConstants import *

import pandas as pd

def computeCorrelation(X, Y):


    pearResult = pearsonr(X, Y)
    pearRho = pearResult[0]
    pearPValue = pearResult[1]

    spearResult = spearmanr(X, Y)
    spearRho = spearResult[0]
    spearPValue = spearResult[1]

    return [pearRho, pearPValue, spearRho,spearPValue]


def getProgrammingLanguages(df):

    return list(set(df[PROGRAMMINGLANGUAGE_COLNAME].values.tolist()))

# METRICS = ['P', 'E', 'DD' ,'LOC', 'T']
METRICS = ['Test Defects', 'Code Defects']

# fig = make_subplots(
#     rows=5, cols=2,
#     subplot_titles=('Defect Density Vs Program Size',
# 'Defect Density Vs Coding Time.png',
# 'Prgramming Experience Vs Defect Density',
# 'Prgramming Experience Vs Program Size',
# 'Prgramming Experience Vs Coding Time.png',
# 'Program Size Vs Coding Time.png',
# 'Productivity Vs Defect Density.png',
# 'Productivity Vs Prgramming Experience.png',
# 'Productivity Vs Program Size.png',
# 'Productivity Vs Coding Time.png'
#     ))


def computeMetric(xDF, metric):

    tempDF = pd.DataFrame()

    if metric == 'Code Defects':
        tempDF['temp'] =    xDF[ACTDEFINJCODE_COLNAME]
    elif metric == 'Test Defects':
        tempDF['temp'] =  xDF[ACTDEFREMTEST_COLNAME]
    else:
        float("error")

    return tempDF['temp'].values.tolist()

def deduceCorrelation(xDF, xMetric, yMetric):

    pearRho, pearPValue, spearRho, spearPValue = computeCorrelation(computeMetric(xDF, xMetric), computeMetric(xDF, yMetric))

    if spearPValue < SIG_LEVEL:
        return spearRho
    else:
        return 0


def exportBoxPlot():



    df = getPSPDF()

    programmingLanguageDF = pd.DataFrame()

    rowIndex = 1
    colIndex = 1
    outputStr = '**** \t Output \t *****\n\n'
    for i in range(0, len(METRICS)):

        for j in range((i+1), len(METRICS)):

            if i == j:
                continue

            annotationList = []
            xMetric = METRICS[i]
            yMetric = METRICS[j]

            label = 'ρ ( X , Y )'

            plCol = []
            paCol = []

            local_boxplot_data = []
            xIndex = 0

            for pl in PROGRAMMING_LANGUAGES:

                columnValues = []

                plDF = df[df[PROGRAMMINGLANGUAGE_COLNAME] == pl]


                for pa in PROGRAM_ASSIGNMENT_LIST_ALL:

                    pl_paDF = plDF[plDF[PROGRAMASSIGNMENT_COLNAME] == pa]


                    columnValues.append(deduceCorrelation(pl_paDF, xMetric, yMetric))
                    plCol.append(pl)
                    paCol.append(pa)


                if 'time' in xMetric or 'time' in yMetric:
                    bcolor = blue
                else:
                    bcolor = orange

                outputStr += pl + " median = " + str(np.median(columnValues)) + " values = " + str(columnValues) +"\n"
                local_boxplot_data.append(go.Box(fillcolor=bcolor,
                                                 marker=dict(color=black),
                                                 y=columnValues,
                                                 name="<b>" + pl, showlegend=False, orientation="v", line_width=3,
                                                 width=0.25))

                annotationList.append(Annotation(
                x=xIndex,
                y=np.median(columnValues),
                text='',
                    arrowcolor="black",
                    arrowsize=3,
                    arrowwidth=1,
                    arrowhead=1
            ))
                xIndex += 1
                # fig.add_trace(,
                #         row= rowIndex, col=colIndex)

                if colIndex == 2:
                    colIndex = 1
                    rowIndex += 1
                else:
                    colIndex += 1

            programmingLanguageDF[label] = columnValues



            # if i == len(METRICS) - 2:
            #     programmingLanguageDF['Language'] = plCol
            #     programmingLanguageDF['PA'] = paCol

            fileName = ""+xMetric + '-' + yMetric

            try:
                plot_boxes(local_boxplot_data,annotationList, "img_P-DD.png" ,
               '',
               label+"", 0, 1)
                print(outputStr)
            except:
                print(outputStr)





def plot_boxes(data, annotationList, filename ,xaxisLabel, yAxisLabel, firstLine, secondLine):

    xAxisTitle = '<br> '+xaxisLabel

    from plotly.graph_objs._deprecations import Annotations
    layout = go.Layout(
        # plot_bgcolor= '#e8eaed',
        plot_bgcolor='#FFFFFF',
        autosize=False,

        title='',

        margin=dict(l=110, r=10, t=15, b=50),

        xaxis=dict(
            title='<b>' + xAxisTitle,
            automargin=False,
            # range=[-1, 1],
            titlefont=dict(
                family=FONT_NAME,
                size=FONT_SIZE,
                color='#000000'  # 7f7f7f'
            ), tickfont=dict(
                family=FONT_NAME,
                size=FONT_SIZE
                # color='blue'
            ),
            showgrid=True,
            zeroline=False,
            showline=True,
            # mirror='ticks',
            # gridcolor='#bdbdbd',
            gridwidth=0.5,

            zerolinecolor='#000000',
            zerolinewidth=0.5,
            linecolor='#000000',
            linewidth=1

        ),
        yaxis=dict(
            title="<b> "+yAxisLabel ,
            automargin=False,
            range=[0, 1],
            showgrid=True,
            zeroline=False,
            showline=True,
            showticklabels=True,

            gridwidth=0.5,
            gridcolor='#bdbdbd',
            zerolinecolor='#000000',
            zerolinewidth=0.5,
            linecolor='#000000',
            linewidth=1,
            titlefont=dict(
                family=FONT_NAME,
                size=FONT_SIZE,
                # color=color_blue
            ), tickfont=dict(
                family=FONT_NAME,
                size=FONT_SIZE
                # color='blue'
            )
        ),

        # annotations=Annotations(annotationList)

    )


    fig = go.Figure(data=data, layout=layout)

    maxY = 0

    i= 0
    while i < len(data):
       tY = max(maxY, max(data[i].y))

       if math.inf != tY:
            maxY = tY

       i+=1


    pio.write_image(fig, "./png/"+filename, scale=4)
    print("Belief 4 correlation distribution (box-plot) exported to  :  ./png/"+filename)

if __name__ == '__main__':

    exportBoxPlot()