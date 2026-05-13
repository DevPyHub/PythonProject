import math
import datetime as dt
import difflib
import json
import os
import string
import random as r
print("WELCOME TO MEGA PROJECT HUB")
while True:
    try:
        u=int(input("CHOOSE YOUR PROJECT\n1.MATH CALCULATOR\n2.TIME\n3.RANDOM GAME\n4.QUIZ GAME\n5.TO DO LIST\n6.UNIT CONVERTER\n7.FAKE ACCOUNT\n8.LINK SEARCHER\n9.BOOK LIBRARY\n10.AI CHATBOT\n11.ACCOUNT WITH CASH\n12.EXIT\nYOUR CHOICE\n"))
        if u==1:
            print(' Math Calculator Pro')
            print('---------------------')
            while True:
                try:
                    print('All Sections:\n1.Normal Math.\n2.Scientific Math.\n3.Interest Math.\n4.Arial Math\n5.Exit')
                    choice = int(input('Enter any section (only numbers are allowed)\n'))
                    if choice == 1:
                        print('\nWelcome to Normal Math Calculator')
                        while True:
                            try:
                                print("Calculator")
                                print("1.Addition")
                                print("2.Subtraction")
                                print("3.Multiplication")
                                print("4.Division")
                                print("5.Power")
                                print("6.Square root")
                                print("7.Modulus")
                                print("8.Exit")
                                u = (input("Enter your choice\n")).strip().lower()
                                if u.lower() in ["1", "addition"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    print("Result: ", u1 + u2, "\n")
                                elif u.lower() in ["2", "subtraction"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    print("Result: ", u1 - u2, "\n")
                                elif u.lower() in ["3", "multiplication"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    print("Result: ", u1 * u2, "\n")
                                elif u.lower() in ["4", "division"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    try:
                                        print("Result: ", u1 / u2, "\n")
                                    except ZeroDivisionError:
                                        print("Cannot divide by zero\n")
                                elif u.lower() in ["5", "power"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    print("Result: ", u1 ** u2, "\n")
                                elif u.lower() in ["6", "square root"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    try:
                                        print("The first number root:", math.sqrt(u1), "\n")
                                        print("The second number root:", math.sqrt(u2), "\n")
                                    except ValueError and OverflowError:
                                        print(
                                            "This is not a positive number or the number is too large to show please try again\n")
                                elif u.lower() in ["7", "modulus"]:
                                    u1 = float(input("Enter the first number\n"))
                                    u2 = float(input("Enter the second number\n"))
                                    print("Result: ", u1 % u2, "\n")
                                elif u.lower() in ["8", "exit"]:
                                    print("Ok, Section ends here\n")
                                    break
                                else:
                                    print("Invalid Input\n")
                                    continue
                            except ValueError:
                                print("Invalid Input\n")
                    elif choice == 2:
                        print('\nWelcome to Scientific Math Calculator')
                        while True:
                            try:
                                print("Calculator")
                                print('1.Sin')
                                print('2.Cos')
                                print('3.Tan')
                                print('4.Log')
                                print('5.Log10')
                                print('6.Factorial')
                                print('7.Exponent')
                                print('8.Exit')
                                U = (input("Enter your choice\n")).strip().lower()
                                if U.lower() in ["1", "sin"]:
                                    x = float(input("Enter the number\n"))
                                    print("Result: ", math.sin(x), "\n")
                                elif U.lower() in ["2", "cos"]:
                                    x = float(input("Enter the number\n"))
                                    print("Result: ", math.cos(x), "\n")
                                elif U.lower() in ["3", "tan"]:
                                    x = float(input("Enter the number\n"))
                                    print("Result: ", math.tan(x), "\n")
                                elif U.lower() in ["4", "log"]:
                                    x = float(input("Enter the number\n"))
                                    try:
                                        print("Result: ", math.log(x), "\n")
                                    except ValueError:
                                        print("This is not a positive number please try again\n")
                                elif U.lower() in ["5", "log10"]:
                                    x = float(input("Enter the number\n"))
                                    try:
                                        print("Result: ", math.log10(x), "\n")
                                    except ValueError:
                                        print("This is not a positive number please try again\n")
                                elif U.lower() in ["6", "factorial"]:
                                    x = float(input("Enter the number\n"))
                                    try:
                                        if x < 0 or not x.is_integer():
                                            print("Factorial only allows non-negative integers\n")
                                        else:
                                            print("Result:", math.factorial(int(x)), "\n")
                                    except ValueError:
                                        print("This is not a positive number please try again\n")
                                elif U.lower() in ["7", "exponent", "exp"]:
                                    try:
                                        x = float(input("Enter the number\n"))
                                        print("Result: ", math.exp(x), "\n")
                                    except ValueError and OverflowError:
                                        print(
                                            "This is not a positive number or the number is too large to show please try again\n")
                                elif U.lower() in ["8", "exit"]:
                                    print("Ok, Section ends here\n")
                                    break
                                else:
                                    print("Invalid Input\n")
                                    continue
                            except ValueError:
                                print("Invalid Input\n")
                    elif choice == 3:
                        print("\nWelcome to Interest Calculator")
                        while True:
                            try:
                                print("Calculator")
                                print("1.Interest Calculator\n2.Exit")
                                choice = int(input("Enter your choice\n"))
                                if choice == 1:
                                    try:
                                        principle = 0
                                        time = 0
                                        rate = 0
                                        while principle <= 0:
                                            principle = float(input("Enter the principal amount\n"))
                                            if principle <= 0:
                                                print("Principle amount cannot be negative or equal to zero.")
                                        while rate <= 0:
                                            rate = float(input("Enter the interest rate\n"))
                                            if rate <= 0:
                                                print("Interest rate cannot be negative or equal to zero.")
                                        while time <= 0:
                                            time = int(input("Enter the time in years\n"))
                                            if time <= 0:
                                                print("Time cannot be negative or equal to zero.")
                                        total = principle * pow((1 + rate / 100), time)
                                        print(f"Balance after {time:,} year/s is ${total:,.3f}\n")
                                    except ValueError or OverflowError:
                                        print("Invalid Input or too large number to show\n")
                                        break
                                elif choice == 2:
                                    print("Ok, Section ends here\n")
                                    break
                                else:
                                    print("Invalid Choice\n")
                            except ValueError:
                                print("Invalid Input\n")
                    elif choice == 4:
                        pi = math.pi
                        print("\nWelcome to Arial Math Calculator")
                        while True:
                            try:
                                print("Calculator")
                                print("1.Rectangle")
                                print("2.Square")
                                print("3.Circle")
                                print("4.Triangle")
                                print("5.Trapezium")
                                print("6.Rhombus")
                                print("7.Parallelogram")
                                print("8.Ellipse")
                                print("9.Sphere Surface")
                                print("10.Exit")
                                u = (input("Enter your choice\n")).strip().lower()
                                if u.lower() in ["1", "rectangle"]:
                                    u1 = float(input("Enter the Length\n"))
                                    u2 = float(input("Enter the Width\n"))
                                    try:
                                        result = u1 * u2
                                        print(f"Result: {result:,.3f}\n")
                                    except ValueError:
                                        print("This is not a positive number please try again")
                                elif u.lower() in ["2", "square"]:
                                    u1 = float(input("Enter a Side\n"))
                                    try:
                                        result = pow(u1, 2)
                                        print(f"Result: {result:,.3f}\n")
                                    except (ValueError, OverflowError):
                                        print(
                                            "This is not a positive number or the number is too large to show please try again\n")
                                elif u.lower() in ["3", "circle"]:
                                    u1 = float(input("Enter the Radius\n"))
                                    try:
                                        result = pi * pow(u1, 2)
                                        print(f"Result: {result:,.3f}\n")
                                    except (ValueError, OverflowError):
                                        print(
                                            "This is not a positive number or the number is too large to show please try again\n")
                                elif u.lower() in ["4", "triangle"]:
                                    u1 = float(input("Enter the Base\n"))
                                    u2 = float(input("Enter the Height\n"))
                                    try:
                                        result = 0.5 * u1 * u2
                                        print(f"Result: {result:,.3f}\n")
                                    except ValueError:
                                        print("This is not a positive number please try again")
                                elif u.lower() in ["5", "trapezium"]:
                                    u1 = float(input("Enter the A parallel side\n"))
                                    u2 = float(input("Enter the B parallel side\n"))
                                    u3 = float(input("Enter the Vertical height\n"))
                                    try:
                                        result = 0.5 * (u1 + u2) * u3
                                        print(f"Result: {result:,.3f}\n")
                                    except ValueError:
                                        print("This is not a positive number please try again")
                                elif u.lower() in ["6", "rhombus"]:
                                    u1 = float(input("Enter the first Diagonal\n"))
                                    u2 = float(input("Enter the second Diagonal\n"))
                                    try:
                                        result = u1 * u2 / 2
                                        print(f"Result: {result:,.3f}\n")
                                    except (ValueError, OverflowError):
                                        print(
                                            "This is not a positive number or the number is too large to show please try again\n")
                                elif u.lower() in ["7", "parallelogram"]:
                                    u1 = float(input("Enter the Base\n"))
                                    u2 = float(input("Enter the Height\n"))
                                    try:
                                        result = u1 * u2
                                        print(f"Result: {result:,.3f}\n")
                                    except ValueError:
                                        print("This is not a positive number please try again")
                                elif u.lower() in ["8", "ellipse"]:
                                    u1 = float(input("Enter the Semi-Major-Axis\n"))
                                    u2 = float(input("Enter the Semi-Minor-Axis\n"))
                                    try:
                                        result = pi * u1 * u2
                                        print(f"Result: {result:,.3f}\n")
                                    except ValueError:
                                        print("This is not a positive number please try again")
                                elif u.lower() in ["9", "sphere surface"]:
                                    u1 = float(input("Enter the Radius\n"))
                                    try:
                                        result = 4 * pi * pow(u1, 2)
                                        print(f"Result: {result:,.3f}\n")
                                    except (ValueError, OverflowError):
                                        print(
                                            "This is not a positive number or the number is too large to show please try again\n")
                                elif u.lower() in ["10", "exit"]:
                                    print("Ok, Section ends here\n")
                                    break
                                else:
                                    print("Invalid Input\n")
                                    continue
                            except ValueError:
                                print("Invalid Input\n")
                    elif choice == 5:
                        print("Ok, Exiting the Program...\n")
                        break
                    else:
                        print("Invalid Choice\n")
                except ValueError:
                    print("Invalid Input\n")
        elif u==2:
            print("WELCOME TO DATE PROJECT")
            while True:
                try:
                    now = dt.datetime.now()
                    print("1.CURRENT MONTH, DATE, YEAR BY NUMBER")
                    print("2.CURRENT YEAR BY NUMBER")
                    print("3.CURRENT MONTH BY NUMBER")
                    print("4.CURRENT DATE BY NUMBER")
                    print("5.CURRENT MONTH BY WRITTEN")
                    print("6.CURRENT HOUR (24) AND HOUR (12)")
                    print("7.CURRENT MINUTE")
                    print("8.CURRENT SECOND")
                    print("9.CURRENT DAY BY WRITTEN")
                    print("10.CURRENT A.M AND P.M")
                    print("11.BACKING")
                    u = int(input("ENTER YOUR CHOICE\n"))
                    if u == 1:
                        print("CURRENT ALL TIME\n", now.strftime("%m/%d/%Y\n"))
                    elif u == 2:
                        print("CURRENT YEAR BY NUMBER\n", now.strftime("%Y\n"))
                    elif u == 3:
                        print("CURRENT MONTH BY NUMBER\n", now.strftime("%m\n"))
                    elif u == 4:
                        print("CURRENT DATE BY NUMBER\n", now.strftime("%d\n"))
                    elif u == 5:
                        print("CURRENT MONTH BY WRITTEN\n", now.strftime("%B\n"))
                    elif u == 6:
                        print("CURRENT HOUR (24) HOUR (12)\n", now.strftime("%H\n%I"))
                    elif u == 7:
                        print("CURRENT MINUTE\n", now.strftime("%M\n"))
                    elif u == 8:
                        print("CURRENT SECOND\n", now.strftime("%S\n"))
                    elif u == 9:
                        print("CURRENT DAY BY WRITTEN\n", now.strftime("%A\n"))
                    elif u == 10:
                        print("CURRENT A.M AND P.M\n", now.strftime("%p\n"))
                    elif u == 11:
                        print("BACKING...\n")
                        break
                    else:
                        print("INVALID CHOICE, TRY AGAIN\n")
                        continue
                except ValueError:
                    print("\nINVALID INPUT\n")
                continue
        elif u==3:
            print("WELCOME TO RANDOM")
            score = 0
            total=0
            while True:
                try:
                    print("1.COUNTRY\n2.SPORTS\n3.COLOUR\n4.NUMBER\n5.BACK")
                    u = input("CHOOSE CATEGORY\n").strip().lower()
                    if u.lower() in ["COUNTRY", "1", "1.", "1.country"]:
                        total+=1
                        print("WELCOME TO COUNTRY CATEGORY")
                        c = r.choice(["bangladesh", "nepal", "pakistan", "mongolia", "chile"])
                        print("GUESS THE COUNTRY WHICH I CHOOSE FROM [1.BANGLADESH 2.NEPAL 3.PAKISTAN 4.MONGOLIA 5.CHILE]")
                        u = input("YOUR GUESS(DON'T WRITE NUMBER)\n").strip().lower()
                        if u.lower() == c:
                            print("CONGRATS! YOU GUESS IT!")
                            score = score + 1
                        else:
                            print(f"WRONG, I CHOSE {c}")
                    elif u.lower() in ["sports", "2", "2.", "2.sports"]:
                        total+=1
                        print("WELCOME TO SPORTS CATEGORY")
                        s = r.choice(["football", "cricket", "badminton", "hockey", "volleyball"])
                        print("GUESS THE SPORT WHICH I CHOOSE FROM [1.FOOTBALL 2.CRICKET 3.BADMINTON 4.HOCKEY 5.VOLLEYBALL]")
                        u = input("YOUR GUESS(DON'T WRITE NUMBER)\n").strip().lower()
                        if u.lower() == s:
                            print("CONGRATS! YOU GUESS IT!")
                            score = score + 1
                        else:
                            print(f"WRONG, I CHOSE {s}")
                    elif u.lower() in ["colour", "3", "3.colour"]:
                        total+=1
                        print("WELCOME TO COLOUR CATEGORY")
                        o = r.choice(["green", "yellow", "blue", "red", "orange"])
                        print("GUESS THE COLOUR WHICH I CHOOSE FROM [1.GREEN 2.YELLOW 3.BLUE 4.RED 5.ORANGE]")
                        u = input("YOUR GUESS(DON'T WRITE NUMBER)\n").strip().lower()
                        if u.lower() == o:
                            print("CONGRATS! YOU GUESS IT!")
                            score = score + 1
                        else:
                            print(f"WRONG, I CHOSE {o}")
                    elif u in ["number", "4", "4.number"]:
                        total+=1
                        print("WELCOME TO NUMBER CATEGORY")
                        n = r.randint(1, 5)
                        print("GUESS THE NUMBER WHICH I CHOOSE FROM (1 TO 5)")
                        try:
                            u = int(input("YOUR GUESS\n"))
                            if u == n:
                                print("CONGRATS! YOU GUESS IT!")
                                score = score+1
                            else:
                                print(f"WRONG, I CHOSE {n}")
                        except ValueError:
                            print("INVALID INPUT, TRY AT THE FIRST\n")
                            continue
                    elif u.lower() in ["back", "5", "5.back"]:
                        print("BACKING...")
                        break
                    else:
                        print("WRONG INPUT\n")
                except ValueError:
                    print("INVALID INPUT\n")
                print(f"YOUR SCORE IS {score}/{total}\n")
        elif u==4:
            print("WELCOME TO SHORT MCQ QUIZ\n")
            score = 0
            questions = [
                {
                    "q": "(1) WHO IS THE PRESIDENT OF BANGLADESH IN 2025?",
                    "o": ["1.MUJIBUR RAHMAN", "2.HASINA", "3.EUNUS", "4.NONE OF ABOVE"],
                    "a": "4"
                },
                {
                    "q": "(2) WHAT IS THE CAPITAL OF BANGLADESH?",
                    "o": ["1.RAJSHAHI", "2.DHAKA", "3.CHITTAGONG", "4.KAMILLA"],
                    "a": "2"
                },
                {
                    "q": "(3) HE IS ____ INTELLIGENT, FILL THE BLANK WITH ARTICLE",
                    "o": ["1.THE", "2.AN", "3.A", "4.NONE OF ABOVE"],
                    "a": "4"
                },
                {
                    "q": "(4) 5 + 5 = x, WHAT IS THE VALUE OF X ?",
                    "o": ["1.10", "2.12", "3.20", "4.0"],
                    "a": "1"
                },
                {
                    "q": "(5) WHAT IS THE POWERFUL COUNTRY IN THE WORLD?",
                    "o": ["1.AMERICA", "2.BANGLADESH", "3.UGANDA", "4.INDIA"],
                    "a": "1"
                }
            ]
            for q in questions:
                print(q["q"])
                for option in q["o"]:
                    print(option)
                u = input("YOUR ANSWER\n")
                if u == q["a"]:
                    print("CORRECT")
                    score += 1
                else:
                    print("WRONG ANSWER, THE CORRECT ANSWER IS ", q["a"], "\n")
                print(f"YOUR SCORE {score}/{len(questions)}\n")
        elif u==5:
            print("WELCOME TO 'TO DO LIST'")
            tasks = []
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r") as f:
                    try:
                        tasks = json.load(f)
                    except json.JSONDecodeError:
                        tasks = []
                while True:
                    try:
                        print("1.CREATE NEW TASK")
                        print("2.VIEW YOUR TASKS")
                        print("3.REMOVE YOUR TASKS")
                        print("4.SAVE ALL YOUR TASKS")
                        print("5.BACK")
                        choice = input("YOUR CHOICE\n")
                        if choice == "4":
                            with open("tasks.json", "w") as f:
                                json.dump(tasks, f)
                            print("ALL TASKS SAVED\n")
                        elif choice == "1":
                            task = input("YOUR NEW TASK\n")
                            tasks.append(task)
                            print(f"{task} ADDED\n")
                        elif choice == "2":
                            if not tasks:
                                print("YOUR TASK LIST IS EMPTY\n")
                            else:
                                print("YOUR TASKS")
                                for i, task in enumerate(tasks, start=1):
                                    print(f"{i}. {task}\n")
                        elif choice == "3":
                            if not tasks:
                                print("YOUR TASK LIST IS EMPTY NO TASKS TO BE REMOVED\n")
                            else:
                                print("YOUR TASKS")
                                for i, task in enumerate(tasks, start=1):
                                    print(f"{i}. {task}\n")
                                try:
                                    num = int(input("ENTER YOUR NUMBER TO REMOVE\n"))
                                    r = tasks.pop(num - 1)
                                    print(f"{r} REMOVED\n")
                                except (ValueError, IndexError):
                                    print("INVALID TASK NUMBER")
                        elif choice == "5":
                            print("BACKING...")
                            break
                        else:
                            print("INVALID CHOICE, TRY AGAIN\n")
                            continue
                    except (ValueError, IndexError):
                        print("INVALID CHOICE TRY AGAIN\n")
        elif u==6:
            print("WELCOME TO UNIT CONVERTER")
            while True:
                try:
                    print("CHOOSE CATEGORY\n1.LENGTH\n2.TEMPERATURE\n3.WEIGHT\n4.AREA\n5.VOLUME\n6.EXIT")
                    u = int(input("ENTER YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                    if u == 1:
                        while True:
                            try:
                                print(
                                    "CHOOSE\n1.KM TO MILE\n2.MILE TO KM\n3.METER TO INCH\n4.INCH TO METER\n5.MILLIMETER TO CENTIMETER\n6.CENTIMETER TO MILLIMETER\n7.METR TO KILOMETER\n8.KILOMETER TO METER\n9.FEET TO METER\n10.METER TO FEET\n11.YARD TO METER\n12.METER TO YARD\n13.MILE TO FEET\n14.FEET TO MILE\n15.MILE TO YARD\n16.YARD TO MILE\n17.INCH TO CENTIMETER\n18.CENTIMETER TO INCH\n19.MILLIMETER TO INCH\n20.INCH TO MILLIMETER\n21.BACK")
                                u = int(input("YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                                if u == 1:
                                    try:
                                        k = float(input("ENTER KM\n"))
                                        r = k * 0.621371
                                        print(f"RESULT = {r:,.3f} MILE\n")
                                    except ValueError:
                                        print("INVALID ENTER KM\n")
                                        continue
                                elif u == 2:
                                    try:
                                        m = float(input("ENTER MILE\n"))
                                        re = m / 0.621371
                                        print(f"RESULT = {re:,.3f} KM\n")
                                    except ValueError:
                                        print("INVALID ENTER MILE\n")
                                        continue
                                elif u == 3:
                                    try:
                                        me = float(input("ENTER METER\n"))
                                        res = me * 39.3701
                                        print(f"RESULT = {res:,.3f} INCH\n")
                                    except ValueError:
                                        print("INVALID ENTER METER\n")
                                        continue
                                elif u == 4:
                                    try:
                                        i = float(input("ENTER INCH\n"))
                                        resu = i / 39.3701
                                        print(f"RESULT = {resu:,.3f} METER\n")
                                    except ValueError:
                                        print("INVALID ENTER INCH\n")
                                        continue
                                elif u == 5:
                                    try:
                                        mm = float(input("ENTER MILLIMETER\n"))
                                        cm = mm / 10
                                        print(f"RESULT = {cm:,.3f} CENTIMETER\n")
                                    except ValueError:
                                        print("INVALID ENTER MILLIMETER\n")
                                        continue
                                elif u == 6:
                                    try:
                                        cm = float(input("ENTER CENTIMETER\n"))
                                        mm = cm * 10
                                        print(f"RESULT = {mm:,.3f} MILLIMETER\n")
                                    except ValueError:
                                        print("INVALID ENTER CENTIMETER\n")
                                        continue
                                elif u == 7:
                                    try:
                                        m = float(input("ENTER METER\n"))
                                        km = m / 1000
                                        print(f"RESULT = {km:,.3f} KILOMETER\n")
                                    except ValueError:
                                        print("INVALID ENTER METER\n")
                                        continue
                                elif u == 8:
                                    try:
                                        km = float(input("ENTER KILOMETER\n"))
                                        m = km * 1000
                                        print(f"RESULT = {m:,.3f} METER\n")
                                    except ValueError:
                                        print("INVALID ENTER KILOMETER\n")
                                        continue
                                elif u == 9:
                                    try:
                                        ft = float(input("ENTER FEET\n"))
                                        m = ft * 0.3048
                                        print(f"RESULT = {m:,.3f} METER\n")
                                    except ValueError:
                                        print("INVALID ENTER FEET\n")
                                        continue
                                elif u == 10:
                                    try:
                                        m = float(input("ENTER METER\n"))
                                        ft = m / 0.3048
                                        print(f"RESULT = {ft:,.3f} FEET\n")
                                    except ValueError:
                                        print("INVALID ENTER METER\n")
                                        continue
                                elif u == 11:
                                    try:
                                        yd = float(input("ENTER YARD\n"))
                                        m = yd * 0.9144
                                        print(f"RESULT = {m:,.3f} METER\n")
                                    except ValueError:
                                        print("INVALID ENTER YARD\n")
                                        continue
                                elif u == 12:
                                    try:
                                        m = float(input("ENTER METER\n"))
                                        yd = m / 0.9144
                                        print(f"RESULT = {yd:,.3f} YARD\n")
                                    except ValueError:
                                        print("INVALID ENTER METER\n")
                                        continue
                                elif u == 13:
                                    try:
                                        mile = float(input("ENTER MILE\n"))
                                        ft = mile * 5280
                                        print(f"RESULT = {ft:,.3f} FEET\n")
                                    except ValueError:
                                        print("INVALID ENTER MILE\n")
                                        continue
                                elif u == 14:
                                    try:
                                        ft = float(input("ENTER FEET\n"))
                                        mile = ft / 5280
                                        print(f"RESULT = {mile:,.3f} MILE\n")
                                    except ValueError:
                                        print("INVALID ENTER FEET\n")
                                        continue
                                elif u == 15:
                                    try:
                                        mile = float(input("ENTER MILE\n"))
                                        yd = mile * 1760
                                        print(f"RESULT = {yd:,.3f} YARD\n")
                                    except ValueError:
                                        print("INVALID ENTER MILE\n")
                                        continue
                                elif u == 16:
                                    try:
                                        yd = float(input("ENTER YARD\n"))
                                        mile = yd / 1760
                                        print(f"RESULT = {mile:,.3f} MILE\n")
                                    except ValueError:
                                        print("INVALID ENTER YARD\n")
                                        continue
                                elif u == 17:
                                    try:
                                        inch = float(input("ENTER INCH\n"))
                                        cm = inch * 2.54
                                        print(f"RESULT = {cm:,.3f} CENTIMETER\n")
                                    except ValueError:
                                        print("INVALID ENTER INCH\n")
                                        continue
                                elif u == 18:
                                    try:
                                        cm = float(input("ENTER CENTIMETER\n"))
                                        inch = cm / 2.54
                                        print(f"RESULT = {inch:,.3f} INCH\n")
                                    except ValueError:
                                        print("INVALID ENTER CENTIMETER\n")
                                        continue
                                elif u == 19:
                                    try:
                                        mm = float(input("ENTER MILLIMETER\n"))
                                        inch = mm / 25.4
                                        print(f"RESULT = {inch:,.3f} INCH\n")
                                    except ValueError:
                                        print("INVALID ENTER MILLIMETER\n")
                                        continue
                                elif u == 20:
                                    try:
                                        inch = float(input("ENTER INCH\n"))
                                        mm = inch * 25.4
                                        print(f"RESULT = {mm:,.3f} MILLIMETER\n")
                                    except ValueError:
                                        print("INVALID ENTER INCH\n")
                                        continue
                                elif u == 21:
                                    confirmation = input("ARE YOU SURE YOU WANT TO EXIT?(Y/N)\n")
                                    if confirmation == "Y" or confirmation == "y" or confirmation == "YES" or confirmation == "yes":
                                        print("OK, BACKING...\n")
                                        break
                                    elif confirmation == "N" or confirmation == "n" or confirmation == "NO" or confirmation == "no":
                                        print("THANKS FOR REUSING IT\n")
                                        continue
                                    else:
                                        print("SORRY, CANNOT PROCEED\n")
                                        continue
                                else:
                                    print("INVALID ENTER CHOICE\n")
                                    continue
                            except ValueError:
                                print("INVALID INPUT, TRY AGAIN\n")
                                continue
                    elif u == 3:
                        while True:
                            try:
                                print("CHOICE\n1.KILO TO POUND\n2.POUND TO KILO\n3.GRAM TO OUNCE\n4.OUNCE TO GRAM\n5.BACK")
                                u = int(input("YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                                if u == 1:
                                    try:
                                        K = float(input("ENTER KILO\n"))
                                        if K < 0:
                                            print("KILOGRAM CANNOT BE NEGATIVE\n")
                                        else:
                                            rE = K * 2.20462
                                            print(f"RESULT = {rE:,.3f} POUND\n")
                                    except ValueError:
                                        print("INVALID ENTER KILO\n")
                                        continue
                                elif u == 2:
                                    try:
                                        p = float(input("ENTER POUND\n"))
                                        if p < 0:
                                            print("POUND CANNOT BE NEGATIVE\n")
                                        else:
                                            REs = p / 2.20462
                                            print(f"RESULT = {REs:,.3f} KILO\n")
                                    except ValueError:
                                        print("INVALID ENTER POUND\n")
                                        continue
                                elif u == 3:
                                    try:
                                        g = float(input("ENTER GRAM\n"))
                                        if g < 0:
                                            print("GRAM CANNOT BE NEGATIVE\n")
                                        else:
                                            RES = g / 28.3495
                                            print(f"RESULT = {RES:,.3f} OUNCE\n")
                                    except ValueError:
                                        print("INVALID ENTER GRAM\n")
                                        continue
                                elif u == 4:
                                    try:
                                        o = float(input("ENTER OUNCE\n"))
                                        if o < 0:
                                            print("OUNCE CANNOT BE NEGATIVE\n")
                                        else:
                                            ReS = o * 28.3495
                                            print(f"RESULT = {ReS:,.3f} GRAM\n")
                                    except ValueError:
                                        print("INVALID ENTER OUNCE\n")
                                        continue
                                elif u == 5:
                                    confirmation = input("ARE YOU SURE YOU WANT TO EXIT?(Y/N)\n")
                                    if confirmation == "Y" or confirmation == "y" or confirmation == "YES" or confirmation == "yes":
                                        print("OK, BACKING...\n")
                                        break
                                    elif confirmation == "N" or confirmation == "n" or confirmation == "NO" or confirmation == "no":
                                        print("THANKS FOR REUSING IT\n")
                                        continue
                                    else:
                                        print("SORRY, CANNOT PROCEED\n")
                                        continue
                                else:
                                    print("INVALID ENTER CHOICE\n")
                                    continue
                            except ValueError:
                                print("INVALID INPUT, TRY AGAIN\n")
                                continue
                    elif u == 2:
                        while True:
                            try:
                                print(
                                    "CHOOSE \n1.CELSIUS TO FAHRENHEIT\n2.FAHRENHEIT TO CELSIUS\n3.CELSIUS TO KELVIN\n4.KELVIN TO CELSIUS\n5.BACK")
                                u = int(input("YOUR CHOICE (DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                                if u == 1:
                                    try:
                                        c = float(input("ENTER CELSIUS\n"))
                                        R = c * 9 / 5 + 32
                                        print(f"RESULT = {R:,.3f} FAHRENHEIT\n")
                                    except ValueError:
                                        print("INVALID ENTER CELSIUS\n")
                                        continue
                                elif u == 2:
                                    try:
                                        f = float(input("ENTER FAHRENHEIT\n"))
                                        Re = (f - 32) * 5 / 9
                                        print(f"RESULT = {Re:,.3f} CELSIUS\n")
                                    except ValueError:
                                        print("INVALID ENTER FAHRENHEIT\n")
                                        continue
                                elif u == 3:
                                    try:
                                        ce = float(input("ENTER CELSIUS\n"))
                                        RE = ce + 273.15
                                        print(f"RESULT = {RE:,.3f} KELVIN\n")
                                    except ValueError:
                                        print("INVALID ENTER CELSIUS\n")
                                        continue
                                elif u == 4:
                                    try:
                                        k = float(input("ENTER KELVIN\n"))
                                        if k < 0:
                                            print("KELVIN CANNOT BE NEGATIVE\n")
                                        else:
                                            R = k - 273.15
                                            print(f"RESULT = {R:,.3f} CELSIUS\n")
                                    except ValueError:
                                        print("INVALID ENTER KELVIN\n")
                                        continue
                                elif u == 5:
                                    confirmation = input("ARE YOU SURE YOU WANT TO EXIT?(Y/N)\n")
                                    if confirmation == "Y" or confirmation == "y" or confirmation == "YES" or confirmation == "yes":
                                        print("OK, BACKING...\n")
                                        break
                                    elif confirmation == "N" or confirmation == "n" or confirmation == "NO" or confirmation == "no":
                                        print("THANKS FOR REUSING IT\n")
                                        continue
                                    else:
                                        print("SORRY, CANNOT PROCEED\n")
                                        continue
                                else:
                                    print("INVALID ENTER CHOICE\n")
                                    continue
                            except ValueError:
                                print("INVALID INPUT, TRY AGAIN\n")
                                continue
                    elif u == 4:
                        while True:
                            try:
                                print("CHOICE\n1.ACRE TO SQUARE METER\n2.SQUARE METER TO ACRE\n3.BACK")
                                u = int(input("YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                                if u == 1:
                                    try:
                                        a = float(input("ENTER ACRE\n"))
                                        if a < 0:
                                            print("ACRE CANNOT BE NEGATIVE\n")
                                        else:
                                            RESu = a * 4046.86
                                            print(f"RESULT = {RESu:,.3f} SQUARE METER\n")
                                    except ValueError:
                                        print("INVALID ENTER ACRE\n")
                                        continue
                                elif u == 2:
                                    try:
                                        s = float(input("ENTER SQUARE METER\n"))
                                        if s < 0:
                                            print("SQUARE METER CANNOT BE NEGATIVE\n")
                                        else:
                                            RESU = s / 4046.86
                                            print(f"RESULT = {RESU:,.3f} ACRE\n")
                                    except ValueError:
                                        print("INVALID ENTER SQUARE METER\n")
                                        continue
                                elif u == 3:
                                    confirmation = input("ARE YOU SURE YOU WANT TO EXIT?(Y/N)\n")
                                    if confirmation == "Y" or confirmation == "y" or confirmation == "YES" or confirmation == "yes":
                                        print("OK, BACKING...\n")
                                        break
                                    elif confirmation == "N" or confirmation == "n" or confirmation == "NO" or confirmation == "no":
                                        print("THANKS FOR REUSING IT\n")
                                        continue
                                    else:
                                        print("SORRY, CANNOT PROCEED\n")
                                        continue
                                else:
                                    print("INVALID ENTER CHOICE\n")
                                    continue
                            except ValueError:
                                print("INVALID INPUT, TRY AGAIN\n")
                                continue
                    elif u == 5:
                        while True:
                            try:
                                print("CHOOSE\n1.LITER TO GALLON\n2.GALLON TO LITER\n3.BACK")
                                u = int(input("YOUR CHOICE(DON'T WRITE INSTEAD WRITE NUMBER)\n"))
                                if u == 1:
                                    try:
                                        l = float(input("ENTER LITER\n"))
                                        if l < 0:
                                            print("LITER CANNOT BE NEGATIVE\n")
                                        else:
                                            result = l / 3.78541
                                            print(f"RESULT = {result:,.3f} GALLON\n")
                                    except ValueError:
                                        print("INVALID ENTER LITER\n")
                                        continue
                                elif u == 2:
                                    try:
                                        g = float(input("ENTER GALLON\n"))
                                        if g < 0:
                                            print("GALLON CANNOT BE NEGATIVE\n")
                                        else:
                                            result = g * 3.78541
                                            print(f"RESULT = {result:,.3f} LITER\n")
                                    except ValueError:
                                        print("INVALID ENTER GALLON\n")
                                        continue
                                elif u == 3:
                                    confirmation = input("ARE YOU SURE YOU WANT TO EXIT?(Y/N)\n")
                                    if confirmation == "Y" or confirmation == "y" or confirmation == "YES" or confirmation == "yes":
                                        print("OK, BACKING...\n")
                                        break
                                    elif confirmation == "N" or confirmation == "n" or confirmation == "NO" or confirmation == "no":
                                        print("THANKS FOR REUSING IT\n")
                                        continue
                                    else:
                                        print("SORRY, CANNOT PROCEED\n")
                                        continue
                                else:
                                    print("INVALID ENTER CHOICE\n")
                                    continue
                            except ValueError:
                                print("INVALID INPUT, TRY AGAIN\n")
                                continue
                    elif u == 6:
                        confirmation = input("ARE YOU SURE YOU WANT TO EXIT?(Y/N)\n")
                        if confirmation == "Y" or confirmation == "y" or confirmation == "YES" or confirmation == "yes":
                            print("OK, BACKING...\n")
                            break
                        elif confirmation == "N" or confirmation == "n" or confirmation == "NO" or confirmation == "no":
                            print("THANKS FOR REUSING IT\n")
                            continue
                        else:
                            print("SORRY, CANNOT PROCEED\n")
                            continue
                    else:
                        print("INVALID CHOICE, TRY AGAIN\n")
                        continue
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
                    continue
        elif u==10:
            print("WELCOME TO POOR AI CHATBOT(TO EXIT WRITE exit OR bye)")
            defaultqa = {
                # Basic Greetings
                "hello": "Hey, hello!",
                "hi": "Hello! How are you?",
                "hey": "Hey there! How’s it going?",
                "good morning": "Good morning! Have a wonderful day.",
                "good night": "Good night! Sweet dreams.",
                "bye": "Goodbye! Take care.",
                "see you": "See you soon!",
                "how are you?": "I am fine, thank you. How are you?",
                "i am fine": "Great! How can I help you today?",
                "thank you": "You are welcome!",
                "thanks": "No problem!",
                "who are you?": "I am a Python chatbot created to assist you.",
                "what is your name?": "I am your AI chatbot friend.",
                "who created you?": "I was created by a programmer using Python.",
                "are you human?": "No, I am an AI chatbot.",

                # Daily Life Conversation
                "how is the weather?": "I can’t check weather, but I hope it's nice where you are.",
                "what is your hobby?": "My hobby is chatting with you!",
                "do you like me?": "Of course! I enjoy talking with you.",
                "what is your favorite color?": "I like blue because it feels calm.",
                "what is your favorite food?": "I don’t eat food, but pizza is very popular.",
                "are you smart?": "I am learning from you every day!",
                "can you help me?": "Yes, I’ll try my best to help you.",
                "what is love?": "Love is a deep feeling of affection and care for someone.",
                "tell me a joke": "Why don’t programmers like nature? Too many bugs!",
                "what is friendship?": "Friendship is a bond of trust and care between people.",

                # Programming Related
                "what is python?": "Python is a high-level, interpreted programming language.",
                "what is java?": "Java is an object-oriented programming language widely used in applications.",
                "what is javascript?": "JavaScript makes websites interactive.",
                "what is html?": "HTML is the language of the web, used to structure pages.",
                "what is css?": "CSS is used to style websites.",
                "what is coding?": "Coding means writing instructions for computers.",
                "what is ai?": "AI means Artificial Intelligence, making machines smart.",
                "what is machine learning?": "Machine learning is AI that learns from data.",
                "what is deep learning?": "Deep learning is a type of machine learning using neural networks.",
                "what is data science?": "Data science is analyzing data to find useful information.",
                "what is programming?": "Programming is giving instructions to computers.",
                "how do i learn coding?": "Start with Python, practice daily, and build projects.",
                "teach me python": "Sure! Begin with print statements, variables, and loops.",

                # General Knowledge - Science
                "what is earth?": "Earth is our home planet, the third from the Sun.",
                "what is the sun?": "The Sun is a star at the center of the solar system.",
                "what is the moon?": "The Moon is Earth’s natural satellite.",
                "what is water?": "Water is H2O, essential for life.",
                "what is fire?": "Fire is rapid oxidation that produces heat and light.",
                "who is albert einstein?": "Einstein was a physicist, famous for relativity theory.",
                "who is isaac newton?": "Newton discovered gravity and laws of motion.",
                "what is gravity?": "Gravity is the force that pulls objects together.",
                "what is photosynthesis?": "Photosynthesis is how plants make food using sunlight.",
                "what is electricity?": "Electricity is the flow of electrons powering devices.",

                # General Knowledge - Geography
                "what is bangladesh?": "Bangladesh is a beautiful country in South Asia.",
                "what is dhaka?": "Dhaka is the capital city of Bangladesh.",
                "what is india?": "India is a neighboring country of Bangladesh.",
                "what is the nile?": "The Nile is the longest river in the world.",
                "what is everest?": "Mount Everest is the highest mountain in the world.",
                "what is asia?": "Asia is the largest continent in the world.",
                "what is africa?": "Africa is the second-largest continent.",

                # General Knowledge - History
                "who was napoleon?": "Napoleon was a French military leader.",
                "who was hitler?": "Hitler was a German dictator during World War II.",
                "who was gandhi?": "Mahatma Gandhi was a leader of Indian independence.",
                "who was lincoln?": "Abraham Lincoln was the 16th president of the USA.",

                # Sports
                "what is cricket?": "Cricket is a popular bat-and-ball sport.",
                "what is football?": "Football is the world’s most popular sport, also called soccer.",
                "who is messi?": "Lionel Messi is an Argentine footballer, one of the greatest ever.",
                "who is ronaldo?": "Cristiano Ronaldo is a Portuguese football legend.",
                "who is shakib al hasan?": "Shakib Al Hasan is a famous Bangladeshi cricketer.",

                # Fun & Random
                "tell me something": "Did you know? Honey never spoils!",
                "who is your best friend?": "You are my best friend!",
                "can you sing?": "I can’t sing, but I can type songs!",
                "do you sleep?": "No, I never sleep.",
                "do you eat?": "No, I don’t eat food.",
                "are you real?": "I am real as a program inside your computer."
            }

            if os.path.exists("chatbot.json"):
                with open("chatbot.json", "r") as f:
                    qa = json.load(f)
            else:
                qa = defaultqa.copy()

            qa = defaultqa.copy()

            # আবার save করা
            with open("chatbot.json", "w") as f:
                json.dump(qa, f, indent=4)


            def normalize(text):
                text = text.lower().strip()
                text = text.translate(str.maketrans('', '', string.punctuation))
                text = " ".join(text.split())
                return text


            while True:
                u = input("your question: ").strip()
                if normalize(u) in ["bye", "ok, bye", "exit","back"]:
                    print(f"chat bot: bye bye\n")
                    break
                normalized_map = {normalize(k): k for k in qa.keys()}
                matches = difflib.get_close_matches(normalize(u), [normalize(k) for k in qa.keys()], n=1, cutoff=0.6)

                if matches:
                    best_match = normalized_map[matches[0]]
                    print("chat bot: " + qa[best_match])
                else:
                    print("chat bot: I don't know!")
                    with open("chatbot.json", "w") as f:
                        json.dump(qa, f, indent=4)
        elif u==12:
            print("EXITING...")
            break
        elif u==7:
            print("WELCOME TO MINI FAKE ACCOUNT")
            d = {
                "pin": "1234",
                "balance": 0,
            }
            attempts = 5
            while attempts > 0:
                while True:
                    try:
                        pin = (input("TO ENTER PLEASE ENTER YOUR PIN\n")).strip()
                        if pin == d["pin"]:
                            u = int(input(
                                "CHOOSE WHAT ARE YOU WANT\n1.CHECK BALANCE\n2.DEPOSIT BALANCE\n3.WITHDRAW BALANCE\n4.CHANGE PIN\n5.EXIT\n"))
                            if u == 1:
                                attempt = 3
                                u = (input("ENTER YOUR PIN\n"))
                                if u == d["pin"]:
                                    print(f"YOUR BALANCE = {d['balance']} DOLLAR")
                                else:
                                    attempt -= 1
                                    print(f"INCORRECT PIN {attempt} ATTEMPTS LEFT")
                                    if attempt == 0:
                                        print("PIN INCORRECT BACKING...\n")
                                        break
                            elif u == 2:
                                attempt = 3
                                try:
                                    u = (input("ENTER YOUR PIN\n"))
                                    if u == d["pin"]:
                                        D = float(input("AMOUNT OF CASH TO DEPOSIT\n"))
                                        if D > 0:
                                            d["balance"] += D
                                            print(f"DEPOSIT SUCCESSFULLY COMPLETE, YOUR BALANCE = {d['balance']} DOLLAR")
                                        else:
                                            print("DEPOSIT FAILED FOR NEGATIVE AMOUNT")
                                    else:
                                        attempt -= 1
                                        print(f"INCORRECT PIN {attempt} ATTEMPTS LEFT")
                                        if attempt == 0:
                                            print("PIN INCORRECT BACKING...\n")
                                            break
                                except ValueError:
                                    print("DEPOSIT FAILED FOR INVALID INPUT")
                            elif u == 3:
                                Attempts = 3
                                try:
                                    u = (input("ENTER YOUR PIN\n"))
                                    if u == d["pin"]:
                                        D = float(input("AMOUNT OF CASH TO WITHDRAW\n"))
                                        if 0 < D <= d["balance"]:
                                            d["balance"] -= D
                                            print(f"WITHDRAW SUCCESSFULLY COMPLETE, YOUR BALANCE = {d['balance']} DOLLAR")
                                        else:
                                            print("WITHDRAW FAILED FOR NEGATIVE AMOUNT")
                                    else:
                                        Attempts -= 1
                                        print(f"INCORRECT PIN {Attempts} ATTEMPTS LEFT")
                                        if Attempts == 0:
                                            print("PIN INCORRECT BACKING...\n")
                                            break
                                except ValueError:
                                    print("WITHDRAW FAILED FOR INVALID INPUT")
                            elif u == 4:
                                attempt = 3
                                try:
                                    u = (input("ENTER YOUR PIN\n"))
                                    if u == d["pin"]:
                                        n = (input("ENTER YOUR NEW 4 DIGIT PIN\n"))
                                        if n.isdigit():
                                            d["pin"] = n
                                            print(f"PIN CHANGED SUCCESSFULLY! YOUR PIN IS {d['pin']}")
                                        else:
                                            print("INVALID PIN(ENTER 4 DIGIT PIN)")
                                    else:
                                        attempt -= 1
                                        print(f"INCORRECT PIN {attempt} ATTEMPTS LEFT")
                                        if attempt == 0:
                                            print("PIN INCORRECT BACKING...\n")
                                            break
                                except ValueError:
                                    print("INVALID PIN, TRY AGAIN")
                                    continue
                            elif u == 5:
                                attempt = 3
                                u = (input("ENTER YOUR PIN\n"))
                                if u == d["pin"]:
                                    print("BACKING...\n")
                                    break
                                else:
                                    attempt -= 1
                                    print(f"INCORRECT PIN {attempt} ATTEMPTS LEFT")
                                    if attempt == 0:
                                        print("PIN INCORRECT BACKING...\n")
                                        break
                            else:
                                print("WRONG CHOICE, TRY AGAIN")
                                continue
                        else:
                            attempts -= 1
                            print(f"WRONG PIN, YOU HAVE {attempts} ATTEMPTS LEFT")
                    except ValueError:
                        print("INVALID INPUT, TRY AGAIN")
                        continue
                    else:
                        if attempts == 0:
                            print("YOU HAVE 0 ATTEMPTS LEFT, SO BACKING...\n")
                            break
        elif u==8:
            l = {
                "Wikipedia": "https://wikipedia.org",
                "Britannica": "https://britannica.com",
                "Khan Academy": "https://khanacademy.org",
                "Coursera": "https://coursera.org",
                "edX": "https://edx.org",
                "MIT OpenCourseWare": "https://ocw.mit.edu",
                "Stanford Online": "https://online.stanford.edu",
                "OpenLearn": "https://www.open.edu/openlearn",
                "National Geographic": "https://www.nationalgeographic.com",
                "HowStuffWorks": "https://www.howstuffworks.com",
                "NASA": "https://www.nasa.gov",
                "TED": "https://www.ted.com",
                "Project Gutenberg": "https://www.gutenberg.org",
                "JSTOR": "https://www.jstor.org",
                "Google Scholar": "https://scholar.google.com",
                "ResearchGate": "https://www.researchgate.net",
                "PubMed": "https://pubmed.ncbi.nlm.nih.gov",
                "ScienceDirect": "https://www.sciencedirect.com",
                "Encyclopedia.com": "https://www.encyclopedia.com",
                "Internet Archive": "https://archive.org"
            }
            l_lower = {k.lower(): v for k, v in l.items()}
            print("WELCOME TO LINK SEARCHER")
            while True:
                u = input("ENTER NAME FOR LINK AND HTTP(TYPE EXIT TO BACK)\n").strip().lower()
                if u.lower() == "exit":
                    print("BACKING...")
                    break
                if u in l_lower:
                    print(f"LINK: {l_lower[u]}")
                else:
                    match = difflib.get_close_matches(u, l_lower.keys(), n=1, cutoff=0.6)
                    if match:
                        print(f"LINK: {l_lower[match[0]]}")
                    else:
                        print(f"I HAVE NO LINK FOR {u}\n")
                        continue
        elif u==9:
            print("WELCOME TO YOUR BOOK LIBRARY")
            library={}
            favourite={}
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r") as f:
                    try:
                        tasks = json.load(f)
                    except json.JSONDecodeError:
                        library = json.load(f)
            else:
                library = {}
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r") as f:
                    try:
                        tasks = json.load(f)
                    except json.JSONDecodeError:
                        favourite = json.load(f)
            else:
                favourite = {}
            while True:
                print(
                    "CHOOSE\n1.ADD BOOK\n2.DELETE BOOK\n3.SEE BOOK\n4.SEE ALL BOOKS\n5.UPDATE BOOK\n6.ADD FAVOURITE BOOK\n7.SEE FAVOURITE BOOK\n8.SEE ALL FAVOURITE BOOKS\n9.DELETE FAVOURITE BOOK\n10.CHANGE FAVOURITE BOOK\n11.SAVE ALL NORMAL BOOKS\n12.SAVE ALL FAVOURITE BOOKS\n13.BACK")
                u = (input("CHOOSE(ONLY NUMBER)\n").strip())
                if not u.isdigit():
                    print("INVALID INPUT, PLEASE ENTER A NUMBER\n")
                    continue
                choice = int(u)
                if u == "1":
                    name = input("ENTER YOUR BOOK NAME\n").strip()
                    author = input("ENTER YOUR BOOK'S AUTHOR NAME\n").strip()
                    if name in library:
                        print("BOOK ALREADY EXISTS\n")
                    else:
                        library[name] = author
                        print("BOOK ADDED SUCCESSFULLY\n")
                elif u == "2":
                    delite = input("ENTER YOUR BOOK NAME TO DELETE\n").strip()
                    if delite in library:
                        del library[delite]
                        print("BOOK DELETED SUCCESSFULLY\n")
                    else:
                        print("BOOK NOT FOUNDED\n")
                        continue
                elif u == "3":
                    s = input("ENTER YOUR BOOK NAME TO SEE\n").strip()
                    if s in library:
                        print(f"THE BOOK {s} BY {library[s]}\n")
                    else:
                        print("BOOK NOT FOUND\n")
                        continue
                elif u == "5":
                    U = input("ENTER YOUR BOOK NAME TO UPDATE\n").strip()
                    if U in library:
                        up = input(f"ENTER NEW AUTHOR NAME FOR {U}\n").strip()
                        library[U] = up
                        print("BOOK UPDATED SUCCESSFULLY\n")
                    else:
                        print("BOOK NOT FOUND\n")
                        continue
                elif u == "4":
                    if not library:
                        print("BOOK NOT FOUND\n")
                        continue
                    else:
                        print("ALL BOOKS\n")
                        for i, (a, b) in enumerate(library.items(), start=1):
                            print(f"{i}. {a} BY {b}\n")
                elif u=="11":
                    with open("library.json", "w") as f:
                        json.dump(library, f)
                    print("ALL NORMAL BOOKS SAVED IN NORMAL LIBRARY\n")
                    continue
                elif u=="12":
                    with open("favourite.json", "w") as f:
                        json.dump(favourite, f)
                    print("ALL FAVOURITE BOOKS SAVED IN FAVOURITE LIBRARY\n")
                    continue
                elif u == "13":
                    print("BACKING...\n")
                    break
                elif u == "6":
                    fn = input("ENTER YOUR FAVOURITE BOOK NAME\n").strip()
                    fa = input("ENTER YOUR FAVOURITE BOOK AUTHOR NAME\n").strip()
                    if fn in favourite:
                        print(f"BOOK {fn} ALREADY EXISTS\n")
                    else:
                        favourite[fn] = fa
                        print("FAVOURITE BOOK ADDED SUCCESSFULLY\n")
                elif u == "7":
                    se = input("ENTER YOUR FAVOURITE BOOK NAME TO SEE\n").strip()
                    if se in favourite:
                        print(f"THE FAVOURITE BOOK {se} BY {favourite[se]}\n")
                    else:
                        print("FAVOURITE BOOK NOT FOUND\n")
                elif u == "8":
                    if not favourite:
                        print("FAVOURITE BOOK NOT FOUND\n")
                        continue
                    else:
                        print("ALL FAVOURITE BOOKS\n")
                        for i, (a, b) in enumerate(favourite.items(), start=1):
                            print(f"{i}. {a} BY {b}\n")
                elif u == "9":
                    de = input("ENTER YOUR FAVOURITE BOOK NAME TO DELETE\n").strip()
                    if de in favourite:
                        del favourite[de]
                        print("FAVOURITE BOOK DELETED SUCCESSFULLY\n")
                    else:
                        print("FAVOURITE BOOK NOT FOUNDED\n")
                elif u == "10":
                    UP = input("ENTER YOUR FAVOURITE BOOK NAME TO CHANGE\n").strip()
                    if UP in favourite:
                        up = input(f"ENTER NEW AUTHOR NAME FOR {UP}\n").strip()
                        favourite[UP] = up
                        print("FAVOURITE BOOK UPDATED SUCCESSFULLY\n")
                    else:
                        print("FAVOURITE BOOK NOT FOUND\n")
                else:
                    print("INVALID INPUT\n")
                    continue
        elif u == 11:
            print("WELCOME TO MINI FAKE ACCOUNT WITH CASH")
            accounts = {}
            balances = {}
            while True:
                try:
                    choice = input(
                        "CHOOSE\n"
                        "1.CREATE NEW ACCOUNT\n"
                        "2.CHANGE ACCOUNT PASSWORD\n"
                        "3.DELETE ACCOUNT\n"
                        "4.SEE ALL ACCOUNT\n"
                        "5.SEE ACCOUNT\n"
                        "6.SEE BALANCE\n"
                        "7.WITHDRAW\n"
                        "8.DEPOSIT\n"
                        "9.EXIT\nYOUR CHOICE(ONLY NUMBERS)\n"
                    ).strip()
                    if choice == "1":
                        name = input("ENTER YOUR ACCOUNT NAME\n").strip()
                        if name in accounts:
                            print("ACCOUNT ALREADY EXISTS\n")
                            continue
                        password = input("ENTER YOUR PASSWORD\n").strip()
                        accounts[name] = password
                        balances[name] = 0
                        print(f"ACCOUNT CREATED SUCCESSFULLY! INITIAL BALANCE = {balances[name]} DOLLAR")
                    elif choice == "2":
                        name = input("ENTER YOUR ACCOUNT NAME\n").strip()
                        if name in accounts:
                            attempt = 3
                            while attempt > 0:
                                old_pass = input("ENTER YOUR OLD PASSWORD\n").strip()
                                if old_pass == accounts[name]:
                                    new_pass = input("ENTER YOUR NEW PASSWORD\n").strip()
                                    if len(new_pass) >= 4:
                                        accounts[name] = new_pass
                                        print("PASSWORD CHANGED SUCCESSFULLY\n")
                                        break
                                    else:
                                        print("INVALID NEW PASSWORD, MUST BE AT LEAST 4 CHARACTERS\n")
                                else:
                                    attempt -= 1
                                    print(f"INCORRECT PASSWORD. {attempt} ATTEMPTS LEFT\n")
                                    if attempt == 0:
                                        print("TOO MANY WRONG ATTEMPTS, EXITING PASSWORD CHANGE\n")
                        else:
                            print("ACCOUNT NOT FOUND\n")
                    elif choice == "3":
                        name = input("ENTER YOUR ACCOUNT NAME TO DELETE\n").strip()
                        if name in accounts:
                            attempt = 3
                            while attempt > 0:
                                password = input("ENTER YOUR PASSWORD TO DELETE ACCOUNT\n").strip()
                                if password == accounts[name]:
                                    del accounts[name]
                                    del balances[name]
                                    print("ACCOUNT DELETED SUCCESSFULLY\n")
                                    break
                                else:
                                    attempt -= 1
                                    print(f"WRONG PASSWORD, {attempt} ATTEMPTS LEFT\n")
                                    if attempt == 0:
                                        print("TOO MANY WRONG ATTEMPTS, CANNOT DELETE ACCOUNT\n")
                        else:
                            print("ACCOUNT NOT FOUND\n")
                    elif choice == "4":
                        if accounts:
                            print("ALL ACCOUNTS\n")
                            for name, password in accounts.items():
                                print(f"ACCOUNT NAME: {name} | PASSWORD: {password} | BALANCE: {balances[name]}")
                        else:
                            print("NO ACCOUNTS FOUND\n")
                    elif choice == "5":
                        name = input("ENTER ACCOUNT NAME TO SEE\n").strip()
                        if name in accounts:
                            print(f"ACCOUNT NAME: {name} | PASSWORD: {accounts[name]} | BALANCE: {balances[name]}")
                        else:
                            print("ACCOUNT NOT FOUND\n")
                    elif choice == "6":
                        name = input("ENTER ACCOUNT NAME TO SEE BALANCE\n").strip()
                        if name in balances:
                            print(f"YOUR BALANCE = {balances[name]}\n")
                        else:
                            print("ACCOUNT NOT FOUND\n")
                    elif choice == "7":
                        name = input("ENTER ACCOUNT NAME TO WITHDRAW\n").strip()
                        if name in balances:
                            attempt = 3
                            while attempt > 0:
                                password = input("ENTER PASSWORD\n").strip()
                                if password == accounts[name]:
                                    if balances[name] == 0:
                                        print(f"YOUR BALANCE = {balances[name]} DOLLAR, SO YOU CAN'T WITHDRAW ANY DOLLAR\n")
                                        break
                                    try:
                                        amount = float(input("ENTER AMOUNT TO WITHDRAW\n"))
                                        if 0 < amount <= balances[name]:
                                            balances[name] -= amount
                                            print(f"WITHDRAW SUCCESSFUL! NEW BALANCE = {balances[name]} DOLLAR\n")
                                            break
                                        else:
                                            print("INVALID AMOUNT\n")
                                    except ValueError:
                                        print("INVALID INPUT, ENTER A NUMBER\n")
                                else:
                                    attempt -= 1
                                    print(f"WRONG PASSWORD, {attempt} ATTEMPTS LEFT\n")
                                    if attempt == 0:
                                        print("TOO MANY WRONG ATTEMPTS\n")
                        else:
                            print("ACCOUNT NOT FOUND")
                    elif choice == "8":
                        name = input("ENTER ACCOUNT NAME TO DEPOSIT\n").strip()
                        if name in balances:
                            attempt = 3
                            while attempt > 0:
                                password = input("ENTER PASSWORD\n").strip()
                                if password == accounts[name]:
                                    try:
                                        amount = float(input("ENTER AMOUNT TO DEPOSIT\n"))
                                        if amount > 0:
                                            balances[name] += amount
                                            print(f"DEPOSIT SUCCESSFUL! NEW BALANCE = {balances[name]} DOLLAR\n")
                                            break
                                        else:
                                            print("AMOUNT MUST BE POSITIVE\n")
                                    except ValueError:
                                        print("INVALID INPUT, ENTER A NUMBER\n")
                                else:
                                    attempt -= 1
                                    print(f"WRONG PASSWORD, {attempt} ATTEMPTS LEFT\n")
                                    if attempt == 0:
                                        print("TOO MANY WRONG ATTEMPTS\n")
                        else:
                            print("ACCOUNT NOT FOUND\n")
                    elif choice == "9":
                        print("GOODBYE\n")
                        break
                    else:
                        print("INVALID CHOICE, TRY AGAIN\n")
                except ValueError:
                    print("INVALID INPUT, TRY AGAIN\n")
        else:
            print("INVALID CHOICE, TRY AGAIN\n")
            continue
    except ValueError:
        print("INVALID INPUT, TRY AGAIN\n")
        continue