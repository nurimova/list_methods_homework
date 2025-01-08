def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    list2=[]
    count_one=list1.count(1)
    count_zero=list1.count(0)
    list2=[count_zero, count_one]
    return list2
list1=[1,0,0,0,1,0]
print(main(list1))