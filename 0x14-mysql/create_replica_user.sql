-- Write a script that creates a replica user
-- with necessary permissions
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user280hbtn';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
