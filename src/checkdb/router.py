class CheckerRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'college':
            return 'college'
        elif model._meta.app_label == 'school':
            return 'school'
        return 'default'

    
    def db_for_write(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        if model._meta.app_label == 'college':
            return 'college'
        elif model._meta.app_label == 'school':
            return 'school'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'college' or obj2._meta.app_label == 'college':
            return True
        elif 'college' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'school' or obj2._meta.app_label == 'school':
            return True
        elif 'school' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label == 'college':
            return db == 'college'
        elif app_label == 'school':
            return db == 'school'
        return None


