from faker import Faker
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
load_dotenv()

fake = Faker()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import User, Trainer


with app.app_context():
    db.drop_all()
    db.create_all()
        
    demouser = User(username='satoshi', 
                    hashed_password=generate_password_hash('password'), 
                    rank='Novice',
                    boulderbadge=False,
                    cascadebadge=False,
                    thunderbadge=False,
                    rainbowbadge=False,
                    soulbadge=False,
                    marshbadge=False,
                    volcanobadge=False,
                    earthbadge=False,
                    beatElite4_1=False,
                    beatElite4_2=False,
                    beatElite4_3=False,
                    beatElite4_4=False,
                    beatChampion=False,
                    )
    
    # trainers = Trainer(name="Brock" slot_1="")
    db.session.add(demouser)
    


    # db.session.add(Chat(jobseekers_id=1, companies_id=1))
    # db.session.add(Chat(jobseekers_id=1, companies_id=3))
    # db.session.add(Chat(jobseekers_id=2, companies_id=1))
    # db.session.add(Chat(jobseekers_id=2, companies_id=3))
    # db.session.add(Chat(jobseekers_id=3, companies_id=3))
    # db.session.add(Chat(jobseekers_id=3, companies_id=4))
    # db.session.add(Chat(jobseekers_id=4, companies_id=2))
    # db.session.add(Chat(jobseekers_id=4, companies_id=4))
    # db.session.add(Chat(jobseekers_id=5, companies_id=2))
    # db.session.add(Chat(jobseekers_id=5, companies_id=5))

    # jobs = [fake.job(), fake.job(), fake.job(), fake.job(), fake.job()]
    # db.session.add(Experience(title=jobs[0], jobseekers_id=1, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[1], jobseekers_id=2, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[2], jobseekers_id=3, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[3], jobseekers_id=4, date_start='now', date_end='now', description=fake.text()))
    # db.session.add(Experience(title=jobs[4], jobseekers_id=5, date_start='now', date_end='now', description=fake.text()))

    # db.session.add(Opening(companies_id=1, title=jobs[0], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=1, title=jobs[1], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=2, title=jobs[3], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=2, title=jobs[4], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=3, title=jobs[0], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=3, title=jobs[1], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=3, title=jobs[2], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=4, title=jobs[3], description=fake.text(), created_at='now'))
    # db.session.add(Opening(companies_id=5, title=jobs[4], description=fake.text(), created_at='now'))

    # companies = Company.query.all()
    # jobseekers = Jobseeker.query.all()
    # openings = []
    # _ = [openings.extend(c.openings) for c in companies]
    # for opening in openings:
    #     for jobseeker in jobseekers:
    #         db.session.add(Swipe(jobseekers_id=jobseeker.id, openings_id=opening.id, created_at='now', swiped_right=True, super_swipe=True, role='company'))

    db.session.commit()
