from payment_service import PaymentService
from nameko.events import event_handler

class Mailer(object):

    name = "mailer"

    @event_handler('payments', 'payment_received')
    def send(self, payload):
        print(
            f"""
            Dear {payload['payee']['name']},

            You have received a payment of {payload['payment']['amount']} {payload['payment']['currency']} from {payload['client']['name']} ({payload['client']['email']}).

            Yours,

            student.com
            """
        )
