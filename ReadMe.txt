    All ASCII characters have numerical values. 
    The winder (and therefore, unwinder) function uses
    those values to find how the indexes of each character
    have been shifted.
    
    Assume:
    A = 2
    B = 3
    C = 4
    D = 5
    
    Dog Code of "ABCD"
    
    Index     |    0   |   I    |   II   |   III   |
    ----------|--------|--------|--------|---------|
    Character |    A   |    B   |    C   |    D    |
    ----------|--------|--------|--------|---------|
    Value     |    2   |    3   |    4   |    5    |
    
    To wind a code, start at the first index, 0. 
    Looking one index ahead, I, its character B has a value of 3.
    With this, we add our current index to the value of the next index.
    Therefore, 0 + 3 (0 + 3), III (3).
    The number after the addition is the index that our current character needs to swap with.
    So, swap 0 and III, A and B. 
    
    Index     |    0   |    I   |   II   |   III   |
    ----------|--------|--------|--------|---------|
    Character |   *D   |    B   |    C   |   *A    |
    ----------|--------|--------|--------|---------|
    Value     |   *5   |    3   |    4   |   *2    |
    
    From here, we move to the next index, I.
    II's character, C, has a value of 4.
    I + 4 (1 + 4), V (5).
    We don't have an index of V. But we can loop around 
    by dividing the answer by the size of the code and taking the remainder.
    Therefore, 5 % 4 (5 mod 4, 5 divided by 4), 1 (4 goes into 5 once, with 1 remaining.)
    We do have an index of I (1). We'd swap now, but we'd swap with the same index (II with II.)
    
    Index     |    0   |    I   |   II   |   III   |
    ----------|--------|--------|--------|---------|
    Character |    D   |   *B   |    C   |    A    |
    ----------|--------|--------|--------|---------|
    Value     |    5   |   *3   |    4   |    2    |
    
    (no change)
    
    Onto II. Value of the next index, III, is 2. 
    II + 2 (2 + 2), 4.
    4 % 4 (5 divided by 4), 0 remaining.
    Swap II and 0.
    
    Index     |    0   |    I   |   II   |   III   |
    ----------|--------|--------|--------|---------|
    Character |   *C   |    B   |   *D   |    A    |
    ----------|--------|--------|--------|---------|
    Value     |   *4   |    3   |   *5   |    2    |
    
    Finally, III. To check the next index, we wrap back to the start. So, index 0.
    III + 4 (3 + 4), 7.
    7 % 4 (8 divided by 4), III (3). 
    Another self-swap, so we finish off.
    
    Final chart:
    
    Index     |    0   |    I   |   II   |   III   |
    ----------|--------|--------|--------|---------|
    Character |   *C   |    B   |   *D   |    A    |
    ----------|--------|--------|--------|---------|
    Value     |   *4   |    3   |   *5   |    2    |
    
    Dog code of CBDA.
    
    Unwinding is just this process but backwards. Starting from III, peeking 0,
    
    
    Values are only useful for calculating swaps, they don't do anything else.