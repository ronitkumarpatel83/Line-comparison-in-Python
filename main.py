"""
    @Name = Ronit kumar Patel
    @Title = Line Comparison
"""
import logging


class Comparison:
    def cartesian_length(self):
        try:
            x1 = int(input("enter the x1-coordinate of point1 : "))
            y1 = int(input("enter the y1-coordinate of point1 : "))
            x2 = int(input("enter the x2-coordinate of point2 : "))
            y2 = int(input("enter the y2-coordinate of point2 : "))

            length_of_line = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
            print("the distance between two point is : ", length_of_line)
            return length_of_line
        except Exception as e:
            print(e)
            logging.exception(e)

    def equality_of_length(self):
        try:
            x3 = int(input("enter the x2-coordinate of point3 : "))
            y3 = int(input("enter the y2-coordinate of point3 : "))
            x4 = int(input("enter the x2-coordinate of point4 : "))
            y4 = int(input("enter the y2-coordinate of point4 : "))

            length_of_line2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** (1 / 2)
            print("the distance between two point is : ", length_of_line2)
            return length_of_line2
        except Exception as e:
            print(e)
            logging.exception(e)

    def compare_to(self):
        try:
            a = comp_obj.cartesian_length()
            b = comp_obj.equality_of_length()
            diff = a - b
            print("******************************************************************")
            if diff > 0:
                print("line-1 is greater!!!")
            elif diff < 0:
                print("line-2 is greater!!!")
            else:
                print("Both lines are of same length")
            print("******************************************************************")
        except Exception as e:
            print(e)
            logging.exception(e)


if __name__ == '__main__':
    print("********************************************************************************")
    print("<<<<<<<<<<<<----- Welcome to Line-Comparison Computation Program----->>>>>>>>>>>>> ")
    print("********************************************************************************")

    log = '%(lineno)d ** %(asctime)s ** %(message)s'
    logging.basicConfig(filename='line_comparison.log', filemode='a', format=log, level=logging.DEBUG)

    logging.debug("Line comparison computation Program running................")

    try:
        comp_obj = Comparison()
        result = comp_obj.compare_to()
        print(result)
    except Exception as e:
        print(e)
        logging.exception(e)