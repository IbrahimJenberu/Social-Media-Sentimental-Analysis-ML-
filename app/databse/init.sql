-- Create the usertable if it doesn't exist
CREATE TABLE IF NOT EXISTS usertable (
    username TEXT,
    password TEXT
);

-- Insert user data into usertable
INSERT INTO usertable (username, password) VALUES 
    ('ebro', 'password123'), 
    ('epha', 'password456'), 
    ('hailab', 'password789');

