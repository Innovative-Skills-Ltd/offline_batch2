

name = ""
phone = ""
#size_name = 
size_name = len(name)
size_phone = len(phone)
if(size_name==0 or size_phone ==0):
    print("required")
else:
    if(size_name<2):
        print("name length is invalid")
    elif(size_phone!=11):
        print("phone number is not invalid")
    else:
        gen_otp = "1234"
        print("send otp")
        sms_provider_status=500
        if(sms_provider_status!=200):
            print("Otp did not send")
        else:
            print("please match your otp")
            received_otp = '1234'
            if(gen_otp!=received_otp):
                print("otp does not match")
            else:
                print("registratrion success")