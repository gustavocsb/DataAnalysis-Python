print(f"Abs: {abs(-56)}")
print(f"Abs: {abs(23)}")
print(f"Bool: {bool(0)}")
print(f"Bool: {bool(1)}")
print(f"Int: {int(4.3)}")
print(f"Str: {str(13)}")
print(f"Float: {float(5)}")

#idade = input("Digite sua idade: ")
# a função 'input' retorna um valor string, por isso é necessário transformá-lo em outro tipo nesse caso
idade = int(input("Digite sua idade: "))

if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")
else:
    print("Seus pais não deveriam deixar você acessar Redes Sociais sem supervisão!")

    
print(f"Int: {int(26)}")
print(f"Float: ", float("123.345"))
print(f"Str: {str(14)}")
print(f"Len: {len([23,34,45,46])}")

array = [1,2,3]

print(f"Max: {max(array)}")
print(f"Min: {min(array)}")

list1 = [16,23,44,75]

print(f"Sum: {sum(list1)}")