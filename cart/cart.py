from FoodieBay.models import fooditem

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #get the current session-key if exist
        cart = self.session.get('session_key')
        
        #if the user if new, NO-session-key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make cart availble to all pages of app
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        
        #logic
        if product_id in self.cart:
            self.cart[product_id] = int(product_qty)
            # pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        
    def __len__(self):
        return len(self.cart)
        
    def get_prods(self):
        # get ids from the cart
        product_ids = self.cart.keys()
        # using id to lookup fooditems in database
        products = fooditem.objects.filter(id__in=product_ids)
        #return those products
        return products
        
    def get_quants(self):
        quantities = self.cart
        return quantities
        
    def delete(self, product):
        product_id = str(product)
            #delete from the dictinory cart 
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
    
    def get_total(self):
           
        product_ids = self.cart.keys()
        products = fooditem.objects.filter(id__in=product_ids)
        quantities = self.cart
        #total
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)
        
        # self.cart[total] = int(total)
        self.session.modified = True
        return total
        
    # # def save(self):
    #     """ Save cart back to session or database (depending on implementation) """
    #     session = self.session
    #     session['cart'] = self.cart
    #     session.modified = True
        