import geoip2.database

GEOLITE_DB = os.getenv('GEOLITE_DB', None)

class Location:
    def __init__(self, IP, db_path=GEOLITE_DB):
        self.IP = IP
        self.reader = geoip2.database.Reader(db_path)
        self.response = self.reader.city(self.IP)
    
    def get_city(self):
        return self.response.city.name

    def get_postalcode(self):
        return self.response.postal.code

    def get_country(self):
        return self.response.country.name

    def get_state(self):
        return self.response.subdivisions.most_specific.name

