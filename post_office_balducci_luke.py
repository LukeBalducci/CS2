def get_dimensions(length, width, height):
    package_class= ""
    if length >= 3.5 and length <=4.25 and width >= .007 and width <= .016 and height >=3.5 and height <= 6:
        package_class = "regular post card"
    if length >=4.25 and length <= 6 and width >= .007 and width <=.015 and height >= 6 and height <= 11.5:
        package_class = "large Post Card"
    if length >=3.5  and length <=6.125 and width >=.016 and width <= .25 and height >=5 and height <= 11.5: 
        package_class = " envelope"
    if length >= 6.125 and length <= 24 and width >= .25 and width <= .5 and height >=11 and height <= 18:
        package_class = "large envelope"
    if length > 24 or width > .5 or hight > 18 and length + 2 * (width + hight ) < 84:
        package_class = " package"
    if length > 24 or width > .5 or hight > 18 and length + 2 * (width + hight ) > 84: and length + 2 * (width + hight ) <130 :
    package_class = "Large Package"


def get_zip (zip_to,zip_from):
    pass





def main():
    input_data = input("enter data")
    input_data = input_data.split(",")

length= input[0]
width = input[1]
hight = input[2]
zip_to = input[3]
zip_from = input[4]
main()
