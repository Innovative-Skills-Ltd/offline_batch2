
#abc = abstraction base class->helper class->class/method k abstract korte help kore

from abc import ABC, abstractmethod
class notification(ABC):
    @abstractmethod
    def send_message(self):
        pass
class email(notification):
    def send_message(self,email,tls):
        print("this is email notification",email,tls)
class whatsapp(notification):
    def send_message(self,number, api):
        print("this is whatsapp notification",number,api)

email = email()
email.send_message(1,2)

whatsapp = whatsapp()
whatsapp.send_message(4,5)