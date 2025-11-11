from mangum import Mangum

from app import get_app

handler = Mangum(get_app())
