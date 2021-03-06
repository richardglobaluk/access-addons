from openerp import models, api, exceptions, SUPERUSER_ID


class ResUsers(models.Model):
    _inherit = 'res.users'

    def fields_get(self, cr, uid, allfields=None, context=None, write_access=True, attributes=None):
        # switch to superuser to get access to virtual fields
        return super(ResUsers, self).fields_get(cr, SUPERUSER_ID, allfields=allfields, context=context, write_access=write_access, attributes=attributes)
