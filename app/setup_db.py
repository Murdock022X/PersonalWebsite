import website.models as models
from website import create_app

def main():

    app = create_app()

    with app.app_context():
        models.db.create_all()
        models.db.session.commit()

        app.logger.info('DB Setup Complete')

if __name__ == '__main__':
    main()