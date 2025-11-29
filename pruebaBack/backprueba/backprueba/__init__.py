import pymysql
pymysql.install_as_MySQLdb()
# Hack de compatibilidad: hacer que Django “vea” una versión reciente
pymysql.version_info = (2, 1, 1, "final", 0)
pymysql.__version__ = "2.1.1"
