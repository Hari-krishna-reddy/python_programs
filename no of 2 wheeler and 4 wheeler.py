import numpy as np
#input :
#200  -> Value of V
#540   -> Value of W

#Output :
#TW =130 FW=70
def vehicles(x,y):
    no_2=y//2
    no_4=0
    while no_2+no_4!=x:
        no_4+=1
        no_2-=2
        if no_2<0:
            return 0,0
    return no_2,no_4
a,b=vehicles(201,404)
print(a,b)


#--------------OR--------------------------------
def calculate_production(v, w):
    # Equation 1: TW + FW = v
    # Equation 2: 2 * TW + 4 * FW = w

    # Coefficients matrix
    coefficients = [[1, 1], [2, 4]]
    
    # Constants matrix
    constants = [v, w]

    try:
        # Solve the system of equations
        solution = np.linalg.solve(coefficients, constants)

        # Extract TW and FW from the solution
        TW = solution[0]
        FW = solution[1]
        if int(TW)+int(FW)!=v:
            return "No valid solution"

        return int(TW), int(FW)
    except np.linalg.LinAlgError:
        return "No valid solution"

# Example usage:
v_invalid = 200  # Total number of vehicles
w_invalid = 539  # Total number of wheels (not divisible by 2)

result = calculate_production(v_invalid, w_invalid)
print(result)


        