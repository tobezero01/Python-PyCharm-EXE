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
    
    # xây dựng API đưa ra các cuốn sách của nhà xuất bản X
    @app.route('/book/getby/nxb', methods=['GET'])                 
    def getByNXB():
        cursor = conn.cursor()
        tenNXB = flask.request.json.get('tennxb')
        sql =  "exec proc_get_book_by_nxb @ten = ?"
        cursor.execute(sql,tenNXB) #thực thi
        results = [] #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results.append(dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
        return res
    
    #Xây dựng và kiểm thử các API sau:
    # - Tìm kiếm sách theo tác giả
    # - Tìm kiếm sách theo khoảng giá tiền
    # - Tính tổng số tiền bán được theo tháng và năm
    # - Đếm số lượt khách hàng mua sách x trong khoảng thời gian
    # - Tìm x khách hàng mua nhiều sách nhất
    # - Hiển thị đơn giá bán được giảm 10% đối với sách của nhà xuất bản x
    # - insert 1 nhà cung cấp
                     
    #Tìm kiếm sách theo tác giả             
    @app.route('/book/searchbyauthor')            
    def SearchByAuthor():
        cursor = conn.cursor()
        tacGia = flask.request.json.get('tacgia')
        sql =  "select * from tSach	where TacGia like '%' + ? + '%'"
        cursor.execute(sql,tacGia) #thực thi
        results = [] #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results.append(dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
        return res
    
    #Tìm kiếm theo khoảng giá tiền
    @app.route('/book/searchbymoney')
    def SearchByMoney():
        cursor = conn.cursor()
        MFrom = flask.request.json.get('mfrom')
        MTo = flask.request.json.get('mto')
        sql =  "select * from tSach	where DonGiaBan between ? and ?"
        cursor.execute(sql,MFrom,MTo) #thực thi
        results = [] #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results.append(dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
        return res
    
    # - Tính tổng số tiền bán được theo tháng và năm
    @app.route('/doanhthu/byyearandmonth')                     
    def DoanhThu():
        cursor = conn.cursor()
        Year = flask.request.json.get('year')
        Month = flask.request.json.get('month')
        sql =  "exec proc_doanh_thu ?, ?"
        cursor.execute(sql,Year,Month) #thực thi
        results = {} #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results = (dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
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
    
    # - Đếm số lượt khách hàng mua sách x trong khoảng thời gian
    @app.route('/book/countcustomer')
    def CountBookByCus():
        cursor = conn.cursor()
        Name = flask.request.json.get('name')
        Date1 = flask.request.json.get('dfrom')
        Date2 = flask.request.json.get('dto')
        sql =  "exec proc_count_cus ?, ? , ?"
        cursor.execute(sql,Name,Date1,Date2) #thực thi
        results = {} #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results = (dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
        return res
    # - Tìm x khách hàng mua nhiều sách nhất
    @app.route('/customer/topcustomer')
    def TopCustomer():
        cursor = conn.cursor()
        num = flask.request.json.get('num')
        sql =  "exec proc_top_cus ?"
        cursor.execute(sql,num) #thực thi
        results = [] #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results.append(dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
        return res
    # - Hiển thị đơn giá bán được giảm 10% đối với sách của nhà xuất bản x
    @app.route('/book/discount')
    def Discount():
        cursor = conn.cursor()
        nxb = flask.request.json.get('nxb')
        sql =  "exec proc_giam_gia ?"
        cursor.execute(sql,nxb) #thực thi
        results = [] #chứa kết quả trả về
        keys = []
        for i in cursor.description:
            keys.append(i[0]) # lấy keys
        for i in cursor.fetchall():
            results.append(dict(zip(keys,i)))        
        res = flask.jsonify(results)
        res.status_code=200
        return res   
                              
                         
    if __name__ == "__main__":
        app.run(host= "192.168.252.1",port=88)
except Exception as e:
    print(e)