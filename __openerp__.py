# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Manuel Márquez <manuel@humanytek.com>
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
###############################################################################

{
    'name': "Add list of posible causes of returns to POS ticket",
    'description': """
    Extends the ticket of POS to add a list of posible causes of return of
    a delivery.
    """,
    'author': "Humanytek",
    'website': "http://www.humanytek.com",
    'category': 'Point Of Sale',
    'version': '0.1.0',
    'depends': ['point_of_sale', 'stock_warehouse_returns'],
    'data': [
        'views/templates.xml',
    ],
    'demo': [
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ]
}
