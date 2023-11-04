def load_categories():
    return [{
        'id': 1,
        'name': 'Milk tea'
    }, {
        'id': 2,
        'name': 'Tea'
    }, {
        'id': 3,
        'name': 'Food'
    }]


def load_products(kw=None):
    products= [{
        "id": 1,
        "name": "Trà sữa thái xanh",
        "price": 25000,
        "image": "https://images.unsplash.com/photo-1592284441621-581ebd2e677d?auto=format&fit=crop&q=80&w=1887&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }, {"id": 2,
        "name": "Trà sữa truyền thống",
        "price": 25000,
        "image": "https://i.pinimg.com/736x/5f/7a/29/5f7a29861796858f19fe248316e1b22e.jpg"
        }, {
        "id": 3,
        "name": "Trà sữa thái đỏ",
        "price": 25000,
        "image": "https://banner2.cleanpng.com/20180327/icq/kisspng-bubble-tea-thai-tea-milk-cafe-thai-5ab9dd70e6c6e6.2715498915221302889453.jpg"
    }, {
        "id": 4,
        "name": "Trà xanh tắc",
        "price": 20000,
        "image": "https://png.pngtree.com/element_our/20190603/ourlarge/pngtree-glass-cup-of-green-tea-decoration-illustration-image_1451420.jpg"
    }, {
        "id": 5,
        "name": "Hồng trà",
        "price": 15000,
        "image": "https://png.pngtree.com/png-clipart/20190617/original/pngtree-hand-painted-health-drink-rose-tea-png-image_3889545.jpg"
    }, {
        "id": 6,
        "name": "Tokbokki",
        "price": 15000,
        "image": "https://img.freepik.com/premium-psd/cartoon-bowl-tteokbokki-food-with-words-transparent-background_345363-8.jpg?w=2000"
    }]
    if kw: #is not null
        products = [p for p in products if p['name'].find(kw) >=0]

    return products