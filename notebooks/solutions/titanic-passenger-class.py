# First look at what the values are with:
print(train_df['Pclass'].value_counts())

print('Passenger class 1')
survival_report(train_df[train_df['Pclass'] == 1])

print('Passenger class 2')
survival_report(train_df[train_df['Pclass'] == 2])

print('Passenger class 3')
survival_report(train_df[train_df['Pclass'] == 3])

# Bonus: or do a loop to do the work for us:
# counts = train_df['Pclass'].value_counts()
# for value in counts.keys():
#     print('\nPassenger class: {}'.format(value))
#     survival_report(train_df[train_df['Pclass'] == value])
