import random
start_number_value=int(input("BAŞLANGIÇ DEĞERİ : "))
stop_number_value=int(input("BİTİŞ DEĞERİ : "))
rnd_number=random.randint(start_number_value,stop_number_value)
print(rnd_number)
user_right=int(input("HAKKINIZ : "))
result=0
while user_right>0:
    user_right=user_right-1
    user_number=int(input("TAHMİN : "))
    result=rnd_number-user_number
    if result==0:
        print("tebrikler sayıyı doğru tahmin ettiniz.")
        break
    elif user_right==0:
        print("oyunu kaybettiniz hakkınız bitti.")
        break
print(user_number)




