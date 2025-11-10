from mangum import Mangum

from app import get_app

app = get_app()

handler = Mangum(app)