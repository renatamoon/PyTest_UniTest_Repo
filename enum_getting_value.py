from enum import Enum


class OrderTifs(Enum):
    GOOD_TILL_CANCEL = "GTC"
    DAY = "DAY"
    IMMEDIATE_OR_CANCEL = "IOC"
    FILL_OR_KILL = "FOK"
    GOOD_TILL_DATE = "GTD"
    AT_THE_CLOSE = "ATC"
    GOOD_FOR_AUCTION = "GFA"

    @classmethod
    def has_member_value(cls, value):
        return cls.__members__.get(value)



def get_tiff_response_acronimun(tif_value: str):
    tiff_response = OrderTifs.has_member_value(value=tif_value)
    try:
        if tiff_response is not None:
            return tiff_response.value
        return {}    
    except Exception as e:
        return e
    

new = get_tiff_response_acronimun("")
print(new)

