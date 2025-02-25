from odoo import models, fields, api


class TaiSan(models.Model):
    _name = 'tai_san'
    _description = "Danh mục tài sản"
    _rec_name = 'ten_tai_san'

    ma_tai_san = fields.Char("Mã tài sản", required=True)
    ten_tai_san = fields.Char("Tên tài sản", required=True)
    loai_tai_san = fields.Selection([
        ('vat_tu', 'Vật tư'),
        ('thiet_bi', 'Thiết bị'),
        ('phuong_tien', 'Phương tiện'),
    ], string="Loại tài sản", required=True)
    gia_tri = fields.Float("Giá trị")
    ngay_mua = fields.Date("Ngày mua")
    tinh_trang = fields.Selection([
        ('moi', 'Mới'),
        ('da_su_dung', 'Đã sử dụng'),
        ('hong', 'Hỏng'),
    ], string="Tình trạng")
    vi_tri = fields.Char("Vị trí")