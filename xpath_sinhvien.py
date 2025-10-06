from lxml import etree

# ====== Đọc file XML ======
tree = etree.parse("sv.xml")
root = tree.getroot()

# ====== Danh sách các truy vấn XPath ======
queries = {
    "1. Lấy tất cả sinh viên": "/school/student",
    "2. Liệt kê tên tất cả sinh viên": "/school/student/name/text()",
    "3. Lấy tất cả id của sinh viên": "/school/student/id/text()",
    "4. Lấy ngày sinh của sinh viên có id = 'SV01'": "/school/student[id='SV01']/date/text()",
    "5. Lấy các khóa học": "/school/enrollment/course/text()",
    "6. Lấy toàn bộ thông tin của sinh viên đầu tiên": "/school/student[1]/*",
    "7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'": "/school/enrollment[course='Vatly203']/studentRef/text()",
    "8. Lấy tên sinh viên học môn 'Toan101'": "/school/student[id=/school/enrollment[course='Toan101']/studentRef]/name/text()",
    "9. Lấy tên sinh viên học môn 'Vatly203'": "/school/student[id=/school/enrollment[course='Vatly203']/studentRef]/name/text()",
    "10. Lấy ngày sinh của sinh viên có id='SV01'": "/school/student[id='SV01']/date/text()",
    "11. Lấy tên và ngày sinh của sinh viên sinh năm 1997": "/school/student[starts-with(date,'1997')]/name/text() | /school/student[starts-with(date,'1997')]/date/text()",
    "12. Lấy tên sinh viên có ngày sinh trước năm 1998": "/school/student[number(substring(date,1,4)) < 1998]/name/text()",
    "13. Đếm tổng số sinh viên": "count(/school/student)",
    "14. Lấy tất cả sinh viên chưa đăng ký môn nào": "/school/student[not(id = /school/enrollment/studentRef)]/name/text()",
    "15. Lấy phần tử <date> anh em ngay sau <name> của SV01": "/school/student[id='SV01']/name/following-sibling::date",
    "16. Lấy phần tử <id> anh em ngay trước <name> của SV02": "/school/student[id='SV02']/name/preceding-sibling::id",
    "17. Lấy toàn bộ node <course> trong enrollment có studentRef='SV03'": "/school/enrollment[studentRef='SV03']/course",
    "18. Lấy sinh viên có họ là 'Trần'": "/school/student[starts-with(name,'Trần')]/name/text()",
    "19. Lấy năm sinh của sinh viên SV01": "substring(/school/student[id='SV01']/date,1,4)"
}

# ====== Thực thi và in kết quả ======
print("\n===== KẾT QUẢ TRUY VẤN XPATH =====\n")

for title, xpath_expr in queries.items():
    print(f"{title}:")
    print("-" * 60)
    try:
        result = root.xpath(xpath_expr)

        # Nếu là kết quả đếm
        if isinstance(result, (int, float)):
            print(f"Kết quả: {int(result)}")

        # Nếu là node XML
        elif all(isinstance(node, etree._Element) for node in result):
            for node in result:
                if node.tag == "student":
                    id_ = node.findtext("id", default="(Không có id)")
                    name = node.findtext("name", default="(Không có tên)")
                    date = node.findtext("date", default="(Không có ngày sinh)")
                    print(f"- {id_}: {name} ({date})")
                else:
                    text = node.text.strip() if node.text else ""
                    print(f"<{node.tag}> {text}")

        # Nếu là chuỗi (text)
        elif isinstance(result, list):
            if not result:
                print("(Không có kết quả)")
            else:
                for val in result:
                    print(val.strip() if isinstance(val, str) else val)

        else:
            print(result)

    except Exception as e:
        print(f"Lỗi truy vấn: {e}")
    print()

print("===== KẾT THÚC =====")
