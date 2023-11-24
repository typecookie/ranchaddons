from odoo import api, exceptions, fields, models, _
from odoo.exceptions import ValidationError


class GuestListDisplayReportWizard(models.TransientModel):
    _name = "guestlist.display.report.wizards"

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

            return self.env.ref('guestreports.guestlist_display_report').report_action(self, data=data)


class ReportGuestListReport(models.AbstractModel):
    _name = 'report.guestreports.guestlist_display_report_document'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['start_date']
        date_end = data['form']['end_date']

        docs = []
        reservations = self.env['hotel.reservation'].search([('checkin', '>', date_start), ('checkout', '<', date_end)])
        for reservation in reservations:

            member_list = []
            for member in reservation.partner_id.child_ids:
                # odoo takes care of joins/ foren keys
                member_list.append({
                    'name': member.name,
                    'height': member.Height,
                    'weight': member.Weight,
                    'sex': member.Sex,
                    'age': member.age,
                    'health-conditions': member.health_conditions,
                    'experience': member.Exp,
                    'food_allergies': member.food_allergies,
                    'dietary_needs': member.dietary_needs,
                    'health_conditions': member.health_conditions,
                    'health_requests': member.health_requests,
                    'horse_request': member.horse_request,
                    'horse_assigned': member.horse_assigned,
                    'saddle_request': member.saddle_request,
                    'saddle_assigned': member.saddle_assigned,
                })

            room_list = reservation.reservation_line.mapped('reserve.name')  # ['a', 'b', 'c']
            rooms = ', '.join(map(str, room_list))  # a, b, c


            docs.append({
                'name': reservation.partner_id.name,
                'rooms': rooms,
                'member_list': member_list,
                'cabin_owner': reservation.partner_id.cabin_owner,
                'number_of_years_return': int(reservation.partner_id.number_of_years_return),
                'cabin_preference': reservation.partner_id.cabin_preference,
                'deposit_request_sent': reservation.partner_id.deposit_request_sent,
                'deposit_request_received': reservation.partner_id.deposit_request_received,
                'deposit_request_received_date': reservation.partner_id.deposit_request_received_date,
                'city': reservation.partner_id.city,
                'state': reservation.partner_id.state_id.name,
                'anniversaries': reservation.partner_id.anniversaries,
                'birthdays': reservation.partner_id.birthdays,
                'partner': reservation.partner_id,
            })

        return {
            'doc_ids': self.ids,
            'doc_model': data['model'],
            'docs': docs,
        }


