def create_profile():
  """Prompts the user for their details and creates a profile dictionary.

  Returns:
    A dictionary representing the user's profile.
  """
  name = input("Enter your name: ")
  age_str = input("Enter your age: ")
  while not age_str.isdigit():
    print("Invalid input. Please enter a number for your age.")
    age_str = input("Enter your age: ")
  age = int(age_str)
  occupation = input("Enter your occupation: ")
  interests_str = input("Enter your interests (separate with commas): ")
  interests = [interest.strip() for interest in interests_str.split(',')]

  profile = {
      "name": name,
      "age": age,
      "occupation": occupation,
      "interests": interests
  }
  return profile

def display_profile(profile):
  """Prints the profile information in a readable format.

  Args:
    profile: A dictionary containing the profile information.
  """
  print("\n--- Your Profile ---")
  for key, value in profile.items():
    if key == "interests":
      print(f"{key.capitalize()}: {', '.join(value)}")
    else:
      print(f"{key.capitalize()}: {value}")
  print("--------------------")

if __name__ == "__main__":
  print("Let's create your profile!")
  user_profile = create_profile()
  display_profile(user_profile)
  print("Profile generated successfully!")
