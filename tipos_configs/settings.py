FOO = "ZAZ"
BAR = "FOO"


app.config["FOO"] = "OUTRA COISA"
app.config["SQL_ALCHEMY_DB_URI"] = "sqlite://:file.db"
#ou
app.config.update[config]