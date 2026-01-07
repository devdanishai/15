
# def main():

#     greet = input("say your greetings: ")

#     greet = greet.lower()

#     if greet == "hello" or greet == "hello there" or greet == "hello newman":
#         print("0 $")

#     elif greet == "hey" or greet == "hi" or greet == "how are you?":
#         print("20 $ fine")

#     else:
#         print("100 $ fine")



# if __name__=="__main__":
#     main()


def main():
    greet = input("Say your greetings: ").strip().lower()

    if greet in ["hello", "hello there", "hello newman"]:
        print("0 $")
    elif greet in ["hey", "hi", "how are you?"]:
        print("20 $ fine")
    else:
        print("100 $ fine")


if __name__ == "__main__":
    main()
