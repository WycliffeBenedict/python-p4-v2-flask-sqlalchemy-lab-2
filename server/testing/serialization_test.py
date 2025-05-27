from app import app, db
from server.models import Customer, Item, Review


class TestSerialization:
    '''models in models.py'''

    def test_customer_is_serializable(self):
        '''customer is serializable'''
        with app.app_context():
            c = Customer(name='Phil')
            i = Item(name='Insulted Mug', price=9.99)
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()
            
            assert c.to_dict()

            

    def test_item_is_serializable(self):
        '''item is serializable'''
        with app.app_context():
            c = Customer(name='Phil')
            i = Item(name='Insulated Mug', price=9.99)
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', item=i, customer=c)
            db.session.add(r)
            db.session.commit()

            assert c.to_dict()

    def test_review_is_serializable(self):
        '''review is serializable'''
        with app.app_context():
            c = Customer()
            i = Item()
            db.session.add_all([c, i])
            db.session.commit()

            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            review_dict = r.to_dict()
            assert review_dict['id']
            assert review_dict['customer']
            assert review_dict['item']
            assert review_dict['comment'] == 'great!'
            assert 'reviews' not in review_dict['customer']
            assert 'reviews' not in review_dict['item']
