# Your code goes here:
def render_person(name, dob, eyes, age, gender):
    string = f'{name} is a {age} years old {gender} born in {dob} with {eyes} eyes'
    return string

# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))