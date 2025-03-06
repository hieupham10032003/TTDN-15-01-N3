from odoo import models, fields, api


class ThongKeTaiSan(models.Model):
    _name = 'thong_ke_tai_san'
    _description = "Thống kê tài sản"
    so_luong_tai_san = fields.Integer("Số lượng tài sản", required=True)
    so_luong_muon = fields.Integer("Số lượng mượn")
    so_luong_thuc_te = fields.Integer("Số lượng thực tế", compute='_compute_so_luong_thuc_te', store=True)

    @api.depends('so_luong_tai_san', 'so_luong_muon')
    def _compute_so_luong_thuc_te(self):
        for record in self:
            record.so_luong_thuc_te = record.so_luong_tai_san - record.so_luong_muon