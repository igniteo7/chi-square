def chi_square(observed):
    row_totals = [sum(row) for row in observed]
    col_totals = [sum(col) for col in list(zip(*observed))]  
    grand_total = sum(row_totals)
    
    chi_square_stat = 0
    for i in range(len(observed)):
        for j in range(len(observed[0])):
            expected = (row_totals[i] * col_totals[j]) / grand_total
            chi_square_stat += (observed[i][j] - expected) ** 2 / expected
    dof = (len(observed) - 1) * (len(observed[0]) - 1)
    return chi_square_stat, dof

observed_values = [
    [300, 350, 425],
    [700, 650, 575]
]
crit_value = input("Enter Critical Value")
chi_square_stat, dof = chi_square(observed_values)
rounded_chi_sq_stat = round(chi_square_stat, 4)
if float(chi_square_stat) > float(crit_value):
    print(rounded_chi_sq_stat)
    print("Hence Ho is accepted")
else:
    print("Hence Ho is not accepted")
