score = int(input("what did you get in mathematics test? "))
is_A = score >= 9
is_B = score >= 8 and score < 9 
is_C = score >=7 and score < 8 
is_D = score >=6 and score < 7 
is_F = score < 6

print(is_A, is_B, is_C, is_D, is_F )