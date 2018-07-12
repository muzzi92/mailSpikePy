from payment_service import PaymentService
from nameko.events import event_handler
import requests

class Mailer(object):

    name = "mailer"

    @event_handler('payments', 'payment_received')
    def send(self, payload):
        key = 'b53481c39be1a2129486cde3809b6526-8b7bf2f1-7333ddf6'
        sandbox = 'sandboxfec723b9368e438888acd3dde7fcee3e.mailgun.org'
        recipient = 'amiraldean@gmail.com'
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
        requests.post(request_url, auth=('api', key), data={
            'from': 'amiraldean@hotmail.com',
            'to': recipient,
            'subject': 'Hello',
            'text': f"""
            Dear {payload['payee']['name']},

            You have received a payment of {payload['payment']['amount']} {payload['payment']['currency']} from {payload['client']['name']} ({payload['client']['email']}).

            Yours,

            student.com
            """
        })
        print('Email Sent.')
