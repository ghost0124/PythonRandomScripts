# take any 2 vectors and output graph of their function 
# adding etc.
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    origin_X = np.array((0))
    origin_Y = np.array((0))
    X = 0
    Y = 0
    
    print('First vector')
    print('X value: ')
    X = np.array(((int(input()))))
    
    print('Y value: ')
    Y = np.array(((int(input()))))

    print('Second vector')
    print('X value: ')
    X2 = np.array(((int(input()))))
    
    print('Y value: ')
    Y2 = np.array(((int(input()))))

    fig,ax = plt.subplots()
    
    v_sum = np.array([(X+X2), (Y+Y2)])
    
    print(v_sum)
    
    origin_vector1 = ax.quiver(origin_X, origin_Y, X, Y, units='xy', scale=1, color='g')
    origin_vector2 = ax.quiver(origin_X, origin_Y, X2, Y2, units='xy', scale=1, color='g')
    origin_vector1_reversed = ax.quiver(origin_X, origin_Y, v_sum[0], v_sum[1], units='xy', scale=1, color='r')
    origin_vector2_reversed = ax.quiver(X,Y, (v_sum[0] - X), (v_sum[1] - Y), units='xy', scale=1, color='b')
    
    sum_vector = ax.quiver(X2,Y2, (v_sum[0] - X2), (v_sum[1] - Y2), units='xy', scale=1, color='b')
    plt.grid(visible=True, which='major')
    
    ax.set_aspect('equal')
    
    plt.ylim(-20, 20)
    plt.xlim(-20, 20)
    
    plt.quiverkey(origin_vector1, 5, 5, .2, 'vector1', color='g')
    plt.quiverkey(origin_vector2, 5, 5, .2, 'vector2', color='b')
    plt.quiverkey(sum_vector, 10, .83, .2, 'sum vector', color='r')
    
    plt.show()