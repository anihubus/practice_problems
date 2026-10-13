def hasPairWithDifference(A: list[int], N: int, B: int) -> int:
    # write your code here 
    for i in A:
        if (i+B) in A:
            return 1
    return 0