class Data:

    def __init__(self, **kwargs):
        """
        class constructor
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def from_dict(cls, data):
        """
        Create an instance of the Data class from a dictionary.

        params: data (dict): Dictionary containing data to load into the Data class.
        returns: Data: An instance of the Data class with the data loaded from the dictionary.
        """
        return cls(**data)

    def to_dict(self):
        """
        Convert the Data instance to a dictionary.

        returns: dict: A dictionary representing the data in the Data instance.
        """
        return vars(self)

    def __getattr__(self, item):
        # Reflects inner value on the main level.
        # set default values.
        # autocomplete


# 1. Loads a dictionary and can save to dictionary: `to_dict`, `from_dict`
data_dict = {
    "id": "1",
    "name": "first",
    "metadata": {
        "system": {
            "size": 10.7
        },
        "user": {
            "batch": 10
        }
    }
}

my_inst_from_dict = Data.from_dict(data_dict)
print(my_inst_from_dict.to_dict())
# Save to dictionary
converted_dict = my_inst_from_dict.to_dict()
print(converted_dict)

# 2. Ability to instantiate directly from the class
my_inst_direct = Data(id="2", name="second", metadata={"system": {
                      "size": 20.3}, "user": {"batch": 15}}, newvalues={'age': 10})
print(my_inst_direct.to_dict())

# 3. Default value: Can define a default value for attributes
# default_values = {
#     "id": "N/A",
#     "name": "Unknown",
#     "metadata": {
#         "system": {
#             "size": 0,
#             "height": 100
#         },
#         "user": {
#             "batch": 1
#         }
#     }
# }

# my_inst_defaults = Data(**default_values)
# print(my_inst_defaults.to_dict())

# 4. Autocomplete
# print(my_inst_defaults.size)

# # 5. Dynamic and general usability for the class (easily define new data structures)
# my_inst_dynamic = Data(color="blue", shape="circle", metadata={
#                        "details": {"material": "plastic"}})
# print(my_inst_dynamic.to_dict())
