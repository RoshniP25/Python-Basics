print("==== OTP VERIFICATION ====")

correctOtp = "5678"
attempt = ""

#keep asking until matching otp
while attempt != correctOtp:
    attempt = input("Enter OTP: ")

print("OTP verified successful.")