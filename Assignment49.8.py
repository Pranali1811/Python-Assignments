actual = [1, 1, 1, 1, 0, 0, 0, 0]
predicted = [1, 1, 0, 1, 0, 1, 0, 0]

TP = 0
TN = 0
FP = 0
FN = 0

for a, p in zip(actual, predicted):

    if a == 1 and p == 1:
        TP += 1

    elif a == 0 and p == 0:
        TN += 1

    elif a == 0 and p == 1:
        FP += 1

    elif a == 1 and p == 0:
        FN += 1

print("TP =", TP)
print("TN =", TN)
print("FP =", FP)
print("FN =", FN)