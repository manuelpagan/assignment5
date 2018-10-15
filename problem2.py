# Manny Pagan
# Sept 24th Python Course
# Assignment 5
# Due: Oct 15th


employees = [
    {
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
    },
    {
    "name": "Leslie Knope",
    "age": "",
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": ""
    },
    {
    "name": "Andy Dwyer",
    "age": "",
    "department": "Shoe Shining",
    "phone": "555-1122",
    "salary": ""
    },
    {
    "name": "April Ludgate",
    "age": "",
    "department": "Administration",
    "phone": "555-3345",
    "salary": ""
    }
]


for i in employees:
    print(i['name'], "in", i['department'], "can be reached at", i['phone'])
