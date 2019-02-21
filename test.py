import itertools  # allows importing of permutations

n = 1
while (n > 0):    #  0 would do nothing, and -1 is nothing to read
  n = int(input())
  if (n>0):
    all_permutations = list(itertools.permutations(range(n)))
##    # uncomment to see all the permutations
##    #
##    #for perm in all_permutations:
##    #  print(perm)
##
    print(len(all_permutations))
