#!/usr/bin/env python3
""" load the dabase with test data"""

from app import db

from database import User

def create_my_user(first_name, last_name, hobbies):
    db.Session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )

    db.sessipon.commit()

    if __name__ == "__main__":
        create_my_user("Felipe", "Botero", "Soccer")
        users = User.query.all()
        print(users)
        create_my_user("Jane", "Smith", "Horses")
        user = User.query.filter_by(first_name="Jane").first()
        print(user)
        create_my_user("John", "Doe", "Basketball")

        
        create_my_user("Abbie", "Road", "Music")
        users = User.query.all()
        print(users)