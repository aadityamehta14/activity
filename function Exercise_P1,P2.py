problem 1
def calculate_final_price():
    initial_price = float(input("Enter the initial price: "))
    is_prime_member = input("Are you a Prime member? (y/n)").lower() == 'y'
    is_black_friday_sale = input("Is the item on Black Friday sale? (y/n)").lower() == 'y'
    discount = 0
    if is_prime_member:
        discount += 0.15
    if is_black_friday_sale:
        discount += 0.08
    final_price = initial_price * (1 - discount)
    return final_price
    
final_price = calculate_final_price()
print(final_price)


problem -2
Chit Chat Application - Function:

def mess(m):
  m=message.split()
  print(len(m))
  if len(m)<30:
    print(message)
  else:
    print('length exceeds')

message=(input(("Enter the message: ")))
m=mess(message)