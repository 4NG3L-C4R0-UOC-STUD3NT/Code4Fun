# https://realpython.com/logistic-regression-python/

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

model = LogisticRegression(solver='liblinear', random_state=0)

model.fit(x, y)

model2 = LogisticRegression(solver='liblinear', random_state=0).fit(x, y)

model2.classes_
model2.intercept_
model2.coef_

model2.predict_proba(x)

model2.predict(x)

model2.score(x, y)

confusion_matrix(y, model.predict(x))

cm = confusion_matrix(y, model.predict(x))

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
plt.show()

print(classification_report(y, model2.predict(x)))


model3 = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model3.fit(x, y)
model3.intercept_
model3.coef_
model3.predict_proba(x)
model3.predict(x)
model3.score(x, y)
confusion_matrix(y, model3.predict(x))
print(classification_report(y, model3.predict(x)))







