"""
Description:
This module calculates the perimeter, area, and volume of a room.

Args:
This module takes in a length, width, & height for use in mathematical formulas.
"""
class Room():
    # CONSTRUCTOR
    def __init__(self, Length, Width, Height, Shape="Rectangle"):
        self.length = int(Length)
        self.width = int(Width)
        self.height = int(Height)
        self.shape = Shape
	def __repr__(self):
		_output = ""
		_output += f"Docstring: \n{self.__doc__}\n\n"
		_output += f"Class: \n{self.__class__}\n\n"
		_output += f"Dict: \n{self.__dict__}\n\n"
		return _output
	def __str__(self):
		_output = ""
		_output += f"Docstring: \n{self.__doc__}\n\n"
		_output += f"Length: \n{self.length}\n"
		_output += f"Width: \n{self.width}\n"
		_output += f"Height: \n{self.height}\n\n"
		_output += f"Area: \n{self.area}\n"
		_output += f"Volume: \n{self.volume}"
		return _output
    # PROPERTIES
    @property
    def area(self):
        if self.shape.lower() == "rectangle":
            area = (self.length * self.width)
            return area
    @property
    def volume(self):
        if self.shape.lower() == "rectangle":
            volume = (self.length * self.width) * self.height
            return volume
    @property
    def perimeter(self):
        if self.shape.lower() == "rectangle":
            perimeter = (self.length + self.width) * 2
            return perimeter
    # METHODS
    def info(self):
        print("\n", f"Room Shape: {self.shape}\n",
            "----------------\n",
            f"Room Length: {self.length}ft.\n",
            f"Room Width: {self.width}ft.\n",
            f"Room Height: {self.height}ft.\n",
            "----------------\n",
            f"Room Perimeter: {self.perimeter}ft.\n",
            f"Room Area: {self.area}ft.\n",
            f"Room Volume: {self.volume}ft.")


# MAIN METHOD
def main():
    """Main Method (Module)"""
    # * Fetch Room Info
    _length = input("\nPlease Enter The Length Of The Room.\t(In Feet)\n")
    _width = input("Please Enter The Width Of The Room.\t(In Feet)\n")
    _height = input("Please Enter The Height Of The Room.\t(In Feet)\n")
    # * Construct Room; Print Details/Calculations
    newRoom = Room(_length, _width, _height)
    newRoom.info()

# DRIVER CODE
if __name__ == "__main__":
    # ? This "while True" Loop Ensures We Can Keep Running The Module As Many Times As We Want.
    while True:
        # * Runs The Main Method
        main()
        # * Ask If the User Wants To Calculate Another Room.
        _again = input("\nWould You Like To Run This Module Again?\n")
        # Run again if the user said "Yes" or "Y"; Otherwise, Break From The Loop.
        if _again.lower() == "yes" or _again.lower() == "y":
            main()
        else:
            break
else:
    # Informs The User That The Module Was Successfully Imported.
    print(f"{__name__} was successfully imported.")
