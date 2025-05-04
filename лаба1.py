def expected_dominant_offspring(pairs):
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = pairs
    expectation = (AA_AA * 2) + (AA_Aa * 2) + (AA_aa * 2) + (Aa_Aa * 1.5) + (Aa_aa * 1) + (aa_aa * 0)
    return expectation

input_data = input("Введите шесть целых неотрицательных чисел через пробел: ")
pairs = list(map(int, input_data.split()))

if len(pairs) != 6 or any(n < 0 or n > 20000 for n in pairs):
    print("Введите ровно шесть неотрицательных чисел, каждое из которых не превышает 20000.")
else:
    result = expected_dominant_offspring(pairs)
    print(f"{result:.1f}")