import numpy as np

def comparison_ufuncs():
    x = np.array([1, 2, 3, 4, 5])
    
    print('\nComparison Ufuncs')
    print('x: {}'.format(x))
    
    # Using < operator and np.less ufunc 
    print('x < 3: {}'.format(x < 3)) # Using operator.
    print('np.less(x, 3): {}'.format(np.less(x, 3)))
    
    print()
    # Using == operator and np.eqlal ufunc
    print('x != 3: {}'.format(x != 3))
    print('np.not_equal(x, 3): {}'.format(np.not_equal(x, 3)))
    
    print()
    # Using == operator and np.eqlal ufunc
    print('x == 3: {}'.format(x == 3))
    print('np.equal(x, 3): {}'.format(np.equal(x, 3)))
    
    print()
    # Using == operator and np.eqlal ufunc
    print('x <= 3: {}'.format(x <= 3))
    print('np.less_equal(x, 3): {}'.format(np.less_equal(x, 3)))
    
    print()
    # Using == operator and np.eqlal ufunc
    print('x > 3: {}'.format(x > 3))
    print('np.greater(x, 3): {}'.format(np.greater(x, 3)))
    
    print()
    # Using == operator and np.eqlal ufunc
    print('x >= 3: {}'.format(x >= 3))
    print('np.greater_equal(x, 3): {}'.format(np.greater_equal(x, 3)))
    
    '''
        Comparison operators work with arrays of any size and shape.
    '''
    print()
    rnd = np.random.RandomState(0)
    two_d = rnd.randint(10, size=(3, 4))
    print('two_d: {}'.format(two_d))
    print('np.less(two_d, 6): {}'.format(np.less(two_d, 6)))
    

def bool_arrays():
    print()
    rnd = np.random.RandomState(0)
    two_d = rnd.randint(10, size=(3,4))
    print('two_d: {}'.format(two_d))
    
    print()
    print('np.less(two_d, 6): {}'.format(np.less(two_d, 6)))
    print('Number of elements < 6: {}'.format(np.count_nonzero(np.less(two_d, 6))))
    print('# of elements < 6 using np.sum(): {}'.format(np.sum(np.less(two_d, 6))))
    print('row-wise # of elements < 6 using np.sum(): {}'.format(np.sum(np.less(two_d, 6), axis=1)))
    print('column-wise # of elements < 6 using np.sum(): {}'.format(np.sum(np.less(two_d, 6), axis=0)))
    
    
    