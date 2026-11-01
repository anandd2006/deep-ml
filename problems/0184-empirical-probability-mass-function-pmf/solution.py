def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    m={}
    for x in samples:
        m[x]=m.get(x,0)+1
    ans=[]
    for key,value in m.items():
        ans.append((key,value/len(samples)))
    ans.sort()
    return ans
        