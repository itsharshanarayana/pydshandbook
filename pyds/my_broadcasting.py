import numpy as np

def display():
    print("Hello World!")
    
def array_center():
    X = np.random.random((10, 3))
    X_mean = X.mean(0)
    print(X_mean)
    X_centered = X - X_mean
#     print(X_centered)
    print(X_centered.mean(0))
    
def binary_operation():
    # Binary operations are element-wise.
    a = np.arange(3)
    b = np.full(3, 5, dtype=int)
    
    # Binary addition - Element-wise addition.
    result = a + b
    print('Result: {}'.format(result))
    
    ''' 
        Above operation can be performed using NumPy broadcasting as below.
        Dimension of a = 1, 3
        Dimension of b = 1,
        Dimension of b is stretched as 1,1 and then 1, 3 to match that of a. 
        After b is stretched to match the shape of a, addition is performed
    '''
    broad_result = a + 5
    print('Broadcast result: {}'.format(broad_result))
    
def numpy_broadcasting():
    '''
    
    '''
    
    
