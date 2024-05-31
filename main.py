# Inventory management system
 
# importing modules
import os
import msvcrt

# Product class
class Product :
    def __init__(self,id,name,description,quantity,price):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def get_id(self) :
        return self.id        

    def get_name(self) :
        return self.name 
           
    def get_description(self) :
        return self.description        
    
    def get_quantity(self) :
        return self.quantity        
    
    def get_price(self) :
        return self.price     
       
    def get_details(self) :
        return f'id: {self.id} , name: {self.name} , description: {self.description} , quantity: {self.quantity} , price: {self.price}'

    def get_raw_details(self) :
        return f'{self.id},{self.name},{self.description},{self.quantity},{self.price}'
    
    def get_stock_details(self) :
        return f'id: {self.id} , product name: {self.name} , quantity : {self.quantity}'
    
# Supplier Class
class Supplier :
    def __init__(self,sup_id,sup_name,sup_contact,sup_products):
        self.sup_id = sup_id
        self.sup_name = sup_name
        self.sup_contact = sup_contact
        self.sup_products = sup_products

    def get_sup_id(self) :
        return self.sup_id

    def get_sup_name(self) :
        return self.sup_name

    def get_sup_contact(self) :
        return self.sup_contact

    def get_sup_products(self) :
        return self.sup_products

    def get_details(self) :
        return f'Supplier id: {self.sup_id}, Supplier name: {self.sup_name}, Supplier contact information: {self.sup_contact}, Supplier Products: {self.sup_products}'

    def get_raw_details(self) :
        return f'{self.sup_id}|{self.sup_name}|{self.sup_contact}|{self.sup_products}'
    
# purchase order class
class PurchaseOrder :
    def __init__(self,order_id,supplier,product_sku,quantity,status):
        self.order_id = order_id
        self.supplier = supplier
        self.product_sku = product_sku
        self.quantity = quantity
        self.status = status
    
    def get_order_id(self) :
        return self.order_id
    
    def get_supplier(self) :
        return self.supplier
    
    def get_product_sku(self) :
        return self.product_sku
    
    def get_quantity(self) :
        return self.quantity
    
    def get_status(self) :
        return self.status
    
    def get_details(self) :
        return f'Order ID: {self.order_id}, Supplier: {self.supplier}, Product SKU: {self.product_sku}, Quantity: {self.quantity}, Status: {self.status}'
    
    def get_raw_details(self) :
        return f'{self.order_id},{self.supplier},{self.product_sku},{self.quantity},{self.status}'

