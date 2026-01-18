from src.app import db, User, app


with app.app_context():
    db.create_all()

    users = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    for name in users:
        db.session.add(User(name=name))
    db.session.commit()

    with open("/seed_output/seed.log", "w") as f:
        f.write("Seed completed\n")

    with open("/seed_output/users.csv", "w") as f:
        for name in users:
            f.write(name + "\n")
