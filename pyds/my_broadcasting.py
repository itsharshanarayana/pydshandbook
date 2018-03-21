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