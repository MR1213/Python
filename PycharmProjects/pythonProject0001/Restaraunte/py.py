(item1, price1) = "Meatballs", 7
(item2, price2) = "Mashed Potatoes", 5
(item3, price3) = "Milkshake", 4
(item4, price4) = "Vegetables", 5
(item5, price5) = "Chocolate Cake", 5
(item6, price6) = "Yummy Soup", 7
(item7, price7) = "Mac & Cheese", 8
(item8, price8) = "Queen Size Bed ", 378


print("Hello, welcome to Aeki (if you dont get it yet it is Ikea but backwards)")
menu = f"""
******Menu******
{item1} {price1}
{item2} {price2}
{item3} {price3}
{item4} {price4}
{item5} {price5}
{item6} {price6}
{item7} {price7}
{item8} {price8}
****************
"""
print("This is our menu here at Aeki: \n")
print(menu)

amount1 = float(input("How many Meatballs would you like? ")) // 1
amount2 = float(input("How much Mashed Potatoes would you like? ")) // 1
amount3 = float(input("How many Milkshake would you like? ")) // 1
amount4 = float(input("How much Vegetables would you like? ")) // 1
amount5 = float(input("How much Chocolate Cake would you like? ")) // 1
amount6 = float(input("How much Yummy Soup would you like? ")) // 1
amount7 = float(input("How much Mac & Cheese would you like? ")) // 1
amount8 = float(input("How many Queen Size Bed would you like? ")) // 1

total1 = (
    amount1 * price1
    + amount2 * price2
    + amount3 * price3
    + amount4 * price4
    + amount5 * price5
    + amount6 * price6
    + amount7 * price7
    + amount8 * price8
)
receipt1 = f"""
****Receipt*****************************
{amount1} {item1} ${price1 * amount1} 
{amount2} {item2} ${price2 * amount2}
{amount3} {item3} ${price3 * amount3}
{amount4} {item4} ${price4 * amount4}
{amount5} {item5} ${price5 * amount5}
{amount6} {item6} ${price6 * amount6}
{amount7} {item7} ${price7 * amount7}
{amount8} {item8} ${price8 * amount8}
****************************************
"""

print(receipt1)
include_tax = total1 * 0.1
tip_cost = float(input("How big of a tip would you like to leave? (0%, 10%, 15%, etc.)"))
print("The cost with your desired tip is: ")
print("$", total1*(1+(tip_cost/100)))
print("Just the tip is: ")
print("$", total1*(tip_cost/100))

final_total = include_tax + total1*(1+(tip_cost/100))
print("The total Bill is:", final_total, "$")



