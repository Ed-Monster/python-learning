STARS = "**************************************************"

""" case converting """
print(STARS)
# the original string
ada = "ada lovelace"
print("ada = " + ada)
# each word begins with a capitalized letter
Ada = ada.title()
print("Ada = " + Ada)
# all uppercase
ADA = ada.upper()
print("ADA = " + ADA)
print(STARS + "\n")

""" use fomat strings """
print(STARS)
print(f"{ada} or {Ada} or {ADA}?")
print(STARS + "\n")

""" strip whitespaces """
print(STARS)
# with whitespaces at the left and the right sides
str_py = " python "
print(f"'{str_py}'")
# strip leftside
print(f"'{str_py.lstrip()}'")
# strip rightside
print(f"'{str_py.rstrip()}'")
# strip both sides
print(f"'{str_py.strip()}'")
print(STARS)