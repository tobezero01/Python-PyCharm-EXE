import datetime
# tim nhieu ngay tiep theo 
if __name__ == '__main__':
    d,m,y = map(int,input().split("/"))
    n = int(input())
    
    D = datetime.date(y,m,y)
    for i in range(n) :
        D+= datetime.timedelta(i)
        print(("%d/%d/%d") % (D.year,D.month,D.day))
    