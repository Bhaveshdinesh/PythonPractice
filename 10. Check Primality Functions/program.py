user_num = int(input("Enter upper limit of prime number range: "))
list_range = list(range(2, user_num))

prime_list = []
for current_num in range(2,user_num):
    prime = True
    for reccuring_num in range(2,current_num):
        if current_num%reccuring_num==0:
            prime = False
            break
    if prime:
        prime_list.append(current_num)

print(prime_list)
