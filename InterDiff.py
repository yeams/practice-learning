import doctest
import pdb 

# pdb.set_trace()

#  交集
def set_intersection(a, b): 
    '''
    >>> set_intersection(set([1, 2, 3]), set([3, 4, 5]))
    {3}
    '''

    return a&b

# 差集 求差集并定要先求出两集合的交集和并集
def set_difference(a, b):
    '''
    >>> set_difference(set([1, 2, 3]), set([3, 4, 5]))
    {1, 2}
    >>> set_difference(set([3, 4, 5]), set([1, 2, 3]))
    {4, 5}
    '''
    return a-b

if __name__ == '__main__':
    # print(set_difference(set([1, 2, 3]), set([3, 4, 5])))
    # print(set_difference(set([3, 4, 5]), set([1, 2, 3])))
    doctest.testmod()