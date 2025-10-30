from project.father import Father
from project.mother import Mother
from project.child import Child

child = Child('Chris',12,"Male")
father = Father("Tom")
mother = Mother("Nancy")

print(child.child_info())
print(child.father_name())
print(child.mother_name())