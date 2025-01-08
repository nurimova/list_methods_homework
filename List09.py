def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    index=0
    apple_indx=[]
    while index<len(fruits):
        if fruits[index]=='apple':
            apple_indx.append(index)
        index+=1
    s=len(apple_indx)
    return s and apple_indx
fruits=["apple", "banana", "apple", "pear", "apple"]
print(main(fruits))