# storage class
class Storage :
    
    # for product management
    def storeProduct(product) :
        try :
            with open('product.txt','a+') as f:
                f.write(f'{product[0]},{product[1]},{product[2]},{product[3]},{product[4]}\n')
                print('\nProduct stored successfully\n')
        except :
            print('Something went wrong while storing product information')

        finally :
            f.close()

    def getProduct() :
        if (os.path.exists('product.txt')) :
            try : 
                with open('product.txt','r') as f :
                    data = f.read().split('\n')
                    productData = list()
                    for i in data :
                        product_list = i.split(',')
                        if (len(product_list)>4) :
                            product = Product(product_list[0],product_list[1],product_list[2],product_list[3],product_list[4])
                            productData.append(product)
                    return productData
            finally :
                f.close()     

    def updateProduct(productData) :
        if (os.path.exists('product.txt')) :
            try : 
                with open('product.txt','w') as f :
                    for product in productData :
                        f.write(f'{product.get_raw_details()}\n')
            finally :
                f.close()

    # for supplier management
    def storeSupplier(supplier) :
        try :
            with open('supplier.txt','a+') as f:
                f.write(f'{supplier[0]}|{supplier[1]}|{supplier[2]}|{supplier[3]}\n')
                print('\nSupplier stored successfully\n')
        except :
            print('Something went wrong while storing supplier information')
        finally :
            f.close()

    def getSupplier() :
            if (os.path.exists('supplier.txt')) :
                try : 
                    with open('supplier.txt','r') as f :
                        data = f.read().split('\n')
                        supplierData = list()
                        for i in data :
                            supplier_list = i.split('|')
                            if (len(supplier_list)>3) :
                                supplier = Supplier(supplier_list[0],supplier_list[1],supplier_list[2],supplier_list[3])
                                supplierData.append(supplier)
                        return supplierData
                finally :
                    f.close()     
    
    def updateSupplier(supplierData) :
        if (os.path.exists('supplier.txt')) :
            try : 
                with open('supplier.txt','w') as f :
                    for supplier in supplierData :
                        f.write(f'{supplier.get_raw_details()}\n')
            finally :
                f.close()
    
    # order management functions
    def storePurchaseOrder(purchaseOrder) :
        try :
            with open('order.txt','a+') as f:
                f.write(f'{purchaseOrder[0]},{purchaseOrder[1]},{purchaseOrder[2]},{purchaseOrder[3]},{purchaseOrder[4]}\n')
                print('\nPurchase Order stored successfully\n')
        except :
            print('Something went wrong while storing order information')

        finally :
            f.close()

    def getPurchaseOrder() :
        if (os.path.exists('order.txt')) :
            try : 
                with open('order.txt','r') as f :
                    data = f.read().split('\n')
                    orderData = list()
                    for i in data :
                        order_list = i.split(',')
                        if (len(order_list)>4) :
                            order = PurchaseOrder(order_list[0],order_list[1],order_list[2],order_list[3],order_list[4])
                            orderData.append(order)
                    return orderData
            finally :
                f.close()     
    
    def updatePurchaseorder(orderData) :
        if (os.path.exists('order.txt')) :
            try : 
                with open('order.txt','w') as f :
                    for order in orderData :
                        f.write(f'{order.get_raw_details()}\n')
            finally :
                f.close()

