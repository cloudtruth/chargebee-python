from chargebee.model import Model
from chargebee import request


class Card(Model):

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/cards/%s' % id, {}, env)

    @staticmethod
    def update_card_for_customer(id, params, env=None):
        return request.send('post', '/customers/%s/credit_card' % id, params, env)
