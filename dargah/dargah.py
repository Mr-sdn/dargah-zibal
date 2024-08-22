import requests
import json

class Zibal:
    """
        A class to communicate with the zibal portal and perform various operations such as payment and transaction enquiry etc...
    
    Methods
    -------    
    """


    def __init__(self, merchant: str = "zibal") -> None:
        
        """
        Initialize and communication with your portal by merchant.
            - you can get merchant from https://zibal.ir
            - To get the merchant, you have to get the zibal port.

        Args:
            merchant: - The merchant id required to communicate with your portal by default you can use the merchant of the zibal website
        
        Returns:
            output: - An object is returned from the zibal class and is reserved for your portal by merchant and you can use this object to create a new payment etc...
        """

        self.merchant = merchant
        if not isinstance(merchant, str):
            raise TypeError(f"Expected 'merchant' to be of type str, but got {type(merchant).__name__}")



    def create_payment(self, amount: float | int, callbackUrl: str, description: str = "", orderId: str = "", mobile: str = "", allowedCards: list[str] = [], ledgerId: str = "", nationalCode: str = "") -> int:
        
        """
        Create a new Payment Order note the following arguments are necessary
            - amount, callbackUrl

        Args:
            amount: - Total order amount (in rials)              
            callbackUrl: - The address of the recipient's site to which zibal will send the payment information Information such as payment status such as successful payment etc...
            description: - Description of the order (optional-will be shown in various reports)
            orderId: - Your unique Order ID (optional-used in reports)
            mobile: - By sending their users mobile numbers, the registered card numbers of customers appear at the payment gateway for selection (optional)
            allowedCards: - If you want the user to be able to pay only from a specific card number, send a 16-digit card lists (optional) 
            ledgerId: - Ledger ID related to this transaction-as the transaction is successful, the transaction amount will be added to the inventory of this ledger (optional)
            nationalCode: - The national code is optional and 10-digit. If this field is sent, the cardholder's nationalCode will be matched to the nationalCode entered, and if it does not match, the transaction will be prevented.
        Returns:
            output: - An integer that represents the trackid of each payment and the user can use it to track the payment    
            example:
            portal = Zibal("zibal")
            portal.create_payment(450000, "https://your-url")
            >>> 3726123664    
        Raises:
            ValueError: Raises an error due to invalid entering merchant or amount or callbackUrl etc...

        """

        if not isinstance(amount, (float, int)):
            raise TypeError(f"Expected 'amount' to be of type float | int, but got {type(amount).__name__}")
        
        if not isinstance(callbackUrl, str):
            raise TypeError(f"Expected 'callbackUrl' to be of type str, but got {type(callbackUrl).__name__}")
        
        if not isinstance(description, str):
            raise TypeError(f"Expected 'description' to be of type str, but got {type(description).__name__}")
        
        if not isinstance(orderId, str):
            raise TypeError(f"Expected 'orderId' to be of type str, but got {type(orderId).__name__}")
        
        if not isinstance(mobile, str):
            raise TypeError(f"Expected 'mobile' to be of type str, but got {type(mobile).__name__}")

        if not isinstance(allowedCards, list):
            raise TypeError(f"Expected 'allowedCards' to be of type list[str], but got {type(allowedCards).__name__}")
        
        if not isinstance(ledgerId, str):
            raise TypeError(f"Expected 'ledgerId' to be of type str, but got {type(ledgerId).__name__}")
        
        if not isinstance(nationalCode, str):
            raise TypeError(f"Expected 'nationalCode' to be of type str, but got {type(nationalCode).__name__}")
        
        url = "https://gateway.zibal.ir/v1/request"
        body = {
            "merchant": self.merchant,
            "amount": amount,
            "callbackUrl": callbackUrl,
            "description": description,
            "orderId": orderId,
            "mobile": mobile,
            "allowedCards": allowedCards,
            "ledgerId": ledgerId,
            "nationalCode": nationalCode
        }

        response = requests.post(url=url, json=body)
        info = Zibal.__json_to_dict(response)
        result = info["result"]

        if result == 100:
            return info["trackId"]
        
        elif result == 102:
            raise ValueError("merchant not found !")
        
        elif result == 103:
            raise ValueError("merchant is inactive !")
        
        elif result == 104:
            raise ValueError("merchant is invalid !")
        
        elif result == 105:
            raise ValueError("the amount should be greater than 1,000 rials !")
        
        elif result == 106:
            raise ValueError("callbackurl is invalid (Starting with http or https) !")
        
        elif result == 113:
            raise ValueError("the transaction amount exceeds the transaction rate ceiling !")
        
        elif result == 114:
            raise ValueError("The national code is invalid !")
        

    def __json_to_dict(response: requests.Response) -> dict:
        info = json.loads(response.text)
        return info


portal = Zibal("zibal")
payment1 = portal.create_payment(450000, 'hts://help.zibal.ir/IPG/API/')
print(payment1)