odoo.define('pos_ticket_with_warehouse_returns.warehouse_returns', function (require){
"use strict"

    var models = require('point_of_sale.models');
    var core = require('web.core');
    var QWeb = core.qweb;
    var _t = core._t;

    models.load_models([
      {
        model:  'stock.warehouse.return',
        fields: ['name'],
        loaded: function(self,warehouse_returns){
          self.warehouse_returns = warehouse_returns;
        },
      },
    ], {'after': 'product.product'});


  });
