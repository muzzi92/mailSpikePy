from payment_service import PaymentService
from nameko.events import event_handler

class Mailer(object):

    name = "mailer"

    @event_handler('payments', 'payment_received')
    def send(self, payload):
        print('Payment recieved', payload)
