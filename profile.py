def create_profile(name, age, occupation, interests):
  """Creates a simple profile dictionary.

  Args:
    name: The person's name (string).
    age: The person's age (integer).
    occupation: The person's occupation (string).
    interests: A list of the person's interests (list of strings).

  Returns:
    A dictionary representing the profile.
  """
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
    profile: A dictionary containing the profile information (as created by create_profile).
  """
  print("--- Profile ---")
  for key, value in profile.items():
    if key == "interests":
      print(f"{key.capitalize()}: {', '.join(value)}")
    else:
      print(f"{key.capitalize()}: {value}")
  print("---------------")

if __name__ == "__main__":
  # Example usage:
  my_profile = create_profile(
      name="Godfrey Mucunguzi",
      age=24,
      occupation="Programmer",
      interests=["Reading", "Hiking", "Coding"]
  )

  display_profile(my_profile)

  # You can also create profiles for others:
  bob_profile = create_profile(
      name="Edna Kusiima",
      age=31,
      occupation="Nutrition Specialist",
      interests=["Taking photos", "Reading", "Cooking"]
  )
  display_profile(bob_profile)
