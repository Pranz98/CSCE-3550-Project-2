# CSCE-3550-Project-2
Project 2: Extending the JWKS Server
Objective : 
In this project, we aim to enhance the security and functionality of the JWKS (JSON Web Key Set) server by integrating a SQLite database to store private keys. By using a database, the server's private keys can be persisted, ensuring availability even after server restarts or moves. Additionally, this integration helps prevent SQL injection vulnerabilities, making our authentication processes more resilient.
Requirements : 
SQLite Backed Storage
File Name: totally_not_my_privateKeys.db
Table Schema:
CREATE TABLE IF NOT EXISTS keys(
    kid INTEGER PRIMARY KEY AUTOINCREMENT,
    key BLOB NOT NULL,
    exp INTEGER NOT NULL
)
Save Private Keys to the DB:
Private keys should be serialized and stored in the database.
At least one key that expires now (or less) and one key that expires in 1 hour (or more) should be generated and stored.
POST:/auth:
Reads a private key from the database.
If the expired query parameter is not present, reads a valid (unexpired) key. Otherwise, reads an expired key.
Signs a JWT with that private key and returns the JWT.
GET:/.well-known/jwks.json:
Reads all valid (non-expired) private keys from the database.
Creates a JWKS response from those private keys.
Documentation : 
Code should be well-organized and commented where necessary.
Code should be linted according to your language/framework standards.
Tests
Test suite for your language/framework with tests covering various scenarios.
Test coverage should be over 80%.
Blackbox Testing
Ensure the included test client functions against your server.
The test client attempts HTTP Basic auth and then sends a JSON payload.
The test client checks for the presence of the DB file in the current directory.
Expected Outcome : 
A functional JWKS server with a RESTful API that serves public keys with expiry and unique kid to verify JWTs, backed by a SQLite database.
The server should authenticate fake user requests, issue JWTs upon successful authentication, and handle the expired query parameter to issue JWTs signed with an expired key.
