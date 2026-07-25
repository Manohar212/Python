# Step 1: Create a list of 5 favourite fruits
fruits = ["Mango", "Banana", "Apple", "Orange", "Grapes"]

# Step 2: Print the full list and its length
print("Full list of fruits:", fruits)
print("Number of fruits:", len(fruits))

# Step 3: Access and print the first, last, and middle item
if fruits:  # Ensure list is not empty
    first_item = fruits[0]
    last_item = fruits[-1]
    middle_item = fruits[len(fruits) // 2]  # Middle index
    print("First fruit:", first_item)
    print("Last fruit:", last_item)
    print("Middle fruit:", middle_item)

# Step 4: Add a new fruit to the end
fruits.append("Pineapple")
print("\nAfter appending Pineapple:", fruits)

# Step 5: Insert a fruit at position 2 (index 1-based in description, 0-based in Python)
fruits.insert(2, "Strawberry")
print("After inserting Strawberry at position 2:", fruits)

# Step 6: Remove a fruit by name
if "Banana" in fruits:
    fruits.remove("Banana")
    print("After removing Banana:", fruits)
else:
    print("Banana not found in the list.")

# Step 7: Sort the list alphabetically
fruits.sort()
print("Sorted fruits:", fruits)

# Step 8: Slice the list to print only the first 3 fruits
print("First 3 fruits:", fruits[:3])

# Step 9: Loop through the list and print each fruit with its index
print("\nFruits with index numbers:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
