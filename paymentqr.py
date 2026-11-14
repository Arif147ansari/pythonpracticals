import qrcode
import urllib.parse

upi_id=input("Enter your UPI ID: ")
recipient_name = urllib.parse.quote("Recipient Name")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRRENCY&tn=MESSAGE
#DEFining the payment url based on the upi id and [ayment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn={recipient_name}&cu=INR'

#Create qr code for each payment apps
phonepe_qr=qrcode.make(phonepe_url)

#save the qr code to image file 
phonepe_qr.save('phonepe_qr.png')

#Display the qr code 
phonepe_qr.show()
# paytm_qr.show()
# gpay_qr.show()






