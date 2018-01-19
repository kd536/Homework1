

yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Harvard', 'UT', 'Rice']

ours1 = yours + mine
print(ours1)

ours2 = []
ours2.append(yours)
ours2.append(mine)
print(ours2)

# Ours1 differs from Ours2 in that Ours1 completely combines the two lists into one new list. Ours2 combines the lists,
# but displays it as the combination of two separate lists.
yours[1] = 'Princeton'

print(ours1)
print(ours2)
# Ours1 was created using the defined list for Yours, so it would not change to show the updated list.
# Ours2 uses append so it pulls in the new updated list.
