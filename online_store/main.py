from classes.main_all_classes import Diamond, FreeUser, Gold, PaidUser, Plan, Product, Review, Silver

silver_plan = Silver()
gold_plan = Gold()
diamond_plan = Diamond()


free_user = FreeUser("Mahmoud", "Badawy", "a@example.com", "password123")
silver_user = PaidUser("Ahmed", "Saber", "b@example.com", "password456", silver_plan)
gold_user = PaidUser("Alaa", "Hatem", "c@example.com", "password789", gold_plan)
diamond_user = PaidUser("Nada", "khaled", "N@example.com", "password000", diamond_plan)
diamond_user_2 = PaidUser("manar", "fathy", "m@example.com", "password256", diamond_plan)


p1 = Product("Laptop", 1000)
p2 = Product("Phone", 500)
p3 = Product("Tablet", 300)


silver_user.buy_item(p1)
gold_user.buy_item(p2)
diamond_user.buy_item(p3)
diamond_user.buy_item(p2)


p1.add_review("Great laptop", "Fast and reliable", 5)
p2.add_review("Good phone", "Value for money", 4)
p3.add_review("Nice tablet", "Compact and efficient", 4)


print(silver_user.say_name())
print(f"Total Amount Spent: ${silver_user.total_spent}")


print(f"Product: {p1.title} Reviews:")
for review in p1.reviews:
    print(f"Title: {review.title}, Stars: {review.star_count}, Description: {review.description}")