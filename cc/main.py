import pyodbc
import flask
from Config import *
from SQLQuery import *

#Ket noi
try:
    conn = pyodbc.connect(conn_str)
    print("Thanh cong")
    #methods: GET: select, POST: insert, PUT: update
    app = flask.Flask(__name__)
    # API getallbook
    @app.route('/book/getall', methods = ['GET'])
    def getAllBook():
        cursor = conn.cursor()
        sql =  BookGetAll
        cursor.execute(sql) #thực thi
        results = [] #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results.append(dict(zip(keys,i)))        
        resp = flask.jsonify(results)
        resp.status_code=200
        return resp
    
    #get by id
    @app.route('/book/getbyid/<id>',methods=['GET'])
    def getBookById(id=1):
        cursor = conn.cursor()
        sql = BookGetById
        data = (id)
        cursor.execute(sql,data)
        result = {}
        keys = []
        for i in cursor.description:
            keys.append(i[0])
        for i in cursor.fetchall():
            result = dict(zip(keys,i))
        res = flask.jsonify(result)
        res.status_code = 200
        return res
    
    #thêm mới một nhà cung cấp
    @app.route('/ncc/insert',methods=['POST'])
    def insertNCC():
        try:
            ma = flask.request.json.get("MaNCC")
            ten = flask.request.json.get("TenNCC")
            cursor = conn.cursor()
            sql = "Insert into tNhaCungCap (MaNCC, TenNCC) values (?, ?)"
            data = (ma,ten)
            cursor.execute(sql,data)
            cursor.commit()
            res = flask.jsonify({"mess":"Thanh cong"})
            res.status_code = 200
            return res
        except Exception as e:
            res = flask.jsonify({"mess":e})
            res.status_code = 200
            return res
    @app.route('/book/getbynxb/<nxb>',methods=['GET'])
    def getBookByNXB(nxb=''):    
        cursor = conn.cursor()
        sql = BookGetByNXB
        data = nxb
        cursor.execute(sql,data)    
        result = []
        keys = []
        for i in cursor.description:
            keys.append(i[0])
        for i in cursor.fetchall():
            result.append(dict(zip(keys,i)))
        res = flask.jsonify(result)
        res.status_code = 200
        return res        
    
    #thêm mới một cuốn sách
    @app.route('/book/insert',methods=['POST'])
    def insertBook():
        try:
            ma = flask.request.json.get("MaSach")
            ten = flask.request.json.get("TenSach")
            tacGia = flask.request.json.get("TacGia")
            maTL = flask.request.json.get("MaTheLoai")
            maNXB = flask.request.json.get("MaNXB")
            DonGiaNhap = flask.request.json.get("DonGiaNhap")
            DonGiaBan = flask.request.json.get("DonGiaBan")
            SoLuong = flask.request.json.get("SoLuong")
            SoTrang = flask.request.json.get("SoTrang")
            TrongLuong = flask.request.json.get("TrongLuong")
            cursor = conn.cursor()
            sql = BookInsert
            data = (ma,ten,tacGia,maTL,maNXB,DonGiaNhap,DonGiaBan,SoLuong,SoTrang,TrongLuong)
            cursor.execute(sql,data)
            cursor.commit()
            res = flask.jsonify({"mess":"Thanh cong"})
            res.status_code = 200
            return res
        except Exception as e:
            res = flask.jsonify({"mess":e})
            res.status_code = 404
            return res
            
    if __name__ == "__main__":
        app.run(host= "192.168.12.101",port=88)
except Exception as e:
    print(e)