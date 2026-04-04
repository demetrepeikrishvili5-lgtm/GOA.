#2) კომენტარების სახით ჩამთვალეთ ყველა შედარებითი ოპერატორები და გააკეთეთ 5-5 ნაგალითი თითოეულზე.
# print(5==5) ტოლობა აკეთებს იმას რომ ყველაფერი ერთდაიგივე უნდა იყოს და მკაცრად ამოწმებს print(15>14) ეს აკეთებს რომ 15 მეტია 14 ზე და trues გამოიტანს
#print("true or false") ეს გამოიტანს trues რადგან or ოპერატორის დროს თუ  true წერია აუდცილებლად trues გამოიტანს     != ეს ნიშნავს რომ არასწორია 
# print(true and false)     აქ false გამოიტანს რაადგან and ოპერატორი თუ არის false გამოიტანს აუცილებლად
# >= ეს ნიშნავს რომ ტოლია.
print(5==4)  #false
print(6==6)  #true
print(7==6)  # false
print("ვაშლი"=="ვაშლი") #true
print("კამფეტი"=="ვაშლატამა") #false


print(10>10)  #false
print(4>5)    #false
print(9>8)    #true
print(7>4)    #true
print(9>3)    #true

print(5<3)    # false
print(7<7)    # false
print(5<4)    # false
print(3<9)    # true
print(5<99)   # true

print(True or False) #True
print(False or True)  #True
print(False or False)  #False
print(True or True)  #True
print(False or True)   # True

print(5!=9)  #true
print(1!=1)   #false
print(4!=6)  #true
print(9!=9) #false
print(4!=4) # false

print(True and False) #False
print(False and True)  #False
print(False and False)  #False
print(True and True)  #True
print(False and True)   # False

print(10>=10)  #true
print(99>=99)  #true
print(1001>=100)  #false
print(10>=112)  #false
print(9>=9)  #true

print(12<=12) #true
print(13<=12) #false
print(15<=15) #true
print(14<=15) # true
print(99<=98)  #false





#3) კომენტარების სახით ახსენით რა არის logical operators, ჩამოწერეთ თითოეული და განმარტეთ რომელი რა დროს რა შედეგს გვიბრუნებს.
#აი მაგალითად or ან and-ი

#4) გააკეთეთ 3-3 მაგალითი logical operator-ებზე.

print(False or True)  #true
print(True or False)  #true
print(False or False) #false

print(False and True)  # false
print(True and True )  # true
print(True and False)  #false

#5) მომხმარებელს შემოატანინეთ რიცხვი, შეინახეთ იგი ცვლადში და შეადარეთ იგი მეტია თუ არა თქვენს მიერ წინასწარ გამზადებულ რიცხვზე.
num=int (input("enter number :")) #5
num1=int(input("enter number :")) #6
print(num<num1)

#6) მომხმარებელს შემოატანინეთ სახელი, შეინახეთ იგი ცვლადში და მკაცრად შეამოწმეთ უდრის თუ არა იგი თქვენს სახელს.

name=input("enter name :" ) #demetre
print("demetre"==name)

#7) მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ მეტია თუ არა იგი 18.

age=int(input("enter your age :")) 
print(age>=18)
