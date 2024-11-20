airline_name = input()  
adult_tickets = int(input())  
child_tickets = int(input())  
adult_ticket_price = float(input())  
service_fee = float(input())  

child_ticket_price = adult_ticket_price * 0.30  
total_adult_price = (adult_ticket_price + service_fee) * adult_tickets  
total_child_price = (child_ticket_price + service_fee) * child_tickets  
total_revenue = total_adult_price + total_child_price  
profit = total_revenue * 0.20  

print(f"The profit of your agency from {airline_name} tickets is {profit:.2f} lv.")
