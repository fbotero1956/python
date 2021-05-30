from app import db
from app.database import Review

def create_product(name, review):
    db.session.add(
        Review(
            name=name,
            reviewText=review
        )
    )
    db.session.commit()

if __name__ == "__main__":
    create_product("Felipe", "The best catalog around")
    create_product("Kelly", "They always deliver quality")
    reviews = Review.query.all()
    print(reviews)