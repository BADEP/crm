# Copyright 2016 Tecnativa S.L. - Jairo Llopis
# Copyright 2016 Tecnativa S.L. - Vicent Cubells
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import typing

from odoo import models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit: typing.ClassVar[list[str]] = [_name, "utm.mixin"]
