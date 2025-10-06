

product_price = 10

print(type(product_price))

print(f'the price of this product {product_price}')

#arithmatic operator: +,-,*/,%,**


product_1 = 100
product_2 = 200
product_3 = 300

discount = 17

total = product_1 + product_2 + product_3

discount_price = total - (total * discount)/100

print(total, discount_price)



#each string has a index number
#index_number always starts from zero
#last_index = size - 1
#size = len()

product_name = "burger"
# print((product_name[6]))

time = int(input("Enter your time: "))

print(type(time))
if(time>=5 and time<=7):
    print("50% Discount")

#and = all needs to be true
#or = any condition is true
elif(time>=8 and time<=10):
    print("20% Discount")

else:
    print("No Discount")