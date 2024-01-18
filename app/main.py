from fastapi import FastAPI, HTTPException

app = FastAPI()

visa_data = {
    "X1234": {
        "registerNumber": "2211023Z227227",
        "namaLengkap": "SASA SARAH",
        "visaNo": "23211A000700",
        "Status": "Visa has been issued"
    },
    "X6789": {
        "Status": "Data not found"
    },
    "X": {
        "status": "Invalid Parameter"
    }
}

@app.get("/get_visa_tracking/{passport_number}")
async def get_visa_tracking(passport_number: str):
    if passport_number in visa_data:
        return visa_data[passport_number]
    else:
        raise HTTPException(status_code=404, detail="Data not found")
    
#------ get status -------#
    
status_problem = {
    "payment error": {
        "message": "Please make sure to check the card's expiration date and CCV before paying. The credit card should allow international transactions with sufficient amounts. Credit cards can be used max. up 30 transactions in one month. Too many attempts to pay may cause the payment declined due to fraud prevention rules.",
        "error_type": "Payment Declined",
        "error_message": "Too many attempts to pay. Possible fraud prevention triggered.",
        "recommended_action": "Check card's expiration date and CCV, Ensure the credit card allows international transactions, exceeded the maximum transaction limit (30 transactions per month)"
    },
    "payment data submission error": {
        "message": "Please kindly check if your data is already correct and click save/submit.The documents should be colour scan picture with size min.100 KB and max. 200 KB in format JPG/JPEG. If your application is still in draft, you cannot proceed to payment.",
        "error_type": "Application Submission Error",
        "error_message": "Unable to proceed with payment. Application in draft mode.",
        "recommended_action": "Confirm if the application is indeed in draft mode, incomplete information, clear the browsr chache"
    },
    "evoa incorrect data input": {
        "message": "If you entered the wrong data, please kindly submit a new application, or you can get a visa on arrival at the airport. All information on any processed e-VOA cannot be changed and the fee paid for an e-VOA is not refundable.Before proceeding with payment, please kindly check if all your personal details match with your passport.",
        "error_type": "Apcplication Error",
        "error_message": "Incorrect data entered. Unable to proceed with current application.",
        "recommended_action": "Confirm the specific details that were entered incorrectly, once an e-VOA is processed, information cannot be altered."
    },
    "evoa extension error": {
        "message": "Holders of e-VOA are granted permission to stay in Indonesia for 30 (thirty) days, and the stay permit is extendable for another 30 days. You can extend the e-VOA after you arrive in Indonesia. Please scan the QR Code at the bottom center of your e-VOA and follow the instructions on the link. If your e-VOA doesn't have the QR Code, please kindly redownload your e-VOA on https://evisa.imigrasi.go.id/",
        "error_type": "e-VOA Extension Error",
        "error_message": "Unable to extend e-VOA. No QR Code detected.",
        "recommended_action": "Confirm if the e-VOA contains a QR Code or not, If no QR Code is found, advise the user to redownload their e-VOA from the official website."
    },
    "molina photo upload error": {
        "message": "Please kindly try again to upload your colour scan picture with size min.100 KB and max. 200 KB in format JPG/JPEG.You can also get a visa on arrival at the airport. Please click the link below for visa on arrival at the airport : https://www.imigrasi.go.id/en/visa-kunjungan-saat-kedatangan/",
        "error_type": "Document Upload Error",
        "error_message": "Uploaded document does not meet size requirements.",
        "recommended_action": "Confirm if the uploaded document meets the specified size requirements, If the document size is not within the required range, advise the user to re-upload the document, properly resize and upload their document."
    },
    "molina country selection error": {
        "message": "If you cannot select your country, please kindly try to edit your passport information by click My Account > Edit Passport Information > log out > log in > Apply. You can also get visa on arrival at the airport. Please click the link below for visa on arrival at the airport : https://www.imigrasi.go.id/en/visa-kunjungan-saat-kedatangan/",
        "error_type": "Passport Information Editing Error",
        "error_message": "Unable to edit passport information for country selection.",
        "recommended_action": "Confirm if there was an issue with editing passport information for country selection., Inform the user about the option of obtaining a visa on arrival at the airport., Check for any technical glitches in the passport information editing process."
    }
} 

@app.get("/get_status/{status}")
async def get_status(status: str):
    if status in status_problem:
        return status_problem[status]
    else:
        raise HTTPException(status_code=404, detail="will contact you to our customer services")
