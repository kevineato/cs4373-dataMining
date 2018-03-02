import itertools as it
import math
import pandas as pd

DEP = ['sales', 'systems', 'marketing', 'secretary']
AGE = ['21..25', '26..30', '31..35', '36..40', '41..45', '46..50']
SALARY = ['26k..30k', '31k..35k', '36k..40k', '41k..45k', '46k..50k', '66k..70k']
STATUS = ['junior', 'senior']

#  calculate 1 - sum(p_i ** 2)
def gini(set_counts):
    jun_prob_sq = (set_counts['junior'] / set_counts.sum()) ** 2
    sen_prob_sq = (set_counts['senior'] / set_counts.sum()) ** 2
    return 1 - jun_prob_sq - sen_prob_sq

df = pd.read_csv('hwk03.csv')
min_gini = 1.0
min_gini_set = ()

#  only need to examine half of combinations
max_len = math.floor(len(DEP) / 2)

for i in range(max_len):
    #  list possible combinations of attribute
    combos = list(it.combinations(DEP, i + 1))
    for t in combos:
        #  stop calculations after halfway through n choose n / 2 since rest is mirrored
        if i + 1 == max_len:
            if len(DEP) % 2 == 0 and t == combos[int(len(combos) / 2)]:
                break

        #  select attribute values from current set in dataframe
        dfin = df[df.department.isin(t)]
        #  select attribute values not in current set in dataframe
        dfnotin = df.mask(df.department.isin(t))

        #  number of junior/senior in dataframe for current selected set
        val_counts = dfin['status'].value_counts().reindex(STATUS, fill_value=0)
        #  number of junior/senior in dataframe for not in current set
        notval_counts = dfnotin['status'].value_counts().reindex(STATUS, fill_value=0)

        #  weighted probabilities for values in and not in current set
        in_prob = (val_counts.sum() / df.shape[0])
        notin_prob = (notval_counts.sum() / df.shape[0])

        #  construct strings for in and not in set probabilities
        in_prob_str = '{}/{}'.format(val_counts.sum(), df.shape[0])
        notin_prob_str = '{}/{}'.format(notval_counts.sum(), df.shape[0])

        #  calculate gini index
        gini_index = in_prob * gini(val_counts) + notin_prob * gini(notval_counts)
        #  construct strings for gini calculations done

        in_gini_str = '1 - ({}/{}) ** 2 - ({}/{}) ** 2'.format(val_counts['junior'], val_counts.sum(), val_counts['senior'], val_counts.sum())
        notin_gini_str = '1 - ({}/{}) ** 2 - ({}/{}) ** 2'.format(notval_counts['junior'], notval_counts.sum(), notval_counts['senior'], notval_counts.sum())

        #  print current attribute values chosen and gini index calculated
        print('{}: {}({}) + {}({}) = {:.4f}'.format(t, in_prob_str, in_gini_str, notin_prob_str, notin_gini_str, gini_index))
        #  update minimum gini obtained so far
        if gini_index < min_gini:
            min_gini = gini_index
            min_gini_set = t

#  repeat for column age
max_len = math.floor(len(AGE) / 2)

for i in range(max_len):
    combos = list(it.combinations(AGE, i + 1))
    for t in combos:
        if i + 1 == max_len:
            if len(AGE) % 2 == 0 and t == combos[int(len(combos) / 2)]:
                break
        dfin = df[df.age.isin(t)]
        dfnotin = df.mask(df.age.isin(t))

        val_counts = dfin['status'].value_counts().reindex(STATUS, fill_value=0)
        notval_counts = dfnotin['status'].value_counts().reindex(STATUS, fill_value=0)

        in_prob = (val_counts.sum() / df.shape[0])
        notin_prob = (notval_counts.sum() / df.shape[0])

        in_prob_str = '{}/{}'.format(val_counts.sum(), df.shape[0])
        notin_prob_str = '{}/{}'.format(notval_counts.sum(), df.shape[0])

        gini_index = in_prob * gini(val_counts) + notin_prob * gini(notval_counts)

        in_gini_str = '1 - ({}/{}) ** 2 - ({}/{}) ** 2'.format(val_counts['junior'], val_counts.sum(), val_counts['senior'], val_counts.sum())
        notin_gini_str = '1 - ({}/{}) ** 2 - ({}/{}) ** 2'.format(notval_counts['junior'], notval_counts.sum(), notval_counts['senior'], notval_counts.sum())

        print('{}: {}({}) + {}({}) = {:.4f}'.format(t, in_prob_str, in_gini_str, notin_prob_str, notin_gini_str, gini_index))
        if gini_index < min_gini:
            min_gini = gini_index
            min_gini_set = t

#  repeat for column salary
max_len = math.floor(len(SALARY) / 2)

for i in range(max_len):
    combos = list(it.combinations(SALARY, i + 1))
    for t in combos:
        if i + 1 == max_len:
            if len(SALARY) % 2 == 0 and t == combos[int(len(combos) / 2)]:
                break
        dfin = df[df.salary.isin(t)]
        dfnotin = df.mask(df.salary.isin(t))

        val_counts = dfin['status'].value_counts().reindex(STATUS, fill_value=0)
        notval_counts = dfnotin['status'].value_counts().reindex(STATUS, fill_value=0)

        in_prob = (val_counts.sum() / df.shape[0])
        notin_prob = (notval_counts.sum() / df.shape[0])

        in_prob_str = '{}/{}'.format(val_counts.sum(), df.shape[0])
        notin_prob_str = '{}/{}'.format(notval_counts.sum(), df.shape[0])

        gini_index = in_prob * gini(val_counts) + notin_prob * gini(notval_counts)

        in_gini_str = '1 - ({}/{}) ** 2 - ({}/{}) ** 2'.format(val_counts['junior'], val_counts.sum(), val_counts['senior'], val_counts.sum())
        notin_gini_str = '1 - ({}/{}) ** 2 - ({}/{}) ** 2'.format(notval_counts['junior'], notval_counts.sum(), notval_counts['senior'], notval_counts.sum())

        print('{}: {}({}) + {}({}) = {:.4f}'.format(t, in_prob_str, in_gini_str, notin_prob_str, notin_gini_str, gini_index))
        if gini_index < min_gini:
            min_gini = gini_index
            min_gini_set = t

#  print final minimum gini for all possible attributes/attribute values
print('Minimum: {} {:.4f}'.format(min_gini_set, min_gini))
