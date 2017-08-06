from flask import jsonify, make_response, abort

from . import app, mongo


FRUITS = {
    'apple',
    'banana',
    'orange',
    'strawberry',
}

VEGETABLES = {
    'beetroot',
    'carrot',
    'celery',
    'cucumber',
}


@app.route('/api/company/<int:company_id>/employees')
def get_employees(company_id):
    employees = list(mongo.db.people.find({
        'company_id': company_id,
    }))

    return jsonify(employees)


@app.route('/api/people/<int:person1>/<int:person2>')
def get_people(person1, person2):
    people = list(mongo.db.people.find({
        'index': {
            '$in': [person1, person2]
        }},
        {
            '_id': 0,
            'name': 1,
            'age': 1,
            'address':1,
            'phone': 1,
            'friends': 1,
        }))

    if len(people) != 2:
        abort(404)

    person1_friends = set(e['index'] for e in people[0].get('friends', []))
    person2_friends = set(e['index'] for e in people[1].get('friends', []))

    common_friends = person1_friends.intersection(person2_friends)

    if common_friends:
        common_friends = list(mongo.db.people.find({
            'index': {
                '$in': list(common_friends)
            },
            'has_died': False,
            'eyeColor': 'brown'
            },
            {
                '_id': 0,
                'name' : 1
            }))

    for p in people:
        p.pop('friends')

    return jsonify({
        'people': [people[0], people[1]],
        'common_friends': [e['name'] for e in common_friends],
    })


@app.route('/api/person/<int:person>')
def get_person(person):
    try:
        person = list(mongo.db.people.find({
            'index': person,
            },
            {
                '_id': 0,
                'name': 1,
                'age': 1,
                'favouriteFood':1,
                'email': 1,
            }))[0]
    except IndexError:
        abort(404)

    return jsonify({
        'username': person['email'].strip().split('@')[0],
        'age': person['age'],
        'vegetables': [e for e in person['favouriteFood'] if e in VEGETABLES],
        'fruits': [e for e in person['favouriteFood'] if e in FRUITS],
        'all': person['favouriteFood'],
    })

