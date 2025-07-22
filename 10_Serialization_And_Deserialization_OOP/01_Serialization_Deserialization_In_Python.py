# ------------------------------------------------------------
# Serialization and Deserialization in Python using `pickle`
# ------------------------------------------------------------

# What is Serialization?
# Serialization means converting a Python object (like a dictionary, list, class object)
# into a byte stream that can be saved to a file or sent over a network.

# What is Deserialization?
# Deserialization is the reverse process — converting a byte stream back into the original Python object.

# Why use Serialization?
# - To save program state to disk
# - To send Python objects between systems
# - To store trained ML models
# - To cache results for faster processing

# Example Scenario:
# Imagine you trained a Machine Learning model. You want to save it and use it later — you serialize (pickle) it.

# ------------------------------------------------------------
# Using `pickle` in Python
# ------------------------------------------------------------
import pickle

# Example 1: Simple Dictionary
data = {'name': 'Alice', 'age': 30, 'marks': [90, 85, 88]}

# --------------------------
# SERIALIZATION (Pickling)
# --------------------------
# This will save the data into a binary file called 'data.pkl'
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

print(" Data has been serialized and saved to 'data.pkl'.")

# ------------------------------
# DESERIALIZATION (Unpickling)
# ------------------------------
# Now we'll load the data back from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(" Data has been loaded from 'data.pkl':")
print(loaded_data)

# ------------------------------------------------------------
# Other Example: Serializing a Custom Class
# ------------------------------------------------------------

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}"

# Create object
student1 = Student("Yasir", 101)

# Serialize the object
with open("student.pkl", "wb") as file:
    pickle.dump(student1, file)

# Deserialize the object
with open("student.pkl", "rb") as file:
    loaded_student = pickle.load(file)

print(" Loaded student object:")
print(loaded_student.display())

# ------------------------------------------------------------
#  WARNING
# ------------------------------------------------------------
# NEVER unpickle data from an untrusted or unknown source.
# Pickle files can execute malicious code if tampered with.

#  Important Points
#  Use `pickle.dump(obj, file)` to serialize
#  Use `pickle.load(file)` to deserialize
#  Pickle works for lists, dicts, custom classes, and more
#  Don't use it for cross-language communication (use JSON instead)

