import phonenumbers
from num import number

#for tracking the location of number
from phonenumbers import geocoder

ch_number= phonenumbers.parse(number,"CH")      #CH-Country History
print(geocoder.description_for_number(ch_number,"en"))    #en-English


#Service Provider of the number
from phonenumbers import carrier

service_number= phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))