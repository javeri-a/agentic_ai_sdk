def summraise_text(text):
    return f"Ye hai chhota version: {text[:20]}"
    
result = summraise_text("Ye ek lme hon jo bohut achi hon or me piyari bhi hon")
print(result)


def  summraise_text(text):
    return f"this is a short version: {text[:39]}"
result = summraise_text("This is a long text that needs to be summarized into a shorter version for better understanding.")
print(result)




def sumText(text):
    return f"Short version of your text: {text[:40]}"

text = input("enter your text here: ")
result = sumText(text)
print(result)


