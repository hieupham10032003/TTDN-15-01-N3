from odoo import models, fields, api


class MuonTra(models.Model):
    _name = 'muon_tra'
    _description = "Quản lý mượn trả tài sane"
    _rec_name = 'ma_tai_san'

    ma_tai_san = fields.Many2one('tai_san', string="Tài sản", required=True)
    so_luong_muon = fields.Integer('Số lượng mượn')
    ngay_muon = fields.Date("Ngày muợn")
    ngay_tra = fields.Date("Ngày trả")
    trang_thai = fields.Selection([
        ('da_qua_su_dung', 'Đã qua sử dụng'),
        ('con_moi', 'Còn mới'),
    ], string="Trạng thái", default='da_qua_su_dung')
    tinh_trang_muon = fields.Selection([
        ('tra_muon','Trả muộn'),
        ('tra_som','Trả sớm'),
        ('dung_han','Đúng hạn'),  
        ('dang_muon','Đang mượn')
    ])
    nhan_vien_id = fields.Many2one("nhan_vien", string="Người mượn")
    nguoi_tra = fields.Char("Người trả")
    nguoi_kiem_duyet = fields.Char("Người kiểm duyệt")
    nguoi_xac_nhan = fields.Many2one("nhan_vien", string="Người xác nhận")
    