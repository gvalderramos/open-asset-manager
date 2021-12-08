db.createUser({
    user: "dbuser",
    pwd: "Pass1234",
    roles: [
        {
            role: "readWrite",
            db: "openassetmanagerdb"
        }
    ]
})