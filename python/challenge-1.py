armStrongInput = input("Enter a Number: ")

sum = 0 

for i in armStrongInput:
    sum += int(i)**len(armStrongInput)

armStrong = f"{armStrongInput} is an Armstrong Number" if sum == int(armStrongInput) else f"{armStrongInput} is not an Armstrong Number"
print(armStrong)

# if sum == int(armStrongInput):
#     print(f"{armStrongInput} is an Armstrong Number")

# else:
#     print(f"{armStrongInput} is not an Armstrong Number")