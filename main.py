import mysql.connector as myconn                                                         #mysql connection
c=myconn.connect(host='localhost',password='123',user='root',database='srsmobiles')
if (c.is_connected()):
        pass
cur=c.cursor()

def srsmain():                                                                                               #MAIN MENU
    
    print('             ____________________________________________________')
    print('            |                                                                                                      |')
    print('            |                  SRS MOBILES                                                       |')
    print('            |___________________________________________________|')
    print('')
    print('                A-Z SOFTWARE DEVELOPERS           ')
    print('-----------------------------------------------------')
    print('')
    print('  1.    CUSTOMER  ')
    print('  2.   ADMIN ')
    print('  3.   EXIT  ')
    print('')
    a=int(input('Enter a choice : '))
    print('')
    if  a==1 :
            customer()
                          
    if  a==2 :
            b=input('ENTER  ACCESS CODE :')
            
            if (b=='sunil123'):
                    k=admin()
                    adminselect(k)

                    
def adminselect(k):
                    if  k==1 :
                            p_code=int(input('Enter product code :  '))              #adding data to the table
                            pdct =input('Enter the product name : ')
                            price=int(input('Enter the price : '))
                            stock_available=int(input('Enter the no.of items : '))
                            Ram_GB=int(input('Enter the ram size : '))
                            Internalstorage_GB=int(input('Enter the internal storage : '))
                            Screentype=input('Enter screentype : ')
                            Primarycam_MP=int(input('Primary camera : '))
                            Frontcam_MP=int(input('Frontcamera : '))
                            Batterycapacity_mAh=int(input('Battery capacity : '))
                            Processor=input('Processor : ')
                            q1="insert into mobspecs values({},{},{},'{}',{},{},{},'{}')".format(p_code,Ram_GB,Internalstorage_GB,Screentype,Primarycam_MP,Frontcam_MP,Batterycapacity_mAh,Processor)
                            q2="insert into mobiles values({} ,'{}',{},{})".format(p_code,pdct,price,stock_available)
                            cur.execute(q1)
                            cur.execute(q2)
                            c.commit()
                            print('DATA ADDED SUCCESSFULLY')
                            k=admin()
                            
                    elif  k==2:
                           h=int(input('Enter product code or product name : '))      #deleting data
                           q3='delete from mobspecs where p_code={}'.format(h)
                           q4='delete from mobiles where p_code={}'.format(h)
                           cur.execute(q3)
                           cur.execute(q4)
                           c.commit()
                
                           print('successfully deleted')
                           try:
                                     h=int(h)
                                     cur.execute(q3)
                           except :
                                     cur.execute(q3)
                           k=admin()
                           adminselect(k)
                           
                    elif k==3:
                            p=int(input('enter product code: '))                     #modify data
                            stock=int(input('enter new stock'))
                            cur.execute('update mobiles set stock_available ={}  where p_code={}'.format(stock,p))
                            c.commit()
                            print('succes')
                            k=admin()
                            adminselect(k)
                            
                    elif k==4:
                              print('')
                              print( '...................MOBILES.....................')
                              print('')
                              cur.execute('Select * from  mobiles')                  #display data
                              a=cur.fetchall()
                              c.commit()
                              for i in a:
                                     print(i)
                              print('')
                              print('..........MOBSPECS..........')
                              print('')
                              cur.execute('Select * from  mobspecs')
                              a=cur.fetchall()
                              for i in a:
                                     print(i[0],'   ',i[1],'   ',i[2],'   ',i[3],'   ',i[4],'   ',i[5],'   ',i[6],'   ',i[7])
                              print('---------------------------------------------------------')                                     
                              k=admin()
                              adminselect(k)
                              
                    elif k==5:
                             print('main menu')                                      #main
                             srsmain()
                    else:
                            print('Wrong Choice...')
                            k=admin()
                            adminselect(k)
def admin():
                    print('____________________')
                    print('|   ADMIN MENU       |')
                    print('|___________________|')
                    print('|                                      |')
                    print('| 1.ADD                         |')
                    print('| 2.DELETE                 |')
                    print('| 3.MODIFY                 |')
                    print('| 4.INFO                      |')
                    print('| 5.BACK                     |')
                    print('~~~~~~~~~~~~~~~~~')
                    k=int(input('Enter choice : '))
                    return k

                
def customer():
        print('..........MOBILE DETAILS...........')
        print('')
        cur.execute('Select * from  mobiles')
        a=cur.fetchall()
        for i in a:
                print(i[0],'   ',i[1],'   ₹',i[2])
        print('')
        spec=int(input('Enter product code : '))
        cur.execute('Select * from  mobiles where p_code={}'.format(spec))
        a=cur.fetchall()
        a=a[0]
        print('')
        qty=int(input('Enter qty : '))
        print('')
        if  a[3]>= qty:
                        bill[a[1]]=qty
                        choice=add_more()
                        if choice==1:                                               #add item
                               customer()
                        if   choice==2:                                             #confirm and checkout
                             billing()
                             srsmain()
                        elif choice==3:                                             #main
                                 srsmain()
                        else:
                         print('')
                         print('wrong choice ! ! !')
                         print('')
                         add_more()
        else:
                        print('No of items available is ',a[3])
        

                        
def  cust_info():
                 cur.execute('Select * from  mobiles')
                 a=cur.fetchall()
                 for i in a:

                        print(i)
                 p=int(input("enter the product code  :  "))
                 cur.execute("select  *  from mobspecs where p_code={}".format(p))

                 
def cust_bill():
        k=input('Do you wish to continue (y/n) : ')
        if k=='y':
                k=int(input('Enter quantity'))
                cur.execute('select product,qty,price from mobiles')

bill={}
s=0
def  add_more():
                    print('1. ADD MORE ITEMS  ')
                    print('2. CONFIRM AND CHECKOUT ')
                    print('3. EXIT !!')
                    print('')
                    choice=int(input('Enter choice : '))
                    return choice                           

def billing():
                 print('')
                 print('')
                 
                 print('...................BILL.......................')
                 print('')
                 b=bill.keys()
                 s=0
                 for i in b:
                       cur.execute("Select  product,price from  mobiles where product='{}'".format(i))
                       a=cur.fetchall()
                       a=a[0]
                       print('')
                       print('|',a[0],'\t',a[1],'')
                       print('')
                       s+=int(a[1])*bill[a[0]]
                 print('Total amount : ',s)
                 print('')
                 print(".....THANK YOU FOR YOUR PURCHASE.....")
                 print('')
                 print('')
                 
srsmain()

                        
        
                             


                    
                        
        
        
