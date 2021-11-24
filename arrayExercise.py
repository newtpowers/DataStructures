# Each of the elements in the array has the index value of the month number - 1 as the array starts at an index of 0
expenses = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
difference = expenses[1] - expenses[0]
print(difference)
# 2. Find out your total expense in first quarter (first three months) of the year.
for i in expenses:
    sum += expenses[i]
print(sum)
# 3. Find out if you spent exactly 2000 dollars in any month
for i in expenses:
    if expenses[i] == 2000:
        print("You spent exactly 2000 dollars!")
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses[len(expenses) + 1] = 1980
# OR BETTER
expenses.append(1980)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200