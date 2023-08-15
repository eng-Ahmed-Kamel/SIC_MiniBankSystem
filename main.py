import json
# function of currency conversion and return true , value of money
def currency_conversion(the_currency,value):
    if the_currency == "USD" or the_currency == "usd":
        money= int(value) * 30
    elif the_currency == "SAR" or the_currency == "sar":
        money= int(value) * 9
    elif the_currency == "EGP" or the_currency == "egp":
        money= int(value)
    else:
        return [False]
    return [True,money]
#------------------------------------------
# function to open json and update it
def save():
    bank_data = open("SIC_bank_data.json", "w")
    json.dump(the_data, bank_data, indent=2)
    bank_data.close()
#--------------------------------------------
# function to register new user and check if account is found
def register():
    global id
    print("******Welcome to sign up page", '*******')
    # checking if the data is empty or not ignored first index because it's the id counter
    if the_data[1:] == list():
        mail = input('please enter your mail:')
        pass_word = input('please enter your password:')
        phone = input('please enter your phone:')
        name = input('please enter your name:')
        gender = input('please enter your gender:')
        age = input('please enter your age:')
        city = input('please enter your city:')
        # the user data
        user = {"id": id, "name": name, "password": pass_word, "phone": phone, "mail": mail, "gender": gender,
                "age": age, "city": city, "balance": 0}
        print('singed in successfully and your ID is:', id)
        # updating the data
        the_data.append(user)
        id += 1
        the_data[0] = id
        # uploading the new data
        save()
    else:
        mail = input('please enter your mail:')
        # checking if the name already exists
        found = False
        for i in the_data[1:]:
            for k, v in i.items():
                if k == "mail" and v == mail:
                    found = True
        if found:
            print("you already have account !!")
        else:
            pass_word = input('please enter your password:')
            phone = input('please enter your phone:')
            name = input('please enter your name:')
            gender = input('please enter your gender:')
            age = input('please enter your age:')
            city = input('please enter your city:')
            # the user data
            #
            user = {"id": id, "name": name, "password": pass_word, "phone": phone, "mail": mail, "gender": gender,
                    "age": age, "city": city, "balance": 0}
            print('singed in successfully and your ID is:', id)
            # updating the new data
            #
            the_data.append(user)
            id += 1
            the_data[0] = id
            # uploading the new data
            #
            save()
#----------------------------------------------------
# function to deposite
def deposit():
    deposit_amount = input("please enter the amount you want to deposit and the "
                           "currency in this format'1 EGP'\n=> ")
    deposit_amount_list = deposit_amount.split()
    the_currency=0
    if len(deposit_amount_list)==2:
        the_currency = deposit_amount_list[1]
    else :
        print("please enter a valid currency")
        return False
    D = 0
    conversation =currency_conversion(the_currency,deposit_amount_list[0])
    if conversation[0]:
        D+=conversation[1]
    else:
        print("please enter a valid currency")
        return False
    
    user_data["balance"] += D
    the_data[data_index] = user_data
    save()
    print(deposit_amount, 'was deposited successfully!!')
    print('your balance is :', user_data['balance'], "EGP")
    return True
#------------------------------------
# function to transfer
def transfer():
    trans_money = input("Enter the amount of money you want to transfer by EGP: ")
    trans_money_splited = trans_money.split()
    if trans_money_splited[0] == "":
        print("invalid please try again !!")
        return False
    else:
        trans_id = input("Enter the id you want to transfer to: ")
        if trans_id == "":  # ??????
            print("invalid input")
            return False
        else:
            user_data2 = None
            trans_index = None
            for i in range(1, len(the_data)):
                for k, v in the_data[i].items():
                    if k == "id" and str(v) == trans_id:
                        user_data2 = the_data[i]
                        trans_index = i

            if user_data2 != None:
                if user_data["balance"] >= int(trans_money_splited[0]):
                    user_data["balance"] -= int(trans_money_splited[0])
                    user_data2["balance"] += int(trans_money_splited[0])
                    the_data[trans_index] = user_data2
                    the_data[data_index] = user_data
                    save()
                    print(trans_money, "successfully transferred to", user_data2["name"])
                    print("your balance now is: ", user_data["balance"])
                    print("\n")
                    return True
                else:
                    print("SORRY !! you don't have enough money")
                    print("\n")
                    return False
            else:
                print("didn't find that id =>", trans_id)
                print("\n")
                return False
