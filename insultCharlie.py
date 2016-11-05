import random, time, smtplib

adjectives = ["fat", "stupid", "annoying", "cantankerous", "naughty", "narrow-minded", "parsimonious"]
nouns = ["nonentity", "rat", "pig", "louis", "elephant", "7 year old", "minecraft player"]
while True:
    insult = adjectives[random.randint(0, 6)] + " " + nouns[random.randint(0, 6)]
    print("Louis is a " + insult)
    time.sleep(1)
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    emailsss = "mattnappo@gmail.com"
    mail.login(emailsss, "password")
    subject = "charlie"
    content = insult
    stuff = "Subject: "+subject+"\n"+content
    mail.sendmail(emailsss,"target@gmail.com",stuff)
    mail.close()