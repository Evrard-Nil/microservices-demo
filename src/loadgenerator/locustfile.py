#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from locust import HttpLocust, TaskSet

products = [
    '0PUK6V6EV0',
    '1YMWWN1N4O',
    '2ZYFJ3GM2N',
    '66VCHSJNUP',
    '6E92ZMYYFZ',
    '9SIQT8TOJO',
    'L9ECAV7KIM',
    'LS4PSXUNUM',
    'OLJCESPC7Z',
    '123456789A',
    '123456789B',
    '123456789C',
    '123456789D',
    '123456789E',
    '123456789F',
    '123456789G',
    '123456789H',
    '123456789I',
    '123456789J',
    '223456789A',
    '223456789B',
    '223456789C',
    '223456789D',
    '223456789E',
    '223456789F',
    '223456789G',
    '223456789H',
    '223456789I',
    '223456789J',
    '323456789A',
    '323456789B',
    '323456789C',
    '323456789D',
    '323456789E',
    '323456789F',
    '323456789G',
    '323456789H',
    '323456789I',
    '323456789J',
    '423456789A',
    '423456789B',
    '423456789C',
    '423456789D',
    '423456789E',
    '423456789F',
    '423456789G',
    '423456789H',
    '423456789I',
    '423456789J',
    '523456789A',
    '523456789B',
    '523456789C',
    '523456789D',
    '523456789E',
    '523456789F',
    '523456789G',
    '523456789H',
    '523456789I',
    '523456789J',
    '623456789A',
    '623456789B',
    '623456789C',
    '623456789D',
    '623456789E',
    '623456789F',
    '623456789G',
    '623456789H',
    '623456789I',
    '623456789J',
    '723456789A',
    '723456789B',
    '723456789C',
    '723456789D',
    '723456789E',
    '723456789F',
    '723456789G',
    '723456789H',
    '723456789I',
    '723456789J',
    '823456789A',
    '823456789B',
    '823456789C',
    '823456789D',
    '823456789E',
    '823456789F',
    '823456789G',
    '823456789H',
    '823456789I',
    '823456789J',
    '923456789A',
    '923456789B',
    '923456789C',
    '923456789D',
    '923456789E',
    '923456789F',
    '923456789G',
    '923456789H',
    '923456789I',
    '923456789J']

def index(l):
    l.client.get("/")

def setCurrency(l):
    currencies = ['EUR', 'USD', 'JPY', 'CAD']
    l.client.post("/setCurrency",
        {'currency_code': random.choice(currencies)})

def browseProduct(l):
    l.client.get("/product/" + random.choice(products))

def viewCart(l):
    l.client.get("/cart")

def addToCart(l):
    product = random.choice(products)
    l.client.get("/product/" + product)
    l.client.post("/cart", {
        'product_id': product,
        'quantity': random.choice([1,2,3,4,5,10])})

def checkout(l):
    addToCart(l)
    l.client.post("/cart/checkout", {
        'email': 'someone@example.com',
        'street_address': '1600 Amphitheatre Parkway',
        'zip_code': '94043',
        'city': 'Mountain View',
        'state': 'CA',
        'country': 'United States',
        'credit_card_number': '4432-8015-6152-0454',
        'credit_card_expiration_month': '1',
        'credit_card_expiration_year': '2039',
        'credit_card_cvv': '672',
    })

class UserBehavior(TaskSet):

    def on_start(self):
        index(self)

    tasks = {index: 1,
        setCurrency: 2,
        browseProduct: 10,
        addToCart: 2,
        viewCart: 3,
        checkout: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 10000