#----------------------------------
# function of login
def login():
    print("******Welcome to login page", '*******')
    # taking the ID
    ID = input('please enter your ID: ')
    # checking the ID, searching for the id of the user
    global user_data 
    global data_index
    for i in range(1, len(the_data)):
        for k, v in the_data[i].items():
            if k == "id" and str(v) == ID:
                user_data = the_data[i]  # putting the user data (dictionary) in user_data variable
                data_index = i  # putting the index of the user data in data_index
    # Checking if the user id exists
    if user_data != None:
        # taking the password
        user_password = input("Enter your password: ")
        # Checking if the password is true
        for k, v in user_data.items():
            if k == "password" and v == user_password:
                return [True ,data_index,user_data]
        return [False, data_index]
    return [False, data_index]
#---------------------------------------------
# withdraw function
def withdraw():
    withdraw_amount = input("please enter the amount you want to withdraw and the currency in "
                                                    "this format'1 EGP'\n")
    withdraw_amount_list = withdraw_amount.split()
    w = 0
    the_currency=0
    if len(withdraw_amount_list)==2:
        the_currency = withdraw_amount_list[1]
    else :
        print("please enter a valid currency")
        return False
    conversation =currency_conversion(the_currency,withdraw_amount_list[0])
    if conversation[0]:
        w+=conversation[1]
    else:
        print("please enter a valid currency")
        return False
# check balance
    if user_data["balance"] >= w:
        # updating the data and uploading it
        user_data["balance"] -= w
        the_data[data_index] = user_data
        save()
        print(withdraw_amount, 'was withdrawn successfully!!')
        print('your balance is :', user_data['balance'], "EGP")
        return True
    else:
        print(withdraw_amount, 'was withdrawn  unsuccessfully!!')
        print('wrong transaction no enough balance')
        return False
#---------------------------
# check personal information function
def check():
    for k, v in user_data.items():
        print(k, ":", v)
    print("\n")
#-----------------------------
# show menu fun
def show_menu():
    print(" welcome back", user_data["name"], )
    x = input(
        "please enter your choice :\n[0]Deposit\n[1]withdraw\n[2]Transfer\n[3]check balance & personal info"
        "\n[4]Back\n=> ")
    return x

#*******************************************************
#*********************main******************************
while True:
    # taking the request (LOGIN or REGISTER)
    print("******Welcome to SIC bank managment system", '*******')
    user_choice = input(
        "If you already have an account please enter : login \nIf you don't already have an account please enter : register\nIf you want to exit please press enter \n ==> ")
    # loading the data and getting latest id
    bank_data = open("SIC_bank_data.json")
    the_data=json.load(bank_data)
    bank_data.close()
    id = the_data[0]
    # user choose to login
    if user_choice == "login" or user_choice == "LOGIN":
            user_data=None
            data_index = None  # the index of the user data (dictionary) in the bank data (list of dictionaries)
            is_found=login()
            if is_found[0]:
                data_index=is_found[1]
                user_data=is_found[2]
                while True:
                    x=show_menu()
                    if x == "0":
                        # deposit function
                        while True:
                            if deposit():
                                break
                    elif x == "1":
                        # withdraw function
                        while True:
                            if withdraw():
                                break
                    elif x == "2":
                        # transfer function
                        while True:
                            if transfer():
                                break
                    elif x == "3":
                        # check & info ---------------------
                        check()
                    elif x == "4":
                        # exit case
                        print('Back successfully ')
                        break
                    else:
                        # wrong input case
                        print("Wrong choice, please try again !!")
            elif is_found[0]==False and user_data!=None:
                print("wrong Password !!")
            else:
                print("Didn't find this ID !!")
    # user choose to register
    elif user_choice == "register" or user_choice == "REGISTER":
       register()
    elif user_choice == "":
        break
    else:
        print("Please enter a one of the given choices")