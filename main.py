# 2D Collections:


groceries = ({"apple", "orange", "banana", "coconut"},
             {"celery", "carrots", "potatoes"}, 
             {"chicken", "fish", "turkey"})

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()