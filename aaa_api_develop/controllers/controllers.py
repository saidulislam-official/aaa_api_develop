#-*- coding: utf-8 -*-
from odoo import http

#for ubuntu
# import logging
# _logger = logging.getLogger(__name__)

class AaaApiDevelop(http.Controller):
    @http.route('/aaa/api/develop', auth='public', website=False, csrf=False, type='http', methods=['GET','POST'])
    def index(self, **kw):
        #for ubuntu
        # _logger.info(kw)

        sum = int(kw['a'])+int(kw['b'])
        sub = int(kw['a'])-int(kw['b'])
        mul = int(kw['a'])*int(kw['b'])
        div = int(kw['a'])/int(kw['b'])

        # result = ("sum", sum, "sub", sub, "mul", mul, "div", div)
        # return str(result)

        return f"Sum is = {sum}\nSub is = {sub}\nMul is = {mul}\nDiv is = {div}"








