# This example teaches you how to...
#   - Define Classes With Constructor And Getter Methods
#   - Fetch User Input, Return It As A Python Tuple, & Use The Provided Data
#   - Increase Maintainability & Reusability Of Your Code By Storing Most Of It Into Classes & Functions
#   - Control Execution Of The Script By Checking Whether It Was Called Directly Or Imported By Another Script

# Character Class
class Character:
	# Constructor
	def __init__(self, Name, Gender, Race, Background, Class, Level=1):
		self.name = Name
		self.gender = Gender
		self.race = Race
		self.background = Background
		self.character_class = Class
		self.level = Level

	def print_details(self):
		print(self.__dict__)
		
# Fetches User Input
def ask_for_character():
		tmp_name = input("\nPlease Enter Your Name.\n")
		tmp_gender = input("\nPlease Enter Your Gender.\n")
		tmp_race = input("\nPlease Enter Your Race.\n")
		tmp_background = input("\nPlease Enter Your Background.\n")
		tmp_class = input("\nPlease Enter Your Character Class.\n")
		tmp_level = input("\nPlease Enter Your Level.\n")
		return tmp_name, tmp_gender, tmp_race, tmp_background, tmp_class, tmp_level
		
#Main Function
def main():
	details = ask_for_character()
	example = Character(details[0], details[1], details[2], details[3], details[4], details[5])
	print("\n\n")
	example.print_details()
	

# Driver Code
if __name__ == "__main__":
	main()
else:
	print(f"{__name__} has been successfully imported.")