# product functions to perform specific tasks
def add_product() :
    id = str(input('Enter product id :'))
    name = str(input('Enter product name :'))
    description = str(input('Enter product description :'))
    quantity = str(input('Enter product quantity :'))
    price = str(input('Enter product price :'))
    Storage.storeProduct([id,name,description,quantity,price])
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def update_product(productData) :
    id = str(input('Enter product id :'))
    product_found = False
    for product in productData :
        if(product.get_id() == id) :
            product_found = True
            try :
                productData.remove(product)
                new_name = str(input('Enter product name :'))
                new_description = str(input('Enter product description :'))
                new_quantity = str(input('Enter product quantity :'))
                new_price = str(input('Enter product price :'))
                new_product = Product(id,new_name,new_description,new_quantity,new_price)
                productData.append(new_product)
                print('\nProduct updated successfully\n')
            except :
                print('Error occured >>')
    if (product_found == False) :
        print('Product Not found')
    Storage.updateProduct(productData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def delete_product(productData) :
    id = str(input('Enter product id :'))
    product_found = False
    for product in productData :
        if(product.get_id() == id) :
            product_found = True
            productData.remove(product)
            print('\nProduct deleted successfully\n')
    if(product_found == False) :
        print('\nProduct not found\n')
    Storage.updateProduct(productData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def view_product(productData) :
    os.system('cls')
    print('\n View Products : \n')
    try :
        for product in productData :
            print(product.get_details())
        print('\n')
    except :
        print('Error occurred, try again after adding product....\n')

    print("Press any key to go back to main menu...")
    msvcrt.getch()

# supplier functions to perform specific task
def add_supplier() :
    sup_id = str(input('Enter supplier id :'))
    sup_name = str(input('Enter supplier name :'))
    sup_contact = str(input('Enter contact information :'))
    sup_products = str(input('Enter product supplied :'))
    Storage.storeSupplier([sup_id,sup_name,sup_contact,sup_products])
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def update_supplier(supplierData) :
    sup_id = str(input('Enter supplier id :'))
    supplier_found = False
    for supplier in supplierData :
        if(supplier.get_sup_id() == sup_id) :
            supplier_found = True
            try :
                supplierData.remove(supplier)
                new_sup_name = str(input('Enter supplier name :'))
                new_sup_contact = str(input('Enter supplier contact information :'))
                new_sup_products = str(input('Enter supplier products :'))
                new_supplier = Supplier(sup_id,new_sup_name,new_sup_contact,new_sup_products)
                supplierData.append(new_supplier)
                print('\nSupplier updated successfully\n')
            except :
                print('Error occured >>')
    if (supplier_found == False) :
        print('Supplier Not found')
    Storage.updateSupplier(supplierData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def delete_supplier(supplierData) :
    sup_id = str(input('Enter supplier id :'))
    supplier_found = False
    for supplier in supplierData :
        if(supplier.get_sup_id() == sup_id) :
            supplier_found = True
            supplierData.remove(supplier)
            print('\nSupplier deleted successfully\n')
    if(supplier_found == False) :
        print('\nSupplier not found\n')
    Storage.updateSupplier(supplierData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def view_supplier(supplierData) :
    os.system('cls')
    print('\n View Suppliers : \n')
    try :
        for supplier in supplierData :
            print(supplier.get_details())
        print('\n')
    except :
        print('Error occurred, try again after adding supplier....\n')
    print("Press any key to go back to main menu...")
    msvcrt.getch()

# stock management functions
def view_stock_level(productData) :
    os.system('cls')
    print('\n View Stock Level : \n')
    try :
        for product in productData :
            print(product.get_stock_details())
        print('\n')
    except :
        print('Error occurred, try again after adding product....\n')
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def update_stock_level(productData) :
    id = str(input('Enter product id :'))
    product_found = False
    for product in productData :
        if(product.get_id() == id) :
            product_found = True
            try :
                productData.remove(product)
                name = product.get_name()
                description = product.get_description()
                price = product.get_price()
                new_quantity = str(input('Enter product quantity :'))
                new_product = Product(id,name,description,new_quantity,price)
                productData.append(new_product)
                print('\nStock updated successfully\n')
            except :
                print('Error occured >>')
    if (product_found == False) :
        print('Product Not found')
    Storage.updateProduct(productData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

# order management functions
def create_purchase_order() :
    order_id = str(input('Enter order id :'))
    supplier = str(input('Enter supplier name :'))
    sku = str(input('Enter product SKU :'))
    quantity = str(input('Enter product quantity :'))
    status = "pending"
    Storage.storePurchaseOrder([order_id,supplier,sku,quantity,status])
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def update_purchase_order(orderData) :
    order_id = str(input('Enter order id :'))
    order_found = False
    for order in orderData :
        if(order.get_order_id() == order_id) :
            order_found = True
            try :
                orderData.remove(order)
                supplier = str(input('Enter supplier name:'))
                product_sku = str(input('Enter product sku:'))
                quantity = str(input('Enter quantity:'))
                status = 'pending'
                new_order = PurchaseOrder(order_id,supplier,product_sku,quantity,status)
                orderData.append(new_order)
                print('\nOrder updated successfully\n')
            except :
                print('Error occured >>')
    if (order_found == False) :
        print('Order Not found')
    Storage.updatePurchaseorder(orderData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

def view_purchase_order(orderData) :
    os.system('cls')
    print('\n View Purchase Orders : \n')
    try :
        for order in orderData :
            print(order.get_details())
        print('\n')
    except :
        print('Error occurred, try again after adding product....\n')

    print("Press any key to go back to main menu...")
    msvcrt.getch()

def update_order_status(orderData) :
    order_id = str(input('Enter order id :'))
    order_found = False
    try :
        for order in orderData :
                if(order.get_order_id() == order_id) :
                    order_found = True
                    orderData.remove(order)
                    supplier = order.get_supplier()
                    product_sku = order.get_product_sku()
                    quantity = order.get_quantity()
                    status = str(input('Enter order Status :'))
                    new_order = PurchaseOrder(order_id,supplier,product_sku,quantity,status)
                    orderData.append(new_order)
                    print('\nStatus updated successfully\n')
        if (order_found == False) :
             print('Order Not found')
    except :
        print('Error occured. Try again after creating purchase order...')
    Storage.updatePurchaseorder(orderData)
    print("Press any key to go back to main menu...")
    msvcrt.getch()

# end message to exit program
def end_message() :
    os.system('cls')
    print('***************************************')
    print('\tWelcome to TrackSphere')
    print('***************************************\n')
    print('\nThank you for using our inventory management system. Have a good day ^_^\n')

# Main Code :- showing the user interface of inventory management
program_state = True
while(program_state) :
    os.system('cls')
    print('***************************************')
    print('\tWelcome to TrackSphere')
    print('***************************************\n')
    print('1. Product Management')
    print('2. Supplier Management')
    print('3. Stock Tracking')
    print('4. Order Management')
    print('5. Exit')
    
    try :
        option = int(input('Choose an option :'))
    except :
        print('You entered wrong input!! try again')
        option = int(input('Choose an option :'))

    # getting all the older data from file
    productData = Storage.getProduct()
    supplierData = Storage.getSupplier()
    orderData = Storage.getPurchaseOrder() 

    # checking the user input
    match option :
        case 1 :
            os.system('cls')
            # showing the user interface of inventory management
            print('\n Product Management Menu\n')
            print('1. Add Product')
            print('2. Update Product')
            print('3. Delete Product')
            print('4. View Product')
            print('5. Main Menu\n')
            try :
                option = int(input('Choose an option :'))
            except :
                print('You entered wrong input!! try again')
                option = int(input('Choose an option :'))

            match option :
                case 1 :
                    add_product()
                case 2 :
                    update_product(productData)
                case 3 :
                    delete_product(productData)
                case 4 :
                    view_product(productData)
                case 5 :
                    exit
        case 2 :
            os.system('cls')
            print('\nSupplier Management Menu\n')

            print('1. Add Supplier')
            print('2. Update Supplier')
            print('3. Delete Supplier')
            print('4. View Suppliers')
            print('5. Main Menu\n')

            try :
                option = int(input('Choose an option :'))
            except :
                print('You entered wrong input!! try again')
                option = int(input('Choose an option :'))

            match option :
                case 1 :
                    add_supplier()
                case 2 :
                    update_supplier(supplierData)
                case 3 :
                    delete_supplier(supplierData)
                case 4 :
                    view_supplier(supplierData)
                case 5 :
                    exit
        case 3 :
            os.system('cls')
            print('\nStock Tracking Menu\n')
            print('1. View Stock Level')
            print('2. Update Stock Level')
            print('3. Main Menu\n')

            try :
                option = int(input('Choose an option :'))
            except :
                print('You entered wrong input!! try again')
                option = int(input('Choose an option :'))

            match option :
                case 1 :
                    view_stock_level(productData)
                case 2 :
                    update_stock_level(productData)
                case 3 :
                    exit
        case 4 :
            os.system('cls')
            print('\nOrder Management Menu\n')
            print('1. Create Purchase Order')
            print('2. Update Purchase Order')
            print('3. View Purchase Order')
            print('4. Update Order Status')
            print('5. Main Menu\n')
            try :
                option = int(input('Choose an option :'))
            except :
                print('You entered wrong input!! try again')
                option = int(input('Choose an option :'))
            match option :
                case 1 :
                    create_purchase_order()
                case 2 :
                    update_purchase_order(orderData)
                case 3 :                    
                    view_purchase_order(orderData)
                case 4 :
                    update_order_status(orderData)
                case 5 :
                    exit
        case 5 :
            end_message()
            program_state = False
            
        
        
