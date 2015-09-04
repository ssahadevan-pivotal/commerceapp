import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
payment = simplify.Payment.create({
        "amount" : "1000",
        "token" : "[TOKEN ID]",
        "description" : "payment description",
        "reference" : "7a6ef6be31",
        "currency" : "USD"
 
})
 
if payment.paymentStatus == 'APPROVED':
    print "Payment approved"
