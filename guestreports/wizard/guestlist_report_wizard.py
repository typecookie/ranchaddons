from odoo import api, exceptions, fields, models, _
from odoo.exceptions import ValidationError


class GuestListReportWizard(models.TransientModel):
    _name = "guestlist.report.wizard"

    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')

    def get_report(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date should be greater than start date')
        else:
            data = {
                'ids': self.ids,
                'model': self._name,
                'form': {
                    'start_date': self.start_date,
                    'end_date': self.end_date,
                }
            }

            return self.env.ref('guestreports.guestlist_report').report_action(self, data=data)


class ReportGuestListReport(models.AbstractModel):
    _name = 'report.guestreports.guestlist_report_document'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['start_date']
        date_end = data['form']['end_date']

        docs = []
        reservations = self.env['hotel.reservation'].search([('checkin', '>', date_start), ('checkout', '<', date_end)])
        for reservation in reservations:

            member_list = []
            for member in reservation.partner_id.child_ids:
                ## odoo takes care of joins/ foren keys
                member_list.append({
                    'name': member.name,
                    'height': member.Height,
                    'birthdate': member.birthdate_date,
                })

            room_list = reservation.reservation_line.mapped('reserve.name')  # ['a', 'b', 'c']
            rooms = ', '.join(map(str, room_list))  # a, b, c

            docs.append({
                'name': reservation.partner_id.name,
                'rooms': rooms,
                'member_list': member_list
            })

        return {
            'doc_ids': self.ids,
            'doc_model': data['model'],
            'docs': docs,
        }


