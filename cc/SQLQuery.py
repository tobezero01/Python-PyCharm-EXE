BookGetAll = "Select MaSach,TenSach,TacGia from tSach"
BookGetById = 'select MaSach, TenSach, TacGia from tSach where MaSach = ?'

BookGetByNXB = 'select ct.MaSach,TenSach,nxb.TenNXB,ncc.TenNCC from tChiTietHDN \
    ct join tHoaDonNhap hd on hd.SoHDN=ct.SoHDN	join tSach s on s.MaSach=ct.MaSach \
    join tNhaXuatBan nxb on nxb.MaNXB=s.MaNXB \
    join tNhaCungCap ncc on ncc.MaNCC=hd.MaNCC where TenNXB = ? '
    
BookInsert = "Insert into tSach (MaSach, TenSach,TacGia,MaTheLoai,MaNXB,DonGiaNhap,DonGiaBan,SoLuong,SoTrang,TrongLuong) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
