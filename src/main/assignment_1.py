import math


#1 APPROXIMATION ALGORITHM
def ApproximationAlgorithm():
    x0 = 1.5;
    tol = .00001;

    iter = 0;
    diff = x0;
    x = x0;
    print( iter, " :" , x);

    while (diff >= tol):
        iter += 1
        y = x;
        x = (x / 2) + (1 / x)
        print( iter, " :" , x);
        diff = math.fabs(x - y)
        
    print(f"\nConvergence after", iter, "iterations")
    

#2 BISECTION METHOD
def BisectionMethod():
    x0 = 1.5;
    tol = .00001;

    iter = 0;
    diff = x0;
    x = x0;
    print(iter, ": ", x);

    while (diff >= tol):
        iter += 1
        y = x;
        x = (x/2) + (1/x)
        print(iter, " :" , x)
        diff = math.fabs( x - y)

    print(f"\nConvergence after" , iter, "iterations")


#3 FIXED POINT ITERATION
def FixedPointIteration():
   
    tol = .00001;
    N0 = 50;
    result = "Failure"

    i = 1;
    p = 0;
    p0 = 1.5;
    
    while (i <= N0):
  
        p = p0 - p0*p0*p0 - 4*p0*p0 + 10
        #p = math.sqrt(10 - p0*p0*p0) / 2
        
        if (p != p): 
            print("Diverges")
            break

        print(i, ": " ,p)

        if math.fabs(p - p0) < tol:
            result = "Success"
            break
        i += 1
        p0 = p
    print(result, " after " , i, "iterations\n")

#4 NEWTON RAPHSON METHOD
def NewtonRaphsonMethod():
 
    f = lambda x: math.sqrt(10 - x*x*x) / 2-x
    df = lambda x: -(3 * x*x) / (4 * math.sqrt(10-x*x*x)) -1
    found = False

    p_prev = 3.14/4;
    p_next = p_prev - f(p_prev) / df(p_prev)
    tol = .00001;
    N0 = 1000;

    i = 1
    while (i <= N0):
        if (df(p_prev) != 0):
           
            print(i, ": " ,p_next)

            if math.fabs(p_next-p_prev) < tol:
                print("Success after " ,i, " iterations")
                found = True
                break
            i += 1
            p_prev = p_next
            
        else:
            print("Failure")
            found = True
            break

    if not found:
        print("Failure")

if __name__=='__main__':
    print(" #1 Approximation Algorithm")
    ApproximationAlgorithm()

    print("#1 Bisection Algorithm")
    BisectionMethod()

    print("#3 Fixed Point Algorithm")
    FixedPointIteration()
    
    print("#4 Newton Raphson Method")
    NewtonRaphsonMethod()
