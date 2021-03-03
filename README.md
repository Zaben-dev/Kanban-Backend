# Kanban-Backend

W przypadku błędu:
<p><b>django.db.migrations.exceptions.MigrationSchemaMissing: 
Unable to create the django_migrations table ((1064, "You have an error in your SQL syntax;
check the manual that corresponds to your MySQL server version for the right syntax to use near '(6) NOT NULL)' at line 1"))</b></p>

Wykonaj downgrade Django do wersji <b>2.0</b>: <p>pip install Django==2.0.0 -i https://pypi.douban.com/simple</p> 
