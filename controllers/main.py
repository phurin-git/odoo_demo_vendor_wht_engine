from odoo import http
from odoo.http import request
import json


class VendorBillAPI(http.Controller):

    @http.route('/api/vendor_bill', type='http', auth='user', methods=['POST'], csrf=False)
    def create_vendor_bill(self, **kwargs):

        data = json.loads(request.httprequest.data)

        vendor_name = data.get("vendor")
        amount = data.get("amount")

        if not vendor_name or not amount:
            return request.make_json_response({"error": "Missing vendor or amount"})

        partner = request.env['res.partner'].sudo().search(
            [('name', '=', vendor_name)], limit=1
        )

        if not partner:
            partner = request.env['res.partner'].sudo().create({
                'name': vendor_name,
                'supplier_rank': 1,
            })

        move = request.env['account.move'].sudo().create({
            'move_type': 'in_invoice',
            'partner_id': partner.id,
            'invoice_line_ids': [(0, 0, {
                'name': 'Service Fee',
                'quantity': 1,
                'price_unit': amount,
            })]
        })

        return request.make_json_response({
            "id": move.id,
            "wht_amount": move.x_wht_amount,
        })
