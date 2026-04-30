weather =input("enter type of weather (sunny/rainy/snowy):")
time_of_the_day = "night"

if weather =="sunny":
    if time_of_the_day =="day":
        print("You play with your car toy.")
    else:
        print("Its night,Time to sleep.")
elif weather=="rainy":
    print("You plaay with your boat toy.")
elif weather=="snowy":
    if time_of_the_day =="night":
        print("You play with your Teddy bear toy.")
    else:
        print("You play with your snowman toy.")
else:
    print("You stay inside and read a storybook.")