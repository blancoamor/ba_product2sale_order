# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from datetime import datetime , timedelta 
from dateutil import parser

from openerp import models, fields, api ,  SUPERUSER_ID
from openerp import tools


from openerp.tools.translate import _
import logging


_logger = logging.getLogger(__name__) 



class product_product(models.Model):

    _inherit = 'product.product'

    @api.multi
    def make_sale_order(self):
        order_lines=[]
        for product_id in self:
            order_lines.append((0,0,{'product_id':product_id.id}))
        _logger.info(order_lines)

        sale_order=self.env['sale.order'].create({'state':'draft','user_id':self._uid,'partner_id':8806,'order_line':order_lines})
        _logger.info(sale_order)
        view = { 
            'name':"Presupuesto",
            'view_mode': 'form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'sale.order',
            'res_id': sale_order.id,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'self',
            'domain': '[]',
        }
        return view
        

