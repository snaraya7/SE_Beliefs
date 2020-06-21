# Assessing Software Engineering Beliefs

Software engineering is a highly dynamic discipline. Hence, as times change, so too might our beliefs about core processes in this field. This paper checks some five beliefs that originated in the past decades that comment on the relationships between (i) developer productivity; (ii) software quality and (iii) years of developer experience. Using data collected from 1,356 developers in the period 1995 to 2006, we found support for only one of the five beliefs titled “Quality entails productivity”. We found no clear support for four other beliefs based on programming languages and software developers. However, from the sporadic evidence of the four other beliefs we learned that a narrow scope could delude practitioners in misinterpreting certain effects to hold in their day to day work. Lastly, through an aggregated view of assessing the five beliefs, we find programming languages act as a confounding factor for developer productivity and software quality. Thus the overall message of this work is that it is both important and possible to revisit old beliefs in SE. Researchers and practitioners should routinely retest old beliefs.

## To reproduce results, see command-line execution instructions (Windows OS) below:

```
Requires: Python3 (to execute .py files) and Python2 (to execute .bat files)
```

### Belief 1

1. python [belief1.py](belief1.py)
2. [belief1.bat](belief1.bat)

### Belief 2

1. python [belief2.py](belief2.py)
2. [belief2.bat](belief2.bat)

### Belief 3

1. python [belief3.py](belief3.py)
2. Prints the required results to the console. To generate the box-plot (as shown in the paper) run [belief3_box_plot.py](belief3_box_plot.py) (but this requires the installation of plotly module and its dependencies).

### Belief 4

1. python [belief4.py](belief4.py)
2. [belief4.bat](belief4.bat)

### Belief 5

1. python [belief5.py](belief5.py)
2. [belief5.bat](belief1.bat)

In Summary, each beliefX.py generates a set of intermediate .txt files. Then running the corresponding beliefX.bat file reads those generated .txt files and writes the results to the SE_Beliefs/results/ folder (except belief 3).     


```
For technical support e-mail Shrikanth N C (nc.shrikanth@gmail.com) with subject `SE Beliefs repository queries'
```
