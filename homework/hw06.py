def cross(u, v):
    '''
    Purpose:
        Returns the cross prod
    '''
    ru = u[1] * v[2] - u[2] * v[1]
    rx = u[2] * v[0] - u[0] * v[2]
    rv = u[0] * v[1] - u[1] * v[0]
    return [ru, rx, rv]
