print("this is my weather forecast")
temperature=int(input("please insert the temperature in celsius:"))
humidity=int(input("please insert the humidity of the air:"))
if temperature>30:
    if humidity>90:
        print("its hot and humid")
    else:
        print("its hot but not humid")
else:
    print("its not hot")
