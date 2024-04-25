import app.website.models as models
from app import app

def main():

    with app.app_context():
        models.db.create_all()
        models.db.session.commit()

        app.logger.info('DB Setup Complete')

if __name__ == '__main__':
    main()