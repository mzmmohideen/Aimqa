class FamilyRouter(object):
    """
    A router to control all database operations on models in
    the myapp2 application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on myapp2 models to 'my_db_2'
        """
        if model._meta.app_label == 'valuation':
            return 'fam'
        return 'default'
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'valuation':
            return 'fam'
        return 'default'

    def allow_syncdb(self, db, model):
        if db == 'fam' or model._meta.app_label == "valuation":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True
 
    # def allow_syncdb(self, db, model):
    #     """
    #     Make sure the 'myapp2' app only appears on the 'other' db
    #     """
    #     if db == 'fam':
    #         return model._meta.app_label == 'valuation'
    #     elif model._meta.app_label == 'valuation':
    #         return False
    #     return None