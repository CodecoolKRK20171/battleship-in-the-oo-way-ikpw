def get_coordinates():
        while (True):
            user_input = input("Please enter coordinates (row,col) ? ")
            try:
                coor = user_input.split(",")
                print(coor)
                if len(coor) != 2:
                    raise Exception("Invalid entry, too few/many coordinates.")

                #check if 2 values are integers
                coor[0] = int(coor[0])-1
                coor[1] = int(coor[1])-1

                #check if values of integers are between 1 and 10 for both coordinates
                if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                    raise Exception("Invalid entry. Please use values between 1 to 10 only.")

                #if everything is ok, return coordinates
                return coor

            except ValueError:
                print ("Invalid entry. Please enter only numeric values for coordinates")



def get_ship_direction():

    while(True):
        try:
            user_input = input("vertical or horizontal (v,h) ? ").lower()
            if user_input == "v" or user_input == "h":
                return user_input
        except ValueError:
            print ("Invalid input. Please only enter v or h")
