import fabutils

from django.conf import settings

from fabric.contrib import django

django.settings_module('deka_backend.settings')

fabutils.autodiscover_environments(settings)


class Deploy(fabutils.GunicornMixin,
             fabutils.VirtualenvMixin, fabutils.Deployment):
    """
    Base deployment class, do not use it directly in the commands
    """
    db_backup_handler_class = fabutils.PostgresqlDatabaseBackup
    db_restore_handler_class = fabutils.PostgresqlDatabaseRestore

    frontend_dir = 'deka-frontend'

    def deploy_tasks(self):
        """
        Manage the order of the deploy tasks. Overload this if you want to add functionalities
        """
        self.fab_update_repo()
        self.fab_install_requirements()
        self.fab_migrate()
        self.fab_clean_pyc_files()
        self.fab_collectstatic()
        self.fab_restart_instance()
        self.fab_check_deploy()
    
    # def fab_update_yarn(self):
    #     """
    #     Installs the dependencies for the frontend build using yarn
    #     """

    #     self.run_raw_command('yarn install')

    # def fab_build(self):
    #     if self.env.is_production or self.env.is_staging:
    #         self.run_raw_command('yarn build:aot:prod')


    # def fab_frontend_deploy(self):
    #     """
    #     Build the frontend of the application
    #     """
    #     with cd("".join([self.env.core_dir, self.frontend_dir])):
    #         print(green("Updating repo"))
    #         self.run_raw_command('git fetch --all')
    #         self.run_raw_command('git checkout %s' % self.env.branch)
    #         self.run_raw_command('git pull origin %s' % self.env.branch)
    #         self.fab_update_npm()
    #         self.fab_build()


fabutils.register_class(Deploy, settings)
fabutils.register_class(PostgresqlDatabaseOperations, settings)
fabutils.register_class(fabutils.RemoteDatabaseOperations, settings)