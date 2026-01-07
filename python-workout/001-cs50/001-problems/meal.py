# # take input of time
# time = input("What time is it? ")
# hours, minutes = time.split(":")
# hours = int(hours) + int(minutes) / 60
# if 7.0 <= hours <= 8.0:
#     print("breakfast time")
# elif 12.0 <= hours <= 13.0:
#     print("lunch time")
# elif 18.0 <= hours <= 19.0:
#     print("dinner time")

###############################

# def main():
#     time = input("What time is it? ")
#     hours = convert(time)

#     if 7.0 <= hours <= 8.0:
#         print("breakfast time")
#     elif 12.0 <= hours <= 13.0:
#         print("lunch time")
#     elif 18.0 <= hours <= 19.0:
#         print("dinner time")


# def convert(time):
#     hours, minutes = time.split(":")
#     return int(hours) + int(minutes) / 60


# if __name__ == "__main__":
#     main()

##################################

def main():
    time = input("what is time? ")
    hours = convert(time)

    if 7.0 <= hours and hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours and hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours and hours <= 19.0:
        print("dinner time")
    else:
        print("it is not a meal time")


def convert(time):
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
