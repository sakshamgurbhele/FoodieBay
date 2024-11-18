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