from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.488
B_val = 0.1171

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s7=0.2300 - 0.7436j  
s8= 0.3142 + 0.2722j 
s9= 0.3142 - 0.2722j 
s10=0.2300 - 0.7436j 
s11= 0.0842 - 1.0157j 
s12= -0.0842 - 1.0157j 
# Define the given polynomial expression
polynomial_expr = 0.4166/((s_L - s7) * (s_L - s8) * (s_L - s9) * (s_L - s10)*(s_L - s11)*(s_L - s12))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
