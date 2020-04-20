# --------------
# Code starts here
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
M=courses.get('Math')
E=courses.get('English')
H=courses.get('History')
F=courses.get('French')
S=courses.get('Science')
total=M+E+H+F+S
print(total)
percentage=(total/500)*100
print(percentage)
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,
'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,
'Corinna Cortes':66,
'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)

topper = 'andrew ng'
# Code starts here
first_name=topper.split()[0]
last_name=topper.split()[1]
space=' '
full_name=last_name + space + first_name 
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


