# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import request as req
import base64


class MyModule(http.Controller):

    @http.route('/crud/create', auth='public', csrf=False)
    def crud_create(self, **kw):

        return req.render('sample_website.create', {
            'aaa': 'aaa',
        })

    @http.route('/crud/create/process', auth='public', csrf=False)
    def crud_create_process(self, **kw):

        product_values = {
            'name': kw.get('name'),
            'list_price': float(kw.get('list_price')),
        }

        image_1920 = kw.get('image_1920')
        product_values['image_1920'] = base64.b64encode(image_1920.read())

        product = req.env['product.template'].sudo().create(product_values)

        if product:
            print('product created')
        else:
            print('Product not created')

        return 'crud_create_process'

    @http.route('/crud/read_all', auth='public', csrf=False)
    def read_all(self, **kw):

        products = req.env['product.template'].sudo().search([])
        print('products:', products)

        return req.render('sample_website.read_all', {
            'products': products,
        })

    @http.route('/crud/read', auth='public', csrf=False)
    def read(self, **kw):

        product_id = kw.get('product_id')

        product = req.env['product.template'].sudo().search([('id', '=', product_id)])
        print('product:', product)

        return req.render('sample_website.read', {
            'product': product,
        })

    @http.route('/crud/update', auth='public', csrf=False)
    def update(self, **kw):

        product_id = kw.get('product_id')
        product = req.env['product.template'].sudo().search([('id', '=', product_id)])

        return req.render('sample_website.update', {
            'product': product,
        })

    @http.route('/crud/update/process', auth='public', csrf=False)
    def update_process(self, **kw):

        product_id = kw.get('product_id')
        product = req.env['product.template'].sudo().search([('id', '=', product_id)])

        name = kw.get('name')
        product.name = name

        return 'update_process'

    @http.route('/crud/delete', auth='public', csrf=False)
    def delete(self, **kw):

        product_id = kw.get('product_id')
        product = req.env['product.template'].sudo().search([('id', '=', product_id)])

        if product:
            product.unlink()

        return 'delete'

    @http.route('/page1', auth='public', csrf=False)
    def page1(self, **kw):

        return req.render('sample_website.page1', {
            'product': 'product',
        })

    @http.route('/page2', auth='public', csrf=False)
    def page2(self, **kw):

        return req.render('sample_website.page2', {
            'product': 'product',
        })
