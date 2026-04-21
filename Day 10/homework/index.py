#2) ლოგიკური ოპერატორებისა და შედარების ოპერატორებზე შეადგინეთ 10 მაგალითი,5 მაგალითმა უნდა დააბრუნოს False და 5 მაგალითმა უნდა დაააბრუნოს True
print(True and False)  # False
print(False and True)  # False
print(False and False) #False
print(False or False)  #false
print(True and False)  #false

print(True or True) # True
print(True or False) # True
print(True and True) # True
print(False or True) # True
print(True or True)  # True


#3) კომენტარის სახით დაწერეთ თუ რა არის sequancing,iteration,selection აღწერე თითეული მათგანი თქვენი სიტყვებით
# sequancing - სწორედ რომ არის დალაგებული, interation - გამოტოვება სფეიცით, selection -არჩევანი.
#4) მოიყვანე sequencing ის მაგალითი,და კომენტარით მიუწერე რატომ არის შენს მიერ მოყვანილი მაგალითი sequence 
print("gamarjobat")
print("ჩემი სახელია დემეტრე")
print("მე  ვარ 10 წლის და ვსწავლობ Goa-ში")
#5) კომენტარის სახით ახსენით თუ რა არის for loop და რაში გვეხმარება ის
# for loop-ი არის იმისთვის რომ ბევრჯერ ერთდაიგივე არ გავიმეოროთ. 
#6)  კომენტარის სახით ახსენით თუ რა გადაეცემა range() ფუნქციას და როგორ მუშაობს for loop 
# ის გადაეცემა ანუ მასში უნდა ჩაწერო ნებისმიერი რიცხვი რაც გინდა და მის შემდეგ დაპრინტავ რაც გინდა და იმდეჯერ გამოიტანს რაც ჩაწერე range-ში.
# 7) შენი დავალებაა ტერმინალში გამოიყენო საყვარელი ავტომობილის სახელი ტერმინალში გამოიყენე for loop
for i in range(5):
    print("ჟიგული")
#8 ) შენი დავალებაა ტერმინალში გამოიტანო შენი გვარი 100 ჯერ 
for i in range(100):
    print("feikrishvili")

#9) შენი დავალებაა ტერმინალში გამოიტანო საყვარელი ფერი 46 ჯერ
for i in range(46):
    print("black")
#10) შენი დავალებაა ტერმინალში გამოიტანო შენი სახელის პირველი ასო 32 ჯერ 
for i in range(32):
    print("D")

#11) მომხმარებელს შემოატანინე 3 სტრინგ ტიპის და ერთი ინტეჯერ ტიპის მნიშვნელობები და შენი დავალებაა მოახდინო ამ ოთხი მნიშვნელობის კონკატინაცია(გამოიყენე შესაბამისი ფუნქცია რომ მოახდინოთ მონაცემთა ტიპიების გარდაქმნა ერთ მონაცემთა ტიპში რომ შეძლოთ კონკატინაცია)
name=input("enter your name :")
surname=input("enter your surname :")
adress=input("enter your adress :")
age=int(input("enter your age"))
result=name+surname+adress+str(age)
print(result)
#12) შექმენი 4 ცვლადი,თითოეულში შეინახე განსხვავებული მონაცემთა ტიპები,შენი დავალებაა გაიგო ამ ცვლადებში შენახული მნიშვნელობის მონაცემთა ტიპი(გამოიყენე შესაბამისი ფუნქცია)
name="Demetre"
age=10
points=99.5
a=True
print(type(name))
print(type(age))
print(type(points))
print(type(True))
#13) მომხმარებელს შემოატანინე 4 რიცხვი და ტერმინალში დააბრუნე ამ 4 რიცხვის ჯამი
num1=int(input("enter your num1 :"))
num2=int(input("enter your num2 :"))
num3=int(input("enter your num3 :"))
num4=int(input("enter your num4 :"))
print(num1+num2+num3+num4)























