from lxml import etree

# ====== Đọc file XML ======
tree = etree.parse("quanlybanan.xml")
root = tree.getroot()

# ====== Danh sách truy vấn XPath ======
queries = {
    "1. Lấy tất cả bàn": "/QUANLY/BANS/BAN/TENBAN/text()",
    "2. Lấy tất cả nhân viên": "/QUANLY/NHANVIENS/NHANVIEN/TENV/text()",
    "3. Lấy tất cả tên món": "/QUANLY/MONS/MON/TENMON/text()",
    "4. Lấy tên nhân viên có mã NV02": "/QUANLY/NHANVIENS/NHANVIEN[MANV='NV02']/TENV/text()",
    "5. Lấy tên và số điện thoại của nhân viên NV03": "/QUANLY/NHANVIENS/NHANVIEN[MANV='NV03']/(TENV|SDT)/text()",
    "6. Lấy tên món có giá > 50,000": "/QUANLY/MONS/MON[GIA > 50000]/TENMON/text()",
    "7. Lấy số bàn của hóa đơn HD03": "/QUANLY/HOADONS/HOADON[SOHD='HD03']/SOBAN/text()",
    "8. Lấy tên món có mã M02": "/QUANLY/MONS/MON[MAMON='M02']/TENMON/text()",
    "9. Lấy ngày lập của hóa đơn HD03": "/QUANLY/HOADONS/HOADON[SOHD='HD03']/NGAYLAP/text()",
    "10. Lấy tất cả mã món trong hóa đơn HD01": "/QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON/text()",
    "11. Lấy tên món trong hóa đơn HD01": "/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOHD='HD01']/CTHDS/CTHD/MAMON]/TENMON/text()",
    "12. Lấy tên nhân viên lập hóa đơn HD02": "/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOHD='HD02']/MANV]/TENV/text()",
    "13. Đếm số bàn": "count(/QUANLY/BANS/BAN)",
    "14. Đếm số hóa đơn lập bởi NV01": "count(/QUANLY/HOADONS/HOADON[MANV='NV01'])",
    "15. Lấy tên tất cả món có trong hóa đơn của bàn số 2": "/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON[SOBAN='2']/CTHDS/CTHD/MAMON]/TENMON/text()",
    "16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3": "/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='3']/MANV]/TENV/text()",
    "17. Lấy tất cả hóa đơn mà nhân viên nữ lập": "/QUANLY/HOADONS/HOADON[MANV = /QUANLY/NHANVIENS/NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()",
    "18. Lấy tất cả nhân viên từng phục vụ bàn số 1":"/QUANLY/NHANVIENS/NHANVIEN[MANV = /QUANLY/HOADONS/HOADON[SOBAN='1']/MANV]/TENV/text()",
    "19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn":"/QUANLY/MONS/MON[MAMON = /QUANLY/HOADONS/HOADON/CTHDS/CTHD/MAMON[count(. | key('mon', .)[1]) = 1][count(/QUANLY/HOADONS/HOADON/CTHDS/CTHD/MAMON[. = current()]) > 1]]/TENMON/text()",
    "20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'":"concat(/QUANLY/BANS/BAN[SOBAN = /QUANLY/HOADONS/HOADON[SOHD='HD02']/SOBAN]/TENBAN/text(), ' - ', /QUANLY/HOADONS/HOADON[SOHD='HD02']/NGAYLAP/text())"
}

# ====== In kết quả ======
print("\n===== KẾT QUẢ TRUY VẤN XPATH =====\n")

for title, xpath_expr in queries.items():
    print(f"{title}:")
    print("-" * 60)
    try:
        result = root.xpath(xpath_expr)
        if isinstance(result, (int, float)):  # Kết quả đếm
            print(f"Kết quả: {int(result)}")
        elif isinstance(result, list):
            if not result:
                print("(Không có kết quả)")
            else:
                for val in result:
                    if isinstance(val, str):
                        print(val.strip())
                    else:
                        print(etree.tostring(val, pretty_print=True).decode())
        else:
            print(result)
    except Exception as e:
        print(f"Lỗi truy vấn: {e}")
    print()

print("===== KẾT THÚC =====")
