# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class FolioReportWizard(models.TransientModel):
    _name = "folio.report.wizards"
    _rec_name = "date_start"
    _description = "Allow print folio report by date"

    date_start = fields.Datetime("Start Date")
    date_end = fields.Datetime("End Date")

    def print_report(self):
        data = {
            "ids": self.ids,
            "model": "hotel.folio",
            "form": self.read(["date_start", "date_end"])[0],
        }
        return self.env.ref("hotel.report_hotel_management").report_action(
            self, data=data
        )
