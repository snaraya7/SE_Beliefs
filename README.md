# Assessing Software Engineering Beliefs

Software engineering is a highly dynamic discipline. Hence, as times change, sotoo might our beliefs about core processes in this field.This paper checks some five beliefs originated in the past decades that comment onthe relationships between (i) developer productivity; (ii) software quality and (ii) years ofdeveloper experience.Using  data  collected  from  1,356  developers  in  the  period  1995  to  2006,  we  foundsupport for only one of those five beliefs; specifically: (1) “Quality entails productivity” andconditional support for a belief titled (2) “Object-oriented programming reduces errors andencourages reuse” (due to C++’s debatable OO support). We found no support for three otherbeliefs including (3) “It takes 5000 hours to turn a novice into an expert”, (4) “Productivityand reliability depend on the length of a program’s text, independent of language levelused”; and (5) “individual developer performance varies considerably”. We also learnedthat developers were more productive and induced fewer defects in writing programs usingmodern programming languages like C#.The overall message of this work, is that it is both important and possible to revisit oldbeliefs in SE. Researchers and practitioners should routinely and regularly revisit and retestold beliefs.

## To reproduce results, see command-line execution instructions (Windows OS) below:

```
Requires: Python3 (to execute .py files) and Python2 (to execute .bat files)
```

### Belief 1

1. python [belief1.py](belief1.py)
2. [belief1.bat](belief1.bat)
3. Generates the following tables (as seen in the paper)
* [belief_1_defect-density.txt](results/sk_belief_1_defect-density.txt)
* [belief_1_LOC.txt](results/sk_belief_1_LOC.txt)
* [belief_1_productivity.txt](results/sk_belief_1_productivity.txt)

### Belief 2

1. python [belief2.py](belief2.py)
2. [belief2.bat](belief2.bat)
3. Generates the following tables (as seen in the paper)
* [belief_2_defect-density.txt](results/sk_belief_2_defect-density.txt)
* [belief_2_defect-density_all_assignments.txt](results/sk_belief_2_defect-density_all_assignments.txt)

### Belief 3

1. python [belief3.py](belief3.py)
2. Generates the box-plot image and prints equivalent results in console
* [img_belief3_P-DD.png](png/img_belief3_P-DD.png) (This requires plotly package) alternatively see equivalent results in console
* See console output

### Belief 4

1. python [belief1.py](belief1.py)
2. [belief1.bat](belief1.bat)
3. Generates the following tables (as seen in the paper)
* [belief_4_DefectDensityGroupedByTask10CompletedByProgrammingLanguages.txt](results/sk_belief_4_DefectDensityGroupedByTask10CompletedByProgrammingLanguages.txt)
* [belief_4_ProductivityGroupedByProgrammingLanguages.txt] (results/sk_belief_4_ProductivityGroupedByProgrammingLanguages.txt)
* [belief_4_ProductivityGroupedByTask10CompletedByProgrammingLanguages.txt](results/sk_belief_4_ProductivityGroupedByTask10CompletedByProgrammingLanguages.txt)
* [belief_4_ProductivityGroupedByTasks.txt](results/sk_belief_4_ProductivityGroupedByTasks.txt)

### Belief 5

1. python [belief5.py](belief5.py)
2. [belief5.bat](belief1.bat)
3. Generates the following tables (as seen in the paper)
* [belief_5_DefectDensityExpertNovice.txt](results/sk_belief_5_DefectDensityExpertNovice.txt)
* [belief_5_DefectDensityExpertNoviceGroupedByProgrammingLanguage.txt (results/sk_belief_5_DefectDensityExpertNoviceGroupedByProgrammingLanguage.txt)
* [belief_5_ProductivityExpertNovice.txt](results/sk_belief_5_ProductivityExpertNovice.txt)
* [belief_5_ProductivityExpertNoviceGroupedByProgrammingLanguage.txt](results/sk_belief_5_ProductivityExpertNoviceGroupedByProgrammingLanguage.txt)

```
For technical support e-mail Shrikanth N C (nc.shrikanth@gmail.com) with subject `SE Beliefs repository queries'
```
