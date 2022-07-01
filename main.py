"""
    @Name = Ronit kumar Patel
    @Title = Line Comparison
"""


class Comparison:
    def cartesian_length(self):
        x1 = int(input("enter the x1-coordinate of point1 : "))
        y1 = int(input("enter the y1-coordinate of point1 : "))

        x2 = int(input("enter the x2-coordinate of point2 : "))
        y2 = int(input("enter the y2-coordinate of point2 : "))

        length_of_line = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        print("the distance between two point is : ", length_of_line)
        return length_of_line


if __name__ == '__main__':
    print("********************************************************************************")
    print("<<<<<<<<<<<<----- Welcome to Line-Comparison Computation Program----->>>>>>>>>>>>> ")
    print("********************************************************************************")

    comp_obj = Comparison()
    result = comp_obj.cartesian_length()

