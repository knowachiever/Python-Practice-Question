import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)

ob.starttls()
ob.login("knowachiever@gmail.com","Qwerty@999700")

subject= "This is auto-generate mail "
body = "Hey! How are you. I hope you are doing well.I send this mail via python so congrates me for this."
message = "Subject:{}\n\n{}".format(subject,body)

listOfAddress=["akashvachheta72260@gmail.com","kamal.saini@locanix.com"]
ob.sendmail("knowachiever",listOfAddress,message)
print("Send Successfully...")
ob.quit()