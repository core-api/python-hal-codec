from coreapi import Document, Link, Field
from hal_codec import HALCodec


hal_bytestring = b'''{
    "_links": {
        "self": {"href": "/orders"},
        "curies": [{"name": "ea", "href": "http://example.com/docs/rels/{rel}", "templated": true}],
        "next": {"href": "/orders?page=2"},
        "ea:find": {
            "href": "/orders{?id}",
            "templated": true
        },
        "ea:admin": [{
            "href": "/admins/2",
            "title": "Fred"
        }, {
            "href": "/admins/5",
            "title": "Kate"
        }]
    },
    "currentlyProcessing": 14,
    "shippedToday": 20,
    "_embedded": {
        "ea:order": [{
            "_links": {
                "self": {"href": "/orders/123"},
                "ea:basket": {"href": "/baskets/98712"},
                "ea:customer": {"href": "/customers/7809"}
            },
            "total": 30.00,
            "currency": "USD",
            "status": "shipped"
        }, {
            "_links": {
                "self": {"href": "/orders/124"},
                "ea:basket": {"href": "/baskets/97213"},
                "ea:customer": {"href": "/customers/12369"}
            },
            "total": 20.00,
            "currency": "USD",
            "status": "processing"
        }]
    }
}'''


hal_document = Document(
    url=u'/orders',
    title='',
    content={
        u'admin': [
            Link(url=u'/admins/2'),
            Link(url=u'/admins/5')
        ],
        u'currentlyProcessing': 14,
        u'order': [
            Document(
                url=u'/orders/123',
                title='',
                content={
                    u'currency': u'USD',
                    u'status': u'shipped',
                    u'total': 30.0,
                    u'basket': Link(url=u'/baskets/98712'),
                    u'customer': Link(url=u'/customers/7809')
                }
            ),
            Document(
                url=u'/orders/124',
                title='',
                content={
                    u'currency': u'USD',
                    u'status': u'processing',
                    u'total': 20.0,
                    u'basket': Link(url=u'/baskets/97213'),
                    u'customer': Link(url=u'/customers/12369')
                }
            )
        ],
        u'shippedToday': 20,
        u'find': Link(url=u'/orders{?id}', fields=[Field(u'id', location='path')]),
        u'next': Link(url=u'/orders?page=2')
    }
)


def test_load():
    codec = HALCodec()
    doc = codec.load(hal_bytestring)
    assert doc == hal_document
