import psycopg2

try :
    conn = psycopg2.connect(host="localhost",database = "gsm_new",user="postgres",password='postgres')
    cur = conn.cursor()
    all_data_query = "select * from public.home_allpro"
    cur.execute(all_data_query)
    alldata = cur.fetchall()
    print(alldata[1])
except(Exception,psycopg2.DatabaseError ) as error:
    print(error)
finally:
    if conn is not None:
            conn.close()
            print('Database connection closed.')

