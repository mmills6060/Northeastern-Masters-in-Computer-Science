# Write a function that, given a set, uses two of the set functions on the set.  
# They should be logical functions to use.

def set_functions(firstset):
    # Create another set to use for set operations
    secondset = {1, 2, 3}
    
    # Determine the union between firstset and secondset
    union_set = firstset.union(secondset)
    print("Union of firstset and secondset:", union_set)
    
    # Check if firstset is a superset of secondset
    is_superset = firstset.issuperset(secondset)
    if is_superset:
        print("firstset is a superset of secondset")
    else:
        print("firstset is not a superset of secondset")
