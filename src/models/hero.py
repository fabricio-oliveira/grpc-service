from models import company

companies = [
    {"id": 1, "name": "Batman", "company": company.index(0)},
    {"id": 2, "name": "Spider Man", "company": company.index(1)}
]


def all():
    return companies
