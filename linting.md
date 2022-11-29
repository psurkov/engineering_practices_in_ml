``` 
❯ flake8 --max-expression-complexity=4 --max-cognitive-complexity=4 src
src/DecisionTree.py:18:9: ECE001 Expression is too complex (5.0 > 4)
src/DecisionTreeClassifier.py:64:9: ECE001 Expression is too complex (5.0 > 4)
src/DecisionTreeClassifier.py:95:17: ECE001 Expression is too complex (5 > 4)
src/DecisionTreeClassifier.py:104:9: ECE001 Expression is too complex (6.5 > 4)
src/DecisionTreeClassifier.py:105:9: ECE001 Expression is too complex (6.5 > 4)
src/DecisionTreeClassifier.py:130:9: R505 unnecessary else after return statement.
src/visualization.py:8:5: R505 unnecessary else after return statement.
src/visualization.py:46:1: CCR001 Cognitive complexity is too high (5 > 4)
src/visualization.py:51:9: ECE001 Expression is too complex (5.5 > 4)
src/visualization.py:52:9: ECE001 Expression is too complex (5.0 > 4)
src/visualization.py:56:9: ECE001 Expression is too complex (5.0 > 4)
src/visualization.py:78:1: CCR001 Cognitive complexity is too high (6 > 4)
src/visualization.py:81:13: ECE001 Expression is too complex (4.5 > 4)
src/visualization.py:86:13: ECE001 Expression is too complex (4.5 > 4)
src/visualization.py:115:5: ECE001 Expression is too complex (6.5 > 4)
```
Много проблем 🥲
