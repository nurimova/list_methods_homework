def main(list01):
    """
    A list of zeros and ones is given. Find how many zeros are involved and return.
    Args:
        list01(list): parameter
    Returns:
        int: return answer
    """
    return list01.count(0)
list01=[0,1,0,1,0,1]
print(main(list01))