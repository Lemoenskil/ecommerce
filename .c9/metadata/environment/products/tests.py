{"filter":false,"title":"tests.py","tooltip":"/products/tests.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":19},"end":{"row":13,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"mode":"ace/mode/python"}},"hash":"6d14ccf6d0b70d9954fd0861371ead98ddb7204c","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.test import TestCase","","# Create your tests here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["v"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["v"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":13,"column":19},"action":"insert","lines":["from django.test import TestCase","from .models import Product","","# Create your tests here.","class ProductTests(TestCase):","    \"\"\"","    Here we'll define the tests that we'll run against our","    Product model","    \"\"\"","","    def test_str(self):","        test_name = Product(name='A product')","        self.assertEqual(str(test_name), 'A product')","© 2020 GitHub, Inc."],"id":4}]]},"timestamp":1586709770378}