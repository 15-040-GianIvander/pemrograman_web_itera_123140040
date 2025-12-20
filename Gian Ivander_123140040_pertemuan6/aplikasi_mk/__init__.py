from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from .models.meta import Base

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')

    # 🔥 INI BARIS PENTING (AUTO CREATE TABLE)
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)

    config = Configurator(settings=settings)

    def dbsession(request):
        session = DBSession()
        request.add_finished_callback(lambda req: session.close())
        return session

    config.add_request_method(dbsession, 'dbsession', reify=True)

    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
